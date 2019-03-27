# AlphaSortable
Alphabetically sortable integer equivalents

<pre>
# Functions for converting integers into lexiographically sortable strings
# and back (lexical order == dictionary order == alphabetical order).
# Supported range: 0 - 100 quadrillions
#
# Uses only lower case chars for compatibility with any sorting algorithm.
#
#
# Decoding/ Encoding:
# 0-9 => a-j
# k==10, l==100, m==1000, ...
#
# Encoding/Decoding in pairs, except for last char: 
# lckbb <=> 211
# [lc]->100*2,[kb]->10*1,[b]->1 ==> 211
#

Usage: 
  ToAlphaSortable(1791535639) => "sbrhqjpbofndmflgkdj"
  FromAlphaSortable("sbrhqjpbofndmflgkdj") => 1791535639

<pre>
