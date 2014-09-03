# "SRS ID","Body Site","Assembly file location","Assembly MD5","Assembly File Size","Reads file location","Reads MD5","Reads File Size"
# "SRS057182","buccal_mucosa","","","","/data/Illumina/buccal_mucosa/SRS057182.tar.bz2","24d0bfe2421f3918ca64d4bdae33551f","374073717"
# "SRS013258","left_retroauricular_crease","/data/HMASM/PGAs/left_retroauricular_crease/SRS013258.scaffolds.fa.bz2","6e1622acbe89ed9bbc422441468eeefe","3092776","/data/Illumina/left_retroauricular_crease/SRS013258.tar.bz2","a56827ec36c7f7273f7219d4d54a196a","1550446872"
# "SRS015072","mid_vagina","/data/HMASM/PGAs/mid_vagina/SRS015072.scaffolds.fa.bz2","2fc7d2c323c7778b8b3fa2ed137cca83","1056986","/data/Illumina/mid_vagina/SRS015072.tar.bz2","039f08ba2b6405d8d441a25a73816f06","70285643"

file_in_obj = open('HMASM.csv','r')
file_out_obj = open('download_HMASM.csv.sh','w')

file_in_obj.readline()

for line in file_in_obj:
    line = line.rstrip()
    fields = line.split(',')
    url = "http://downloads.hmpdacc.org"+ fields[-3][1:-1]
    command = "curl -O "+url+'\n'
    file_out_obj.write(command)
    
