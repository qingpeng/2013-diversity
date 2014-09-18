# O2.UC-11.trimmed.fa.gz
# O2.UC-12.trimmed.fa.gz
# O2.UC-13.trimmed.fa.gz
# O2.UC-14.trimmed.fa.gz
# O2.UC-16.trimmed.fa.gz
# O2.UC-17.trimmed.fa.gz
# O2.UC-18.trimmed.fa.gz
# O2.UC-19.trimmed.fa.gz
# O2.UC-1.trimmed.fa.gz
# O2.UC-20.trimmed.fa.gz
# O2.UC-21.trimmed.fa.gz
# O2.UC-22.trimmed.fa.gz
# O2.UC-23.trimmed.fa.gz
# O2.UC-24.trimmed.fa.gz
# O2.UC-4.trimmed.fa.gz
# V1.CD-11.trimmed.fa.gz
# V1.CD-12.trimmed.fa.gz


file_list_obj =open("gz.list",'r')

for line in file_list_obj:
    line = line.rstrip()
    prefix = line.split(".trimmed")[0]
    to_print = "ls "+prefix+"-in-*.out >"+prefix+"_out.list"
    print to_print
