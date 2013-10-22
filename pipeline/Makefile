KHMER=/home/qingpeng/python/khmer
PAPER=/home/qingpeng/Dropbox/Work/Manuscript/2013-diversity

# run this Makefile in ./data directory
# make -f
# diversity paper pipeline
# raw data:

	
all: 220_random_genomes.fna.tar.gz

copydata:
	rm -fr ../data/
	mkdir ../data/
	cp jelly_*_22.hist *.time* ecoli_ref.fastq.pos*.abund1 fp_assessment.out *.wc ../data/


clean:
	rm -fr `cat clean-list.txt`


# generate random genomes

random_genome_220.fna:
	python ${PAPER}/pipeline/simulate_random_genomes.py

220_random_genomes.fna.tar.gz: random_genome_220.fna
	tar -zcvf 220_random_genomes.fna.tar.gz random_genome_*


normalize_overlap_1020: 1A21B.sweep6X.keep.Empirical 1A21C.sweep6X.keep.Empirical 1B21A.sweep6X.keep.Empirical 1B21C.sweep6X.keep.Empirical 1C21A.sweep6X.keep.Empirical 1C21B.sweep6X.keep.Empirical 1A21B.sweep6X.keep.Exact 1A21C.sweep6X.keep.Exact 1B21A.sweep6X.keep.Exact 1B21C.sweep6X.keep.Exact 1C21A.sweep6X.keep.Exact 1C21B.sweep6X.keep.Exact

1A21B.sweep6X.keep.Empirical: sample1A-Empirical-6X.fna.gz.keep sample1B-Empirical-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1A21C.sweep6X.keep.Empirical: sample1A-Empirical-6X.fna.gz.keep sample1C-Empirical-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@
	
1B21A.sweep6X.keep.Empirical: sample1B-Empirical-6X.fna.gz.keep sample1A-Empirical-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1B21C.sweep6X.keep.Empirical: sample1B-Empirical-6X.fna.gz.keep sample1C-Empirical-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1C21A.sweep6X.keep.Empirical: sample1C-Empirical-6X.fna.gz.keep sample1A-Empirical-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1C21B.sweep6X.keep.Empirical: sample1C-Empirical-6X.fna.gz.keep sample1B-Empirical-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1A21B.sweep6X.keep.Exact: sample1A-Exact-6X.fna.gz.keep sample1B-Exact-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1A21C.sweep6X.keep.Exact: sample1A-Exact-6X.fna.gz.keep sample1C-Exact-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@
	
1B21A.sweep6X.keep.Exact: sample1B-Exact-6X.fna.gz.keep sample1A-Exact-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1B21C.sweep6X.keep.Exact: sample1B-Exact-6X.fna.gz.keep sample1C-Exact-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1C21A.sweep6X.keep.Exact: sample1C-Exact-6X.fna.gz.keep sample1A-Exact-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

1C21B.sweep6X.keep.Exact: sample1C-Exact-6X.fna.gz.keep sample1B-Exact-6X.fna.gz.keep
	python ${KHMER}/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 $^ > $@

%.keep: %
	python ${KHMER}/scripts/normalize-by-median.py -C 5 -k 22 -N 4 -x 1e9 $<


saturation_1021: evenness_1-Empirical.fna.gz.C1.report evenness_10-Empirical.fna.gz.C1.report evenness_40-Empirical.fna.gz.C1.report evenness_1_10_40-Empirical.fna.gz.C1.report evenness_5-Empirical.fna.gz.C1.report evenness_20-Empirical.fna.gz.C1.report evenness_1_5_10_20_40-Empirical.fna.gz.C1.report evenness_12345-Empirical.fna.gz.C1.report evenness_124816-Empirical.fna.gz.C1.report
saturation_1021_copy:
	cp evenness_*-Empirical.fna.gz.C1.report ${PAPER}/data/
#1017
evenness_1017: evenness_1-Empirical.fna.gz.hist evenness_10-Empirical.fna.gz.hist evenness_40-Empirical.fna.gz.hist evenness_1_10_40-Empirical.fna.gz.hist evenness_5-Empirical.fna.gz.hist evenness_20-Empirical.fna.gz.hist evenness_1_5_10_20_40-Empirical.fna.gz.hist evenness_12345-Empirical.fna.gz.hist evenness_124816-Empirical.fna.gz.hist

evenness_1-Empirical.fna.gz: ${PAPER}/pipeline/evenness_1.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 12500 --threads 2 -z -s $<
evenness_10-Empirical.fna.gz: ${PAPER}/pipeline/evenness_10.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 125000 --threads 2 -z -s $<
evenness_40-Empirical.fna.gz: ${PAPER}/pipeline/evenness_40.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 500000 --threads 2 -z -s $<
evenness_1_10_40-Empirical.fna.gz: ${PAPER}/pipeline/evenness_1_10_40.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 637500 --threads 2 -z -s $<

evenness_5-Empirical.fna.gz: ${PAPER}/pipeline/evenness_5.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 62500 --threads 2 -z -s $<
evenness_20-Empirical.fna.gz: ${PAPER}/pipeline/evenness_20.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 250000 --threads 2 -z -s $<
evenness_1_5_10_20_40-Empirical.fna.gz: ${PAPER}/pipeline/evenness_1_5_10_20_40.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 950000 --threads 2 -z -s $<
evenness_12345-Empirical.fna.gz: ${PAPER}/pipeline/evenness_12345.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 187500 --threads 2 -z -s $<
evenness_124816-Empirical.fna.gz: ${PAPER}/pipeline/evenness_124816.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 387500 --threads 2 -z -s $<

%.hist: %.ht % 
	python ${KHMER}/sandbox/calc-median-distribution.py $^ $@

%.ht: %
	python ${KHMER}/scripts/load-into-counting.py --ksize 22 --n_hashes 4 --hashsize 1e9 $@ $<

%.C1.report: %
	python ${PAPER}/pipeline/normalize-by-median.py -C 1 -k 22 -N 4 -x 1e9  $<  -R $@
	
	
	
overlap:
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 1250000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleA.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 1250000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleB.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 1250000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleC.mprf
	MetaSim cmd -mg ${PAPER}/pipeline/errormodel-80bp.mconf -r 1250000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleD.mprf

	mv sampleA-Empirical.fna.gz sampleA-Empirical-1X.fna.gz
	mv sampleB-Empirical.fna.gz sampleB-Empirical-1X.fna.gz
	mv sampleC-Empirical.fna.gz sampleC-Empirical-1X.fna.gz
	mv sampleD-Empirical.fna.gz sampleD-Empirical-1X.fna.gz


	~/bin/metasim/MetaSim cmd -mg ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/errormodel-80bp.mconf -r 25000000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleA.mprf
	~/bin/metasim/MetaSim cmd -mg ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/errormodel-80bp.mconf -r 25000000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleB.mprf
	~/bin/metasim/MetaSim cmd -mg ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/errormodel-80bp.mconf -r 25000000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleC.mprf
	~/bin/metasim/MetaSim cmd -mg ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/errormodel-80bp.mconf -r 25000000 --threads 2 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleD.mprf



	~/bin/metasim/MetaSim cmd -r 1250000 -f 80 -t 0 --threads 2 -z -s  ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleA.mprf 
	~/bin/metasim/MetaSim cmd -r 1250000 -f 80 -t 0 --threads 2 -z -s  ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleB.mprf 
	~/bin/metasim/MetaSim cmd -r 1250000 -f 80 -t 0 --threads 2 -z -s  ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleC.mprf 
	~/bin/metasim/MetaSim cmd -r 1250000 -f 80 -t 0 --threads 2 -z -s  ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/sampleD.mprf 
	mv sampleA-Exact.fna.gz sampleA-Exact-1X.fna.gz
	mv sampleB-Exact.fna.gz sampleB-Exact-1X.fna.gz
	mv sampleC-Exact.fna.gz sampleC-Exact-1X.fna.gz
	mv sampleD-Exact.fna.gz sampleD-Exact-1X.fna.gz


	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Empirical-1X.fna.gz sampleB-Empirical-1X.fna.gz >A2B.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Empirical-1X.fna.gz sampleC-Empirical-1X.fna.gz >A2C.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Empirical-1X.fna.gz sampleD-Empirical-1X.fna.gz >A2D.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Empirical-1X.fna.gz sampleA-Empirical-1X.fna.gz >B2A.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Empirical-1X.fna.gz sampleC-Empirical-1X.fna.gz >B2C.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Empirical-1X.fna.gz sampleD-Empirical-1X.fna.gz >B2D.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Empirical-1X.fna.gz sampleA-Empirical-1X.fna.gz >C2A.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Empirical-1X.fna.gz sampleB-Empirical-1X.fna.gz >C2B.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Empirical-1X.fna.gz sampleD-Empirical-1X.fna.gz >C2D.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Empirical-1X.fna.gz sampleA-Empirical-1X.fna.gz >D2A.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Empirical-1X.fna.gz sampleB-Empirical-1X.fna.gz >D2B.sweep1X.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Empirical-1X.fna.gz sampleC-Empirical-1X.fna.gz >D2C.sweep1X.Empirical


	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Empirical.fna.gz sampleB-Empirical.fna.gz >A2B.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Empirical.fna.gz sampleC-Empirical.fna.gz >A2C.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Empirical.fna.gz sampleD-Empirical.fna.gz >A2D.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Empirical.fna.gz sampleA-Empirical.fna.gz >B2A.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Empirical.fna.gz sampleC-Empirical.fna.gz >B2C.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Empirical.fna.gz sampleD-Empirical.fna.gz >B2D.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Empirical.fna.gz sampleA-Empirical.fna.gz >C2A.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Empirical.fna.gz sampleB-Empirical.fna.gz >C2B.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Empirical.fna.gz sampleD-Empirical.fna.gz >C2D.sweep.Empirical

	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Empirical.fna.gz sampleA-Empirical.fna.gz >D2A.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Empirical.fna.gz sampleB-Empirical.fna.gz >D2B.sweep.Empirical
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Empirical.fna.gz sampleC-Empirical.fna.gz >D2C.sweep.Empirical

	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Exact-1X.fna.gz sampleB-Exact-1X.fna.gz >A2B.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Exact-1X.fna.gz sampleC-Exact-1X.fna.gz >A2C.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Exact-1X.fna.gz sampleD-Exact-1X.fna.gz >A2D.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Exact-1X.fna.gz sampleA-Exact-1X.fna.gz >B2A.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Exact-1X.fna.gz sampleC-Exact-1X.fna.gz >B2C.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Exact-1X.fna.gz sampleD-Exact-1X.fna.gz >B2D.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Exact-1X.fna.gz sampleA-Exact-1X.fna.gz >C2A.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Exact-1X.fna.gz sampleB-Exact-1X.fna.gz >C2B.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Exact-1X.fna.gz sampleD-Exact-1X.fna.gz >C2D.sweep1X

	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Exact-1X.fna.gz sampleA-Exact-1X.fna.gz >D2A.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Exact-1X.fna.gz sampleB-Exact-1X.fna.gz >D2B.sweep1X
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Exact-1X.fna.gz sampleC-Exact-1X.fna.gz >D2C.sweep1X




	 ~/bin/metasim/MetaSim cmd -r 25000000 -f 80 -t 0 --threads 4 -z -s ~/Dropbox/Work/Manuscript/2013-diversity/pipeline/SampleD.mprf &
 
 
	# 20X no error
	#python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Exact.fna.gz sampleB-Exact.fna.gz >A2B.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Exact.fna.gz sampleC-Exact.fna.gz >A2C.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleA-Exact.fna.gz sampleD-Exact.fna.gz >A2D.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Exact.fna.gz sampleA-Exact.fna.gz >B2A.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Exact.fna.gz sampleC-Exact.fna.gz >B2C.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleB-Exact.fna.gz sampleD-Exact.fna.gz >B2D.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Exact.fna.gz sampleA-Exact.fna.gz >C2A.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Exact.fna.gz sampleB-Exact.fna.gz >C2B.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleC-Exact.fna.gz sampleD-Exact.fna.gz >C2D.sweep

	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Exact.fna.gz sampleA-Exact.fna.gz >D2A.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Exact.fna.gz sampleB-Exact.fna.gz >D2B.sweep
	python ~/python/khmer/sandbox/sweep-reads2.py --ksize 22 --n_hashes 4 --hashsize 4e10 sampleD-Exact.fna.gz sampleC-Exact.fna.gz >D2C.sweep


 
 
 