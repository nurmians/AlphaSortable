# Alphabetically sortable integer equivalents (AlphaSortable)
#
# Functions for converting integers into lexiographically sortable strings
# and back (lexical order == dictionary order == alphabetical order).
# Supported range: 0 - 100 000 000 000 000 000 (100 quadrillions)
#
# Uses only lower case chars for compatibility with any sorting algorithm.
#
# @author: Anssi Nurminen
# @date: 2019-03-27
#
# Decoding/ Encoding:
# 0-9 => a-j
# k==10, l==100, m==1000, ...
#
# Encoding/Decoding in pairs, except for last char: 
# lckbb <=> 211
# [lc]->100*2,[kb]->10*1,[b]->1 ==> 211
#

import sys

def FromAlphaSortable( aStr):	

	retval=0
	# Read in pairs of chars
	for i in range( 0, len( aStr)-1, 2):
		base = 10**(ord( aStr[ i])-(ord('k')-1))		
		mult = ord( aStr[ i+1]) - 97
		retval += base * mult

	retval += ord( aStr[ -1]) - 97
	return retval

def ToAlphaSortable( aInt):	

	aInt = int( aInt)
	if aInt < 0: 
		sys.stderr.write( "ERROR: Negative integers not supported.\n")
		return ""
	num=10
	cur_alpha = 'k'
	remainder = chr(97 + (aInt % 10))	
	retval = [remainder]

	while True:
		aInt = aInt/10
		if aInt == 0: break
		mod = (aInt % 10)
		if mod > 0: # zeros can be omitted wthout affecting order
			remainder = "%s%s" % (chr(97 + mod), cur_alpha)
			retval += remainder
		if cur_alpha == 'z': # Max reached
			retval += (aInt/10)*'kz' 
			break
		cur_alpha = chr( ord( cur_alpha) + 1)


	return "".join(reversed(retval))
	

def TestAlphaSortable( aInt):

	tas = ToAlphaSortable( aInt)
	fas = FromAlphaSortable( tas)
	print "[%s] %i => %s => %s" % ( "OK" if int( fas) == aInt else "FAIL", aInt, tas, fas)
	return (tas, fas)



# TEST
if __name__ == '__main__':

	import random
	nums = []
	strs = []
	for i in range( 20):		
		tas, fas = TestAlphaSortable( random.randint(0, sys.maxint))
		#tas, fas = TestAlphaSortable( random.randint(0, 100000))		
		strs.append( tas)
		nums.append( int( fas))
		tas, fas = TestAlphaSortable( random.randint(0, 1000))		
		strs.append( tas)
		nums.append( int( fas))

	s_nums = sorted( nums)
	s_strs = sorted( strs)
	sort_ok = True

	#print "nums:"
	#print s_nums
	#print "strs:"
	#print s_strs

	for i in range( 10):
		num_index = nums.index( s_nums[ i])
		str_index = strs.index( s_strs[ i])
		if num_index != str_index:
			sort_ok = False
			break
	print "Sort test [%s]" % ("OK" if sort_ok else "FAIL")

	#print "Max:", FromAlphaSortable( "zka")
	#TestAlphaSortable( 10000000000000000)
	#TestAlphaSortable( 99999999999999999)
	TestAlphaSortable( 100000000000000000)
	#TestAlphaSortable( 4000000000000000000)
 
