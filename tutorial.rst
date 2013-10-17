=======================================
Running the diversity paper script pipeline
=======================================

:Date: June 20, 2013

 
Installing necessary software
-----------------------------

Before we get started, we need to install all the necessary software, including:

 - MetaSim


wget http://ab.inf.uni-tuebingen.de/data/software/metasim/download/V0_9_5/MetaSim_unix_0_9_5.sh
bash MetaSim_unix_0_9_5.sh -c

./bin/MetaSim



echo 'export PATH=$PATH:/home/qingpeng/bin/metasim/' >> ~/.bashrc
source ~/.bashrc
 
 
================




Before we get started, we need to install all the necessary software, including:

 - Tallymer
 - Jellyfish
 - DSK
 - ipython
 - LaTex
 - Velvet

To do so, run::

 cd /mnt/2013-khmer-counting/pipeline
 bash software_install.sh

.. @CTB fix tags

Next you'll need to install our packages 'screed' and 'khmer'.
In this case we're going to use the versions tagged for the paper ::

 cd /usr/local/src

 git clone git://github.com/ged-lab/screed.git
 cd screed
 git checkout 2013-khmer-counting
 python setup.py install
 cd ..

 git clone http://github.com/ged-lab/khmer.git
 cd khmer
 git checkout 2013-khmer-counting
 make test
 cd ..

 echo 'export PYTHONPATH=/usr/local/src/khmer/python' >> ~/.bashrc
 echo 'export PATH=$PATH:/usr/local/src/khmer/scripts' >> ~/.bashrc
 echo 'export PATH=$PATH:/usr/local/src/khmer/sandbox' >> ~/.bashrc
 source ~/.bashrc

OK, now all your software is installed, hurrah!


Running the pipeline
--------------------

Now go into the pipeline directory and run the pipeline.  This will take a few
hours hours, so you might want to do it in 'screen' (see `"Running long jobs on
UNIX" <http://ged.msu.edu/angus/tutorials-2011/unix_long_jobs.html>`__). ::

 cd /mnt/2013-khmer-counting/pipeline
 make KHMER=/usr/local/src/khmer

Once it successfully completes, copy the data over to the ../data/ directory::

 make copydata

Run the ipython notebook server::

 cd ../notebook
 ipython notebook --pylab=inline --no-browser --ip=* --port=80 &

Connect into the ipython notebook (it will be running at 'http://<your EC2 hostname>'); if the above command succeeded but you can't connect in, you probably forgot to enable port 80 on your EC2 firewall.

Once you're connected in, select the 'khmer-counting' notebook (should be the
only one on the list) and open it.  Once open, go to the 'Cell...' menu
and select 'Run all'.


Now go back to the command line and execute::

 % cd ../
 % make

and voila, 'khmer-counting.pdf' will contain the paper with the figures you just
created.


