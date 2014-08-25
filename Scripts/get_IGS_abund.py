# 29-15 2 25
# 29-15 3 20
# 29-15 4 18
# 29-15 5 2
# 29-16 0 18
# 29-16 1 19
# 29-16 2 43
# 29-16 3 61
# 29-16 4 37
# 29-16 5 13
# 29-16 6 11
# 29-16 7 1
# 29-17 0 63
# 29-17 1 42
# 29-17 2 99
# 29-17 3 90
# 29-17 4 40
# 29-17 5 27
# 29-17 6 13
# 29-17 7 10
# 29-17 8 2

import sys

file_in = sys.argv[1]
file_out = sys.argv[2]

file_in_o = open(file_in,'r')
file_out_o = open(file_out,'w')

def get_flag(string):
	if string == '0':
		return "-"
	else:
		return "+"
count = {}
all_count = {}
for line in file_in_o:
    line = line.rstrip()
    f1 = line.split()
    f2 = f1[0].split('-')
    if int(f2[0])+int(f2[1])+int(f1[1])>1:

    	number = float(f1[2])/(int(f2[0])+int(f2[1])+int(f1[1]))

	flag = get_flag(f2[0])+get_flag(f2[1])+get_flag(f1[1])
	if flag in count:
		count[flag] += number
	else:
		count[flag] = number 
	if flag in all_count:
		all_count[flag] += int(f1[2])
	else:
		all_count[flag] = int(f1[2])

    	out_string = f2[0]+' '+f2[1]+' '+ f1[1]+' '+ str(number)
    	if number >0:
        	file_out_o.write(out_string+'\n')


for key in count:
	file_out_o.write(key+' '+str(count[key])+'\n')

for key in all_count:
        file_out_o.write(key+' '+str(all_count[key])+'\n')
 
