# Tutorial: Case studies for task management in science
In this folder you will find examples of how to conduct various scientific tasks.
The case studies are meant to illustrate the approaches and operating
procedures discussed in the handbook documentation.
You should learn from these examples how to efficiently manage, solve, and
document your own projects and tasks.

## MotifSetReduce
This chapter reviews development of the _MotifSetReduce.pl_ script to solve a
common task in dealing with sets of redundant DNA motifs.
The task was motivated by our own research on constructing statistically
validated motifs in putative promoter regions identified on a genome-wide
scale.
In that case, the same motif-finding software was run on distinct data sets
that we expect to give similar results.
Another application would involve running different motif-finding programs on
the same data set.
Either way, after appropriate clustering, we end up with a set of motifs
(represented as frequency matrices) containing quite similar but not identical
entries: different matrices will have somewhat different nucleotide
frequencies, possibly different lengths, and may be shifted relative to each
other.
_MotifSetReduce.pl_ provides a solution to the problem of removing redundancy
from such a set of motifs and providing the best representative, consensus
motifs.

Case study contributed by Volker Brendel (February 2016).
