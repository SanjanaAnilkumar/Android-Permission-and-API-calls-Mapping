import sys
import re
data1 = ""
data2 = ""
calls = []
bad_words = ['Callers']
d = dict()
for fil in sys.argv[1:]: 
		with open(fil) as f:
	    		for line in f:
				if not any(bad_word in line for bad_word in bad_words):
					if line.startswith('<') and line.strip().endswith('>'):
						line2 = line.replace(":", ".")
						line2 = re.sub(' .*? ', '', line2)
						line2 = line2.split('(')[0]
						line2 = line2.replace('<', '')
						line2 = line2.replace('>', '')
						line2 = line2.rstrip("\n")
	    					data1 = line2
						var1 = data1
						var2 = data2
						d[var1] = var2
					elif line.startswith('P'):
						line3 = line.rstrip("\n")
						data2 = line3
		with open (sys.argv[-1], "r") as tracefile:
    			for line in tracefile:
				line2 = re.sub(r'\([^)]*\)', '', line)
				for key,value in d.items():
	               			if key in line2:
						print d[key]
