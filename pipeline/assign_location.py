# -rw-r--r-- 1 qingpeng tg  12M Oct 26 21:57 all_SRS013269.fa.gz
# -rw-r--r-- 1 qingpeng tg  12M Oct 26 22:36 all_SRS044626.fa.gz
# -rw-r--r-- 1 qingpeng tg  11M Oct 26 22:35 all_SRS044742.fa.gz
# -rw-r--r-- 1 qingpeng tg  11M Oct 26 22:15 all_SRS019339.fa.gz
# -rw-r--r-- 1 qingpeng tg  10M Oct 26 21:59 all_SRS013956.fa.gz
# -rw-r--r-- 1 qingpeng tg 8.9M Oct 26 22:48 all_SRS051600.fa.gz
# -rw-r--r-- 1 qingpeng tg 8.0M Oct 26 23:05 all_SRS063417.fa.gz
# -rw-r--r-- 1 qingpeng tg 7.0M Oct 26 22:08 all_SRS018312.fa.gz
# -rw-r--r-- 1 qingpeng tg 7.0M Oct 26 22:57 all_SRS056210.fa.gz
# -rw-r--r-- 1 qingpeng tg 6.0M Oct 26 22:31 all_SRS022545.fa.gz
# -rw-r--r-- 1 qingpeng tg 5.8M Oct 26 23:19 all_SRS065179.fa.gz
# -rw-r--r-- 1 qingpeng tg 5.5M Oct 26 23:17 all_SRS065142.fa.gz
# -rw-r--r-- 1 qingpeng tg 4.4M Oct 26 22:14 all_SRS019215.fa.gz
# 
# SRS013261.tar.bz2 right_retroauricular_crease
# SRS013269.tar.bz2 anterior_nares
# SRS013521.tar.bz2 stool
# SRS013687.tar.bz2 stool
# SRS013800.tar.bz2 stool


file_down = open("full_download.txt",'r')
location = {}
for line in file_down:
    line = line.rstrip()
    fields = line.split()
    location[fields[0]] = fields[1]

file_ls = open("ls_gz.log",'r')

for line in file_ls:
    line = line.rstrip()
    fields = line.split()
    SR = fields[-1].split('.')[0].split('_')[1]
    print line, location[SR+'.tar.bz2']

