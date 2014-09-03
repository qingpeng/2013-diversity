# 
# 0-0-10 0 0 521
# 0-0-11 0 0 230
# 0-0-12 0 0 80
# 0-0-13 0 0 31
# 0-0-14 0 0 19
# 0-0-15 0 0 41
# 0-0-16 0 0 50
# 0-0-17 0 0 72
# 0-0-18 0 0 155
# 0-0-19 0 0 237
# 0-0-20 0 0 427
# 0-0-21 0 0 640
# 0-0-22 0 0 789
# 0-0-23 0 0 1150
# 0-0-24 0 0 1340
# 0-0-25 0 0 1579

# discard spectrum as 1-0-0 or 0-1-0, and adjust he spectrum by *2.
# 
import sys

file_in = sys.argv[1]
file_out1 = sys.argv[2]
file_out2 = sys.argv[3]


file_in_o = open(file_in,'r')
file_out1_o = open(file_out1,'w')
file_out2_o = open(file_out2,'w')

IGS_count = 0

for line in file_in_o:
    line = line.rstrip()
    f1 = line.split()
    f2 = f1[0].split('-')
    sum_count = 0
    for freq in f1[1:]:
        sum_count = sum_count + int(freq)

    sum_spectr = 0
    for freq in f2:
        sum_spectr = sum_spectr + int(freq)
        
    if sum_spectr>1:
    
        IGS_abundance =  sum_count/float(sum_spectr)/2
        file_out1_o.write(f1[0]+' '+str(IGS_abundance) + '\n')
        if int(IGS_abundance)>=1:
            for i in range(int(IGS_abundance)):
                IGS_count += 1
                new_spectr = '\t'.join(f2)
                file_out2_o.write(str(IGS_count)+'\t'+new_spectr+'\n')
            


        