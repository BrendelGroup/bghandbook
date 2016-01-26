# Basic GREP Tutorial

Grep stands for: <b>g</b>lobally search a <b>r</b>egular <b>e</b>xpression and <b>p</b>rint

And, it does it exactly that. Grep allows you to specify a regular expression of ascii characters and then find all instances of said regular expression in a file or a collection of files. This tool is very useful for searching through genome files and even managing personal files.

# String Searching

Searching for a basic string is quite easy:

```
$ grep "mystring" myfile
```

For case-insensitive search, use the flag -i.
```
$ grep -i "mystring" myfile
```

To count the number of occurrences, use the flag -c.
```
$ grep -c "mystring" myfile
```

To color-code the occurrences, use the flag --color.
```
$ grep --color "mystring" myfile
```

# Regular Expressions

The true power of grep lies in the ability to utilize regular expressions for string search. This gives one significant flexibility in their search input.

The syntax is as follows

```
$ grep <myRegEx> myfile
```

One example of Grep usage is when you want to match a certain item 0 or more times.
```
$ grep "tel*" myfile
```
^This command would return all lines with strings like "te" in 'technology', "tel" in 'telephone', and "tell" in 'tell me'.

Another use is the OR functionality. You want to search for all cases of
the string "fil" or the string "fig".
```
$ grep "fi[l,g]" myfile
```

Other basic operators of regular expressions are:


? - The preceding item is optional and matched at most once.

plus sign -  The preceding item will be matched one or more times.

{x} - The preceding item is matched exactly x times.

{x,} - The preceding item is matched x or more times.

{,y} - The preceding item is matched at most y times.

{x,y} - The preceding item is matched at least x times, but not more than y times.
