import sys

file_name_list = sys.argv[1]

f_list = open(file_name_list,'r')
f_output = open(file_name_list+'.freq_table','w')

f_handle_list = []
for line in f_list:
    line = line.rstrip()
    f_handle = open(line,'r')
    f_handle_list.append(f_handle)

for line_1 in f_handle_list[0]:

        to_write = line_1.rstrip()

        for f_handle in f_handle_list[1:]:
            to_write = to_write+' '+f_handle.readline().rstrip().split()[1]
    
        f_output.write(to_write+'\n')


    

    
