# Reducing redundancy in DNA protein motif sets - Addendum 1
Contributed by Volker Brendel, February 2016.

Ok, so we made the point of breaking down a scientific quest into smaller tasks
that have well-defined inputs and outputs, filling out the path to solution,
and providing a documented implementation thereof that can be shared for
reproducible (and potentially scalable) application by our peers.
If the task is done, then why write an addendum?

That raises the question as to when a task is truly done.
Obviously, if we did our job right the first time, then __that__ task __is__ done.
However, more often than not, we keep using the tool and thinking about its
utility, and we get new ideas.
How can we generalized the tool?  What additional functions would be nice to
have?   What related problems might we be able to solve with an adaption of
the initial tool?
This scenario is part and parcel of the scientific process.
I like to think of it as a creative spiral: you go back to the initiation point,
but from a new, broader perspective.
That's part of the joy of doing science: there is the pleasure of finishing
tasks and delivering tools and insights, and there is the fun of getting ten
more ideas with every finished task!

Let's review our case study.

### _MotifSetReduce.pl_ version 2: Quality control of output motifs
Looking at the output of _MotifSetReduce.pl_ from various input files, it was
noticeable that some of the merged (and thus by necessity, some of the input
motifs) were pretty "weak" - short, with few positions that seemed distinctive
at all.
In other word, some of the frequency matrices hardly deserve the distinctive
title of "motif."
Thus, one immediately gets the idea that the software needs to be expanded a bit
to 1) indicate a quality measure for each motif, and indeed each motif position;
2) sort motifs by this quality measure; and 3) optionally remove from consideration
motif positions and entire motifs that don't measure up.

A common measure of distinctiveness of a frequency vector in a motif is its
__information content__, a simple measure of how different the frequencies are
from being all equal.
We can confidently add the following subroutine to our program to produce this
value for a frequency array of length four:

```
sub calcIC {
  my $sum = 0;
  for (my $l=0; $l<4; $l++){
    if($_[$l]>0){
      $sum +=$_[$l] * (log($_[$l])/log(2));
    }
  }
  return(2+$sum);
}
```

You should convince yourself that the subroutine returns a value of 2 if one
frequency is 1.0 and a value of 0 if all frequencies are equally 0.25 (and a
value in between for other frequency vectors).
Thus, the more distinctive the frequency vector is in a given position, the
closer to the maximum value of 2 is its information content.

The remainder is an adaptation from the _formatMotifs.pl_ script in the
[STAMP repository](https://github.com/shaunmahony/stamp.git).
For any motif, we define its core as the continuous _$mmlength_ rows with
maximal cumulative information content (here, _$mmlength_ is the user-set minimal length of motifs to be considered; called _$delta_ in Version 1 of
_MotifSetReduce.pl_).
Then we trim from the original motif left and right ends towards the core,
eliminating end positions of information content less than the user-set
threshold _$mmthreshold_.

The trimming is implemented in the subroutines _trimByIC()_ and _trim_motif()_.
Thanks to our nice data structure _%motifset_, printing out the final trimmed
motif set in decreasing order of overall information content is simply a
matter of invoking the Perl syntax for ordering a hash by hash values; see
_displaymotifset()_ for details.

### What's next?
Is this the end of the story then?
Probably not.
We could add a filter to eliminate trimmed motifs of poor overall quality.
We might want to have different output options for the motifs so that the
output could directly feed into other programs.
In some cases, we might want to have a more convenient display of the various
merging and trimming actions (i.e., think about the _-v_ verbose output, or
additional flags).
But, the next step should be the next step in the creative cycle: apply What
we have, test it thoroughly, get new ideas in the process.
