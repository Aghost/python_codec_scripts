import sys
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')
import codecs

src_path = IN[0]
dst_path = IN[1]

with codecs.open(src_path, 'r', encoding = 'UTF-16') as file:
	lines = file.read()  

#write output file
with codecs.open(dst_path, 'w', encoding = 'latin-1') as file:
	file.write(lines)

OUT = 0