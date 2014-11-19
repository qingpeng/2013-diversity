# fd3ffcee540d014600741739fb94d1c3  SRS011111.tar.bz2
# baf6f351e97a1833f8f028f70b3d880b  SRS011132.tar.bz2
# 466f35f89ae84868723d31d0526b2b2d  SRS011134.tar.bz2
# a21c0073aa1854809d300384f41d66a1  SRS011140.tar.bz2
# ae781cf1419a6b9b87db3c711b0307f7  SRS011144.tar.bz2
# 9e7a7859630c34cfa8ad89940840b0e8  SRS011152.tar.bz2
# b1d24e5ad94e322e13155563ad981d80  SRS011239.tar.bz2
# 92a054f8923a941b5036a2fda63a9c88  SRS011243.tar.bz2
# 5c0d047f2a97761c8b9d934f2a455d26  SRS011247.tar.bz2
# 
# 
# 6d9e2ffc82b08ef37551e902096e4c98  ./anterior_nares/SRS049744.tar.bz2
# 6b8ace391b7797a97fc6b04bb949fdbf  ./anterior_nares/SRS053437.tar.bz2
# ceefbd37f300e4dc492a0bdde2011284  ./anterior_nares/SRS022006.tar.bz2
# ce202d8eba5a31a53d2e343c4edb8df7  ./anterior_nares/SRS022645.tar.bz2
# 12775f5df6e71961f1c544e84f6c7342  ./anterior_nares/SRS012291.tar.bz2
# 552427d1ac2cdbe5202a8b5547f5b4f1  ./anterior_nares/SRS024424.tar.bz2
# 701ecd9a9a85ca02fdc0041c49aadfce  ./anterior_nares/SRS019986.tar.bz2
# bbb25b41df1a88f748789d94eebc2f3a  ./anterior_nares/SRS051613.tar.bz2
# 7d0b7d4e22778141c9bd149e844efc4e  ./anterior_nares/SRS014901.tar.bz2
# 26da99039a85dd19c1c77996da7bd0f7  ./anterior_nares/SRS017156.tar.bz2
# 7a56000f9a9306745066f5a2e16f4c3c  ./anterior_nares/SRS015269.tar.bz2
# 48b72a38332af46183472346c8cf4586  ./anterior_nares/SRS015793.tar.bz2
# 97e0a29281ea9bba1d7d1984f3dae191  ./anterior_nares/SRS020868.tar.bz2
# 7cca5dd5cd1190a80d1e9bed25bdad4d  ./anterior_nares/SRS020232.tar.bz2

file_local = open("md5.log",'r')
file_full = open("md5sum.txt",'r')

md5 = {}
sample = {}

for line in file_full:
    line = line.strip()
    fields = line.split()
    #print fields
    file_name = fields[1].split("/")[-1]
    md5[file_name] = fields[0]
    sample[file_name] = fields[1].split("/")[-2]

for line in file_local:
    line = line.strip()
    fields = line.split()
    if fields[0] == md5[fields[1]]:
        print fields[1], sample[fields[1]]

