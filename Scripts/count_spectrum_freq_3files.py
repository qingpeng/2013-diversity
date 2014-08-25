
#40 35 0
#35 37 0
#39 38 0
#38 44 0
#32 38 0
#2 0 0



import sys


def read_file(file_in,x,y,z):
    file_in_obj = open(file_in, 'r')
    count = {}
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
        
    return count,x,y,z
    
    
        
file_in1 = sys.argv[1]
file_in2 = sys.argv[2]
file_in3 = sys.argv[3]
file_out = sys.argv[4]

file_out_obj = open(file_out,'w')


x = set()
y = set()
z = set()

count1,x,y,z = read_file(file_in1,x,y,z)
count2,x,y,z = read_file(file_in2,x,y,z)
count3,x,y,z = read_file(file_in3,x,y,z)


for a in range(max(x)):
    for b in range(max(y)):
        for c in range(max(z)):
            key = str(a) + '-' + str(b) + '-' + str(c)
            if key not in count1:
                fre1 = 0
            else:
                fre1 = count1[key]
                
                
            if key not in count2:
                fre2 = 0
            else:
                fre2 = count2[key]
                
            if key not in count3:
                fre3 = 0
            else:
                fre3 = count3[key]
                
                
            if fre1 !=0 or fre2 != 0 or fre3 != 0:
              file_out_obj.write(key+' '+str(fre1)+' '+ str(fre2) + ' ' +str(fre3)+'\n')
            
            
            
            
            
            
            
            
            

