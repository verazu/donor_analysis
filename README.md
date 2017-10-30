# Documentation #


## Dependencies ##

The standard modules used in the code were `numpy`, `collections` (`defaultdict`) and `re`.

## Performance ##

The code has been tested using a donor txt file downloaded from FEC's website (size 828.8mb). It can be further sped up with a customized function calculating rolling median. But I think the current implementation is fast enough relative to the input file size.

## Miscellaneous ##

The code has been tested on Ubuntu 17.10 using Python 3.6.3.
