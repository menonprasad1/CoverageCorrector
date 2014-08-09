import re
import sys
import pdb
import os

print "Coverage File : " + sys.argv[1]
print "Base Directory : " + sys.argv[2]
corrFile = sys.argv[1] + "_corrected"
print "Corrected Coverage : " + corrFile
fd=open(sys.argv[1],"r");
fdwrite=open(corrFile,"w");
ptrn=re.compile("^SF:(.*)");
for line in fd:
	#pdb.set_trace()
	mtch=ptrn.match(line)
	if(mtch is not None):
		if(not os.path.exists(mtch.group(1))):
			wrongPath=mtch.group(1)
			tup1=os.path.split(mtch.group(1)) #tup1[1] is the file
			corrPath=""
			for dir,subdir,files in os.walk(sys.argv[2]):
				if(corrPath != ""):
					break
				for f in files:
					if(f==tup1[1]):
						corrPath=os.path.join(dir,f)
						break
			if(corrPath==""):
				print line + " : " +  "-------Cannot be found"
				print "\n"
			#print tup1[1] + " : " + wrongPath + " : " + corrPath
			corrString="SF:" + corrPath
			fdwrite.write(corrString+"\n")
		else:
			fdwrite.write(line)
	else:
		fdwrite.write(line)
						
