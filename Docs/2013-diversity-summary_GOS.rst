
beta diversity analysis - GOS data set
======================================

1. get GOS data set
-------------------

2. create graph files
---------------------

run\_load.qsub: (qsub to run load-into-counting.py)

::

    [qingpeng@dev-intel14 GOS_Data]$ more run_load.qsub
    #!/bin/bash -login
    #PBS -l walltime=10:00:00,nodes=1:ppn=1,mem=3g
    #PBS -q main
    #PBS -M qingpeng@gmail.com
    #PBS -m abe
    #PBS -A ged-intel11

    module load khmer
    module load screed

    cd $PBS_O_WORKDIR
    python /mnt/home/qingpeng/bin/khmer/scripts/load-into-counting.py --ksize 20 --n_hashes 4 --hashsize 500000000 $htfile $seqfile

write\_qsub.py: (generate .sh file to submit run\_load.qsub jobs, a
sample.list file is required.)

::

    [qingpeng@dev-intel14 GOS_Data]$ more write_qsub.py
    filein = open('sample.list','r')

    #qsub -v htfile="GS000a.fa.ht",seqfile="GS000a.fa" run_load.qsub

    for line in filein:
      line = line.rstrip()
      to_print = "qsub -v htfile=\"GS0"+line+".fa.ht\",seqfile=\"GS0"+line+".fa\" run_load.qsub"
      print to_print

sample.list:

::

    [qingpeng@dev-intel14 GOS_Data]$ more sample.list
    00a
    00b
    00c
    00d
    01a
    01b
    01c
    02
    03
    04
    05
    06
    07
    08
    09
    10
    11

all\_load\_qsub.sh

::

    [qingpeng@dev-intel14 GOS_Data]$ more all_load_qsub.sh
    qsub -v htfile="GS000a.fa.ht",seqfile="GS000a.fa" run_load.qsub
    qsub -v htfile="GS000b.fa.ht",seqfile="GS000b.fa" run_load.qsub
    qsub -v htfile="GS000c.fa.ht",seqfile="GS000c.fa" run_load.qsub
    qsub -v htfile="GS000d.fa.ht",seqfile="GS000d.fa" run_load.qsub
    qsub -v htfile="GS001a.fa.ht",seqfile="GS001a.fa" run_load.qsub
    qsub -v htfile="GS001b.fa.ht",seqfile="GS001b.fa" run_load.qsub
    qsub -v htfile="GS001c.fa.ht",seqfile="GS001c.fa" run_load.qsub

3 generate config.txt for counting reads coverage spectrum
----------------------------------------------------------

write\_config.py ( to generate config.txt):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    [qingpeng@dev-intel14 GOS_Data]$ more write_config.py
    filein = open('sample.list','r')

    #qsub -v htfile="GS000a.fa.ht",seqfile="GS000a.fa" run_load.qsub

    for line in filein:
      line = line.rstrip()
      print "GS0"+line+".fa.ht ",
    print "\n"

    filein = open('sample.list','r')

    #qsub -v htfile="GS000a.fa.ht",seqfile="GS000a.fa" run_load.qsub

    for line in filein:
      line = line.rstrip()
      print "GS0"+line+".fa ",
    print "\n"

config-GOS.txt
^^^^^^^^^^^^^^

::

    [qingpeng@dev-intel14 GOS_Data]$ more config-GOS.txt
    GS000a.fa.ht  GS000b.fa.ht  GS000c.fa.ht  GS000d.fa.ht  GS001a.fa.ht  GS001b.fa.ht  GS001c.fa.ht  GS002.fa.ht  GS003.fa.ht  GS004.fa.ht
     GS005.fa.ht  GS006.fa.ht  GS007.fa.ht  GS008.fa.ht  GS009.fa.ht  GS010.fa.ht  GS011.fa.ht  GS012.fa.ht  GS013.fa.ht  GS014.fa.ht  GS015
    .fa.ht  GS016.fa.ht  GS017.fa.ht  GS018.fa.ht  GS019.fa.ht  GS020.fa.ht  GS021.fa.ht  GS022.fa.ht  GS023.fa.ht  GS025.fa.ht  GS026.fa.ht
      GS027.fa.ht  GS028.fa.ht  GS029.fa.ht  GS030.fa.ht  GS031.fa.ht  GS032.fa.ht  GS033.fa.ht  GS034.fa.ht  GS035.fa.ht  GS036.fa.ht  GS03
    7.fa.ht  GS047.fa.ht  GS051.fa.ht
    GS000a.fa  GS000b.fa  GS000c.fa  GS000d.fa  GS001a.fa  GS001b.fa  GS001c.fa  GS002.fa  GS003.fa  GS004.fa  GS005.fa  GS006.fa  GS007.fa
     GS008.fa  GS009.fa  GS010.fa  GS011.fa  GS012.fa  GS013.fa  GS014.fa  GS015.fa  GS016.fa  GS017.fa  GS018.fa  GS019.fa  GS020.fa  GS021
    .fa  GS022.fa  GS023.fa  GS025.fa  GS026.fa  GS027.fa  GS028.fa  GS029.fa  GS030.fa  GS031.fa  GS032.fa  GS033.fa  GS034.fa  GS035.fa  G
    S036.fa  GS037.fa  GS047.fa  GS051.fa
    100000000000

4. count reads coverage spectrum across species for each reads file(get .comb)
------------------------------------------------------------------------------

get\_comb\_multi.qsub:
^^^^^^^^^^^^^^^^^^^^^^

::

    #!/bin/bash -login
    #PBS -l walltime=20:00:00,nodes=01:ppn=4,mem=110gb
    #PBS -q main
    #PBS -M qingpeng@gmail.com
    #PBS -m abe
    #PBS -A ged-intel11

    module load khmer
    module load screed
    cd $PBS_O_WORKDIR
    python get_comb_multi.py config-GOS.txt

GS000a.fa.comb
~~~~~~~~~~~~~~

::

    JCVI_READ_838489 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    JCVI_READ_839879 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    JCVI_READ_839881 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    JCVI_READ_839880 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    JCVI_READ_839883 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    JCVI_READ_840623 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0
    JCVI_READ_840621 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    JCVI_READ_840620 0 2 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0

5.1 Get distance matrix ( method 1: use number of reads that are covered in another sample, similar to Compareads.)
-------------------------------------------------------------------------------------------------------------------

::

    python get_distance.py
    cp distance.txt GOS_distance.txt

5.2 Using IGS-based method to get distance matrix
-------------------------------------------------

5.2.1 get .comb list file and get spectrum frequency across samples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    ls *.comb >comb.list
    python ~/Dropbox/Manuscript/2013-diversity/scripts/count_spectrum_freq_multiple_files.py comb.list GOS.freq 

GOS.freq
~~~~~~~~

::

    8-3-0-7-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-0-6-4-8-8-12-0-0-3-4-8-9-1-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-0-7-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-0-6-4-8-8-12-0-0-4-5-8-9-1-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-0-7-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-1-5-4-7-8-11-0-0-3-4-8-9-1-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-0-7-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-1-5-4-8-9-12-0-0-3-5-8-10-0-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-0-7-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-1-6-4-8-8-12-0-0-3-4-8-9-1-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0
    8-3-0-7-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-1-6-4-8-8-12-0-0-4-4-8-9-0-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-0-7-0-2-0-0-0-0-0-0-0-0-0-0-0-0-0-1-5-4-7-8-11-0-0-3-3-8-9-1-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-0-8-0-1-0-0-0-0-0-0-0-0-0-0-0-0-0-0-5-4-8-9-12-0-0-3-5-8-10-0-0-0-2-0-0-0-0-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-1-11-2-2-1-0-0-0-0-0-0-0-0-0-0-0-0-1-14-4-12-7-7-0-0-6-9-6-7-1-0-0-0-0-0-0-1-0-0-0-0-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
    8-3-1-17-0-2-0-0-0-0-0-0-0-0-0-0-0-0-0-1-7-9-16-6-11-0-1-3-9-5-6-3-1-1-0-0-0-0-3-0-0-1-3-0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

5.2.1 get .IGS and .IGS\_abund files from \*.freq file, listing all the IGSs and get the IGS-abundance matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    python ~/Dropbox/Manuscript/2013-diversity/scripts/seperate_IGS.py GOS.freq GOS_Map.txt 

Count the number of IGSs with that spectrum of coverage across samples (.IGS\_abund file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For many "coverage spectrum", the number of "normalized" IGSs is smaller
than 1. In the next step, we just discard those rare IGSs.

GOS.freq.IGS\_abund
'''''''''''''''''''

::

    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-0-0-5 0.142857142857
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-0-1-0 27.0
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-0-1-1 0.25
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-0-2-0 3.25
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-1-0-0 17.3333333333
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-1-1-0 0.5
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-2-0-0 11.5
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-2-1-0 0.6
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-3-1-0 0.5
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-4-0-0 0.333333333333
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-0-4-1-0 0.142857142857
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-0-0-0 242.666666667
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-0-0-1 11.25
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-0-0-2 1.8
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-0-0-3 0.333333333333
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-0-0-5 0.125
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-0-1-0 0.5
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-1-0-0 0.25
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-1-1-0 0.4
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-2-0-0 0.4
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-1-4-0-0 0.142857142857
    0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-2-0-2-0-0-0 30.5

List the IGSs and abundance in samples (IGS-table) (\*.IGS file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

GOS.freq.IGS
''''''''''''

::

    4203559 9       0       1       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203560 9       0       1       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203561 9       0       1       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203562 9       0       1       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203563 9       0       2       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203564 9       0       2       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203565 9       0       2       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203566 9       0       2       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203567 9       1       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0
    4203568 9       1       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0       0

5.2.3 Get the similarity matrix. (Here we use braycurtis metric.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    python /mnt/home/qingpeng/Dropbox/Manuscript/2013-diversity/scripts/get_distance_matrix_v2.py GOS.freq.IGS comb.list matrix.out

get\_dm.qsub
''''''''''''

::

    qingpeng@dev-intel14 0824]$ more get_dm.qsub
    #!/bin/bash -login
    #PBS -l walltime=20:00:00,nodes=1:ppn=1,mem=10g
    #PBS -q main
    #PBS -M qingpeng@gmail.com
    #PBS -m abe
    #PBS -A ged-intel11

    module load NumPy/1.8.1
    module load matplotlib/1.1.0
    module load SciPy/0.13.0
    module h5py/2.1.3
    source /mnt/home/qingpeng/env/bin/activate

    cd $PBS_O_WORKDIR
    python /mnt/home/qingpeng/Dropbox/Manuscript/2013-diversity/scripts/get_distance_matrix_v2.py GOS.freq.IGS comb.list matrix.out

matrix.out is the distance matrix

6. Do clustering using distance matrix
--------------------------------------

See other notebook

7. GOS alpha diversity
----------------------

