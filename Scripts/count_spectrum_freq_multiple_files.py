
#40 35 0
#35 37 0
#39 38 0
#38 44 0
#32 38 0
#2 0 0

#JCVI_READ_1095899380104 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 0


import sys



str_sets = set()

def read_file(file_in,str_set):
    file_in_obj = open(file_in, 'r')
    count = {}
    for line in file_in_obj:
        
        line = line.rstrip()
        fields = line.split()

        key = '-'.join(fields[1:])
        
        
        str_set.add(key)
        
        if key in count:
            count[key] = count[key] + 1
        else:
            count[key] = 1
        
    return count,str_set
    
    
        
file_list = sys.argv[1]
file_out = sys.argv[2]

file_list_obj = open(file_list,'r')

file_out_obj = open(file_out,'w')


count_list = []
n = 0
for line in file_list_obj:
    line = line.rstrip()
    count, str_sets = read_file(line, str_sets)
    print line+' done!'
    count_list.append(count)
    n = n+1

sorted_str = sorted(list(str_sets))
#print sorted_str

for spetr in sorted_str:
    to_print = spetr 
    for i in range(n):
        if spetr not in count_list[i]:
            fre = 0
        else:
            fre = count_list[i][spetr]
            
        to_print = to_print + ' ' + str(fre)

    file_out_obj.write(to_print+'\n')


            
            
            
            
            
            
            

