#!/bin/bash
#Sorts the files within ads.txt, terms.txt, pdates.txt, and prices.txt,
#According to ther key type (Lexicographic sort: pdates/terms; Numerical sort: ads/prices)
#Then removes duplicate lines, prepares the file with external perl script break.pl
#Which replaces delimiters with line breaks, and removes backslashes.
#Using db_load the files are then convereted into Berkeley DB files ready for use.
#The files are organized using hashes (ads) and btrees (terms, pdates, prices)

sort ads.txt -n | uniq | ./break.pl | db_load -T -t hash ad.idx
sort terms.txt | uniq | ./break.pl | db_load -T -t btree te.idx
sort pdates.txt | uniq | ./break.pl | db_load -T -t btree da.idx
sort prices.txt -n | uniq | ./break.pl | db_load -T -t btree pr.idx