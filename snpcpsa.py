#!/usr/bin/env python2.7
# Getting to know os.walk
import os, regex, sys

argquan=len(sys.argv)
if arguqan != 1 and argquan != 2:
	print "This script can be run with zero or one argument. With zero arguments or if 1 argumentts the \".\", the current directory will be use to search for fastq.gz files"
	print "The first argument neess to be a directory path because this script works by directories"
	sys.exit(2)

# Primarily we expected absolute paths .. but the following condition, a codeblock will take care of relative paths too.
if argquan == 1:
		PATH=os.getcwd()
else:
	lc1=sys.argv[1][0]
	a1sz = len(sys.argv[1])
	if a1sz ==1:
		if lc1 == '.':
			PATH=os.getcwd()
		else:
			print "If argument is a single character, only the dot, i.e. CWD, is accepted."
			sys.exit(2)
	else:
		# OK. now argv1 has more than one character
		lc2=sys.argv[1][1]
		if lc1 == '/':
			PATH=sys.argv[1]
		elif lc1 == '.' and lc2 == '/':
			if a1sz == 2:
				print "Sorry, the ./ argument indicate relative path and cannot be aloner. Use . or no arguments, if you want current directory"
				sys.exit(2)
			PATH=os.getcwd() +sys.argv[1][1:]
		else:
			PATH=os.getcwd() +"/"+ sys.argv[1]

print PATH

FLEXT='.fastq.gz' # file extension of interest
r=regex.compile(r'(?:([/_.])+)')

DL= { dp: [r.split(f) for f in fnz if f.endswith(FLEXT)] for dp, dn, fnz in os.walk(PATH)}
# this is a dict, keyed by directory and subdirectory names. Each key has a list of all the files. Each filename is tokenized into a list based on [._/]
# if there are no fastq.gz files in there, the dictionary will be empty.
if not DL or not DL[PATH]:
	print "The specified directory does not contain any fastq.gz files in its root"
	sys.exit(2)

# We can expect different name formats and boh single and pair-end reads
# easiier to treat these separately by settign up

LLSZ=len(DL) # gives number of elements in fqz: i.e. number of fastq.gz file in the PATH

# We create two containers, one a set of unique names, prefixes for each readpair, which will be iterated over, and then a dict based n thse unique names which will be appended to.
UIST=set()
DL0={} # for our single paired reads
DL2={} # for our pair-end reads
print len(DL[PATH])
for J in DL[PATH]:
	UIST.add(J[0])
	if len(J) ==13:
		DL2[J[0]]=[]
	elif len(J) ==5:
		DL0[J[0]]=[]
	else:
		print "fastq.gz filename format is unrecognised. Sorry, this is due to this python code not being robust enough"

# Note: why 5 and 13? well it's just the format of the filenames currently beign dealt with:
# 362711M_S7_L001_R2_001.fastq.gz will come out as 13 strings (note forward lookup regex, saves the tokens as list members as well
# SRR961686.fastq.gz will come out as 5.

# for DL2, we're going to go by threes: DIRNAME, PAIR1FNAME, PAIR2FNAME, repeat. Unfortunately P1 and P2 may not be in the right order.
# attach the main directory
for J in DL2:
	DL2[J].append(PATH)

for J in DL0:
	DL0[J].append(PATH)

for I in DL[PATH]:
	for J in UIST:
		if J == I[0]:
			if len(I) == 13:
				DL2[J].append("".join([K for K in I]))
			elif len(I) == 5:
				DL0[J].append("".join([K for K in I]))
			break

# Procedure: Ensure right pair order (not necessary for single-end reads!)
# So unfortunately we cannot depend on the pairs being sorted in relation to each other.
# So, we'll go through every second and third entry, compare them lexicographically, and switch their positions
# we are a bit stuck if lexicographically it doesn't work that way i.e. left shoul dbe econd, and right first.
# using pythons well-known ability to do this, i.e.
# mylist[1],mylist[0] = mylist[0, mylist[1]
for J in DL2:
	JLEN=len(DL2[J])
	J3L=JLEN/3
	for I in xrange(J3L):
		if(DL2[J][I*3+1]>DL2[J][I*3+2]):
			DL2[J][I*3+2], DL2[J][I*3+1] = DL2[J][I*3+1], DL2[J][I*3+2]

for J in DL2:
	print "%s_R1=%s" % (J, DL2[J][0] + "/" + DL2[J][1])
	print "%s_R2=%s" % (J, DL2[J][0] + "/" + DL2[J][2])
for J in DL0:
	print "%s=%s" % (J, DL0[J][0] + "/" + DL0[J][1])
