
#40 35 0
#35 37 0
#39 38 0
#38 44 0
#32 38 0
#2 0 0



import sys

file_in = sys.argv[1]
file_out = sys.argv[2]

file_in_obj = open(file_in, 'r')
file_out_obj = open(file_out,'w')
count = {}
x = set()
y = set()
z = set()


for line in file_in_obj:

    line = line.rstrip()
    fields = line.split()
    x.add(int(fields[0]))
    y.add(int(fields[0]))
    z.add(int(fields[0]))
    
    key = fields[0] + '-' + fields[1] + '-' + fields[2]
    if key in count:
        count[key] = count[key] + 1
    else:
        count[key] = 1
        
for a in range(max(x)):
    for b in range(max(y)):
        for c in range(max(z)):
            key = str(a) + '-' + str(b) + '-' + str(c)
            if key not in count:
                fre = 0
            else:
                fre = count[key]
            if fre !=0:
              file_out_obj.write(key+' '+str(fre)+'\n')
            
            
            
            
            
            
            
            
            

