# Reducing redundancy in DNA protein motif sets
Contributed by Volker Brendel, February 2016.

In this case study, we'll review development and implementation of an
algorithm to reduce redundancy in a set of DNA motifs.
To formulate the problem, look at part of the input file
_msfile1_ in this directory:

```
MEME version 4
ALPHABET= ACGT

MOTIF motif_Train8_9 10-CGCTAGAGGG
letter-probability matrix: alength= 4 w= 10 nsites= 20 E= 1e-43
0.103   0.786   0.043   0.068
0.16    0.001   0.793   0.046
0.107   0.73    0.063   0.1
0.109   0.317   0.045   0.529
0.941   0.011   0.047   0.001
0.053   0.014   0.869   0.064
0.674   0.101   0.124   0.101
0.047   0.029   0.602   0.322
0.101   0.162   0.585   0.152
0.165   0.058   0.605   0.172

MOTIF motif_Train6_17 17-CCGCTAGA
letter-probability matrix: alength= 4 w= 8 nsites= 20 E= 1e-24
0.001   0.997   0.001   0.001
0.001   0.997   0.001   0.001
0.001   0.001   0.864   0.134
0.001   0.997   0.001   0.001
0.001   0.001   0.001   0.997
0.997   0.001   0.001   0.001
0.001   0.001   0.997   0.001
0.837   0.001   0.161   0.001
```

Shown are two motifs in MEME format, represented as frequency matrices
corresponding the consensus sequences CGCTAGAGGG and CCGCTAGA, respectively.
We can easily agree that the motifs should be aligned as follows as far as
the consensus sequences are concerned:

```
__CGCTAGAGGG_
_CCGCTAGA____
```

However, we have a more formidable task to solve.
First, in general we don't have just two motifs to merge, but _n_ >= 2.
Second, we want to align the actual frequency matrices, not the consensus
sequences.
The output of our algorithm should be a reduced set of motifs, possibly a
single motif, that represents the input set in a non-redundant way.
The Perl script _MotifSetReduce.pl_ provides a possible solution to the problem.
Type

```
MotifSetReduce.pl
MotifSetReduce.pl -m msfile1 -t 0.09
```

on the commandline to see the usage instructions and sample run.

Now let's break down the path to solution.
We have already articulated the input (a file of motifs in format shown in
_msfile1_) and the desired output (a similarly formatted reduced set of motifs).
What remains is to fill in the path ...

### Task 1: Choice of programming language
For this task, choice of programming language is likely to be only an issue of
your personal preference.
Whatever you are most comfortable with should be up to the task.
For this example, I used Perl.

### Task 2: Reading the input into a data structure
A good starting point is always to process the input file with your fledgling
program and make sure that all the data are read into a manageable data structure
that will facilitate the computations to be done.
Here, the data are clearly structured:  we have motifs identified by names on
the "MOTIF" lines, and following a line with details we may not need, there are
rows of nucleotide frequencies (A, C, G, T), as many as there are positions in
the motif.
Thus, we need a 3-dimensional data structure: a motif set consisting of multiple
motifs, each of which comprising multiple arrays of size 4 each containing the
nucleotide frequencies in the respective motif position.
Perl is not exactly the easiest language to encompass multi-dimensional arrays,
but hashes the elements of which are references to other hashes will do.
The following lines of code show how we implemented this, using the motif
names as keys in the _motifset_ hash and constructs like _row01_ ... _row10_ ...
as keys for the positional frequencies for each motif.

```
# Reading in the original motif file:
#
open (MFILE, "< $msfile");
while (defined($line = <MFILE>)) {
  if ( $line =~ /^MOTIF/ ) {
    ($motif1) = $line =~ /^MOTIF (\w+) /;
#   print $motif1, "\n";

# Setting up an empty hash for motif $motif1 in the data structure $motifset
#  (a hash with keys $motif1 and values being hashes with keys row01, row02,
#  ... and values arrays containing the nucleotide frequencies in each motif
#  position; this is the Perl way of representing a 3-dimensional array
#  consisting of motifs, rows, and frequency values):
#
    $motifset{$motif1} = {};
    $r = 0;
  }
  if ( $line =~ /^[0\1]/ ) {
    chomp($line);
    $r++;
    if ($r < 10) {
      $label = "row" . "0$r";
    } else {
      $label = "row" . "$r";
    }

# Here we are adding the frequencies on $line to the proper row key for
# motif $motif1:
#
    @{$motifset{$motif1}{$label}}= split(/\t/,$line);
  }
}

if ($debug) {print "\nDump of motif set as read into program:\n\n", Dumper(%motifset), "\n\n";}
```

Note the "Dumper" command at the end when _$debug_ is set.
Task 2 would not be complete without proof that the code faithfully reads all
the input just as intended.

### Task 3: Defining a distance measure for two aligned motifs
Obviously we need to come up with some measure of similarity between two motifs.
Let's assume first that the motifs are already aligned, maybe each starting at
position 1.
How close are the two frequency vectors in position 1?
Then those in position 2, and so forth until we run out of positions?
The simplest measure might be good enough; enter the sum of squares:

```
sub dsqr {
  my $d = 0.0;
  for (my $i=0; $i<=$#{$_[0]}; $i++) {
    $d += ($_[0][$i] - $_[1][$i]) * ($_[0][$i] - $_[1][$i]);
  }
  return ($d);
}
```

As we need this often, we add the _dsqr()_ to our program.
We can then define the distance of two matrices as the average of the _dsqr()_
values taken over all aligned rows.
Remains to take care of all possible alignments of the two matrices.
To make sense, we require a minimum of _$delta_ aligned rows.
The following schematic shows the possible alignments for two motifs _M_ and
_N_, each of length 5, where _$delta = 3_:

```
_MMMMM___   _MMMMM___   _MMMMM_   __MMMMMM_   ___MMMMMM_
___NNNNN_   __NNNNN__   _NNNNN_   _NNNNN___   _NNNNN____

```

The different alignments can be identified by the offsets _3/1, 2/1, 1/1, 1/2,_
and _1/3_.
The next code section calculates the minimum average _dsqr()_ value for all these cases and reports this value as the distance between the two matrices.

```
@tmpds1 = ();
for ($s=$width1-$delta+1;$s>1;$s--) {
  if ($debug) {
    print "... calculating distance for offsets $s/1:\n";
  }
  $dst = 0.0;
  for ($k=1; $s-1+$k <= $width1 && $k <= $width2; $k++) {
    $l = $s-1+$k;
    if ($l < 10) {$row1 = "row" . "0$l";} else {$row1 = "row" . "$l";}
    if ($k < 10) {$row2 = "row" . "0$k";} else {$row2 = "row" . "$k";}
    if ($debug) {
      print "... adding $row1 @{$motifset{$motif1}{$row1}} versus $row2 @{$motifset{$motif2}{$row2}} dsqr() value\n";
    }
    $dst += dsqr(\@{$motifset{$motif1}{$row1}},\@{$motifset{$motif2}{$row2}});
  }
  $dst = $dst/($k-1);
  push (@tmpds1,$dst);
}
my ($minvs1,$minxs1) = argmin(@tmpds1);
```

### Task 4: Merging two motifs
Take a look at the _mergemotifs()_ function in the code for details, but this
part is rather straightforward: we simply average the frequencies of the
corresponding rows.

### Task 5: Iterative merging of the most similar motifs.
To complete the solution of the overall task, we implement hierarchical clustering.
We calculate all pairwise distances, take the closest two motifs, merge them,
and repeat the procedure with the now reduced set of motifs.
Thanks to the nice data structure we set up for _motifset_, all we have to do
is to add a hash for the newly named merged motif (in the code we simply add the
letter _m_ to the first motif name), then delete the key/value pairs for the
original two motifs.

Remains to set a stopping criterion.
This should not just be when only one motif is left, because we do not want to
force merging of motifs that are not all that similar to start with.
The solution is to set a maximal distance (_$mmthreshold_ in the code; set as
a parameter on the commandline) for two motifs to be considered mergeable.
Empirically, a value of _0.09_ seems to be a reasonable default value, which
corresponds to average frequency differences of _0.15_ in each nucleotide position.

### Task 6: Testing and dissemination
Now that the program is complete, extensive testing should be done to make sure
that the implemented approach works as intended.
In particular, it is always helpful to include "edge cases" in the testing
(roughly speaking, weird input) as well as lots of real data sets.
This step is not completed as of this writing!

At some point after initial testing, the code would best be cleaned up to
make it easier to run different data sets with different parameters.
As you will appreciate, the _MotifSetReduce.pl_ code has a pretty decent
interface and documentation.
__Be polite to your team members!__
Once you invite others to test your code, make it easy, or even better
yet, make it a pleasant and useful learning experience for them.

### Task 7: Framing the solved task in the larger project
Similarly to how the solution of the _MotifSetReduce.pl_ task involved several
subtasks, each clearly defined, solved, and tested, so is the overall task
presumably part of a larger project.
Often it is helpful to frame this in terms of "upstream" and "downstream."
Here the "upstream" refers to how we get the input files.
The "downstream" refers to what to do with the output, e.g how to test that the
consensus motifs indeed capture the biological reality that is probed by the
upstream experiments.

As the work on this larger context gets completed, we will update these pages
with the proper citations!

### Conclusions
Please go over our case studies carefully, learn how the principles apply to
your own specific work, and then try to write up documentation for your work
in similar detail.
Once internalized, the approaches outlined in our handbook will definitely
be of great benefit to you with respect to your increasing your work efficiency
and your work's longterm relevance.
