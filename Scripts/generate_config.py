# [qingpeng@dev-gfx10 Error_Correction]$ head fa.list
# O2.UC-11.trimmed.fa
# O2.UC-12.trimmed.fa
# O2.UC-13.trimmed.fa
# O2.UC-14.trimmed.fa
# O2.UC-16.trimmed.fa
# O2.UC-17.trimmed.fa
# O2.UC-18.trimmed.fa
# 
# [qingpeng@dev-gfx10 Error_Correction]$ head ht.list
# O2.UC-11.trimmed.fa.clippered.corr.ht
# O2.UC-12.trimmed.fa.clippered.corr.ht
# O2.UC-13.trimmed.fa.clippered.corr.ht
# O2.UC-14.trimmed.fa.clippered.corr.ht
# O2.UC-16.trimmed.fa.clippered.corr.ht
# O2.UC-17.trimmed.fa.clippered.corr.ht

import sys
file_fa_obj = sys.argv[1]
file_ht_obj = sys.argv[2]
memory = sys.argv[3]

ht_string = ''
for line in file_ht_obj:
    line = line.rstrip()
    ht_string = ht_string+' '+line

for line in file_fa_obj:
    line = line.rstrip()
    file_config = open(line+'.config','w')
    file_config.write(ht_string+'\n')
    file_config.write(line+'\n')
    file_config.write(memory+'\n')
    


