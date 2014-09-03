alpha diversity of simulated ecoli reads dataset
============

1. get simulated reads

- 50X and 150X
- 1%, 2% and 0% error rate

git clone https://github.com/ctb/dbg-graph-null.git

e.coli_reference.fa from 2013-khmer-counting repo

python dbg-graph-null/make-reads.py -C 150 ~/Dropbox/Manuscript/2013-diversity/pipeline/e.coli_reference.fa  >e.coli_150x_0.01e_100.fa
python dbg-graph-null/make-reads.py -C 50 ~/Dropbox/Manuscript/2013-diversity/pipeline/e.coli_reference.fa  >e.coli_50x_0.01e_100.fa
python dbg-graph-null/make-reads.py -e 0.00 -C 50 ~/Dropbox/Manuscript/2013-diversity/pipeline/e.coli_reference.fa  >e.coli_50x_0.00e_100.fa
python dbg-graph-null/make-reads.py -e 0.02 -C 50 ~/Dropbox/Manuscript/2013-diversity/pipeline/e.coli_reference.fa  >e.coli_50x_0.02e_100.fa

2. create graph file

print_load_sh.sh:
for i in *.fa; do echo load-into-counting.py -x 1e8 -k 20 $i.kh $i \&;  done

bash print_load_sh.sh  >load-into-counting.sh
bash load-into-counting.sh

3. generate config.txt for counting reads coverage spectrum

[qingpeng@dev-intel14 Ecoli_Alpha]$ more config.txt 
e.coli_150x_0.01e_100.fa.kh  e.coli_50x_0.00e_100.fa.kh  e.coli_50x_0.01e_100.fa.kh  e.coli_50x_0.02e_100.fa.kh
e.coli_150x_0.01e_100.fa  e.coli_50x_0.00e_100.fa  e.coli_50x_0.01e_100.fa  e.coli_50x_0.02e_100.fa
10000000000

4. count reads coverage spectrum across species for each reads file(get .comb)

python ~/Dropbox/Manuscript/2013-diversity/scripts/get_comb_multi.py config.txt &

5. get .comb list file and get spectrum frequency across samples

ls *.comb >comb.list
python ~/Dropbox/Manuscript/2013-diversity/scripts/count_spectrum_freq_multiple_files.py comb.list e.coli.spectrum

6. generate MAP file (prepare for QIIME run) (also used in seperate_IGS.py)

#SampleID	BarcodeSequence	LinkerPrimerSequence	Description coverage  error_rate  file_name
sampleA	A	A	e.coli_150x_0.01e_100 150x  0.01  e.coli_150x_0.01e_100.fa.comb
sampleB	A	A	e.coli_50x_0.00e_100  50x 0.00  e.coli_50x_0.00e_100.fa.comb
sampleC	A	A	e.coli_50x_0.01e_100  50x 0.01  e.coli_50x_0.01e_100.fa.comb
sampleD A A e.coli_50x_0.02e_100  50x 0.02  e.coli_50x_0.02e_100.fa.comb

7. get .IGS and .IGS_abund files from *.spectrum file, listing all the IGSs and get the IGS-abundance matrix

python ~/Dropbox/Manuscript/2013-diversity/scripts/seperate_IGS.py e.coli.spectrum e.coli_Map.txt 


8. convert .IGS file to .biom format

module load QIIME/1.7.0
biom convert -i e.coli.spectrum.IGS -o e.coli.spectrum.IGS.biom --table-type="OTU table"

9. get summary from .biom file

biom summarize-table -i  e.coli.spectrum.IGS.biom -o e.coli.spectrum.IGS.biom.summary.txt

[qingpeng@dev-intel14 Ecoli_Alpha]$ more e.coli.spectrum.IGS.biom.summary.txt
Num samples: 4
Num observations: 260333
Total count: 2105023
Table density (fraction of non-zero values): 0.408
Table md5 (unzipped): 6b71f7e4f1d3957fb47f669a0231de6f

Counts/sample summary:
 Min: 310594.0
 Max: 1016129.0
 Median: 389150.000
 Mean: 526255.750
 Std. dev.: 287829.236
 Sample Metadata Categories: None provided
 Observation Metadata Categories: None provided

Counts/sample detail:
 sampleB: 310594.0
 sampleC: 328731.0
 sampleD: 449569.0
 sampleA: 1016129.0
 
 
 10. decide min max step for saturation curve, run .qsub with QIIME scripts

qsub ~/Dropbox/Manuscript/2013-diversity/pipeline/e_coli_alpha_diversity.qsub
 
 
 
 new method
 ------
 
 From step 7:
 
 treat IGSs in different seperately
 
 7. 
python ~/Dropbox/Manuscript/2013-diversity/scripts/seperate_IGS_for_alpha.py e.coli.spectrum e.coli_Map.txt

8. 
biom convert -i e.coli.spectrum.IGS.alpha -o e.coli.spectrum.IGS.alpha.biom --table-type="OTU table"

9.
biom summarize-table -i e.coli.spectrum.IGS.alpha.biom -o e.coli.spectrum.IGS.alpha.biom.summary.txt
10.

qsub ~/Dropbox/Manuscript/2013-diversity/pipeline/e_coli_alpha_diversity_for_alpha_biom.qsub

 
file:///Users/qingpeng/Google%20Drive/Dropbox/Manuscript/2013-diversity/Data/rare_plot_alpha/rarefaction_plots.html



beginning of curve:

/mnt/home/qingpeng/Manuscript/2013-diversity/data/Ecoli_Alpha/Begin_curve



