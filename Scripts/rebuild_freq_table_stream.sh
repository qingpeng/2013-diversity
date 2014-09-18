#!/bin/sh



for f in *_out.list
do
    printf 'qsub -v seq_file="'$f'" /mnt/home/qingpeng/Dropbox/Manuscript/2013-diversity/scripts/rebuild_freq_table_stream.qsub\n'
    qsub -v list_file="$f" /mnt/home/qingpeng/Dropbox/Manuscript/2013-diversity/scripts/rebuild_freq_table_stream.qsub
done
