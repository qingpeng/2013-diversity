
import sys

file_ht = open(sys.argv[1],'r')
file_gz = open(sys.argv[2],'r')

hts = {}
for line in file_ht:
    line = line.rstrip()
    fields = line.split()
    hts[fields[0]] = fields[1]

gzs =[] 
for line in file_gz:
    line = line.rstrip()
    gzs.append(line)

for ht in hts.keys():
    ht_size = hts[ht]
    for gz in gzs:
        outputfile = gz.split('.')[0] + '-in-'+ ht.split('.')[0]+'.out'
        qsubfile = gz.split('.')[0] + '-in-'+ ht.split('.')[0]+'.qsub'
        f_qsub = open(qsubfile,'w')
        f_qsub.write("#!/bin/bash -login\n")
        line = "#PBS -l walltime=150:00:00,nodes=01:ppn=1,mem="+ht_size
        f_qsub.write(line)
        lines = '''
#PBS -q main
#PBS -M qingpeng@gmail.com
#PBS -m abe
#PBS -A ged-intel11

module load khmer/1.0.1-rc2
module load screed
cd $PBS_O_WORKDIR
'''
        f_qsub.write(lines)
        line = "python /opt/software/khmer/1.0.1-rc2--GCC-4.4.5/scripts/count-median.py "\
        + ht + ' ' + gz + ' ' + outputfile 
        f_qsub.write(line)
        f_qsub.close()
        
