# 2016-sourmash-tax

Taxonomic breakdown of metagenomes using sourmash.

## Install instructions

Starting from a blank Ubuntu 15.10 install, run:

    sudo apt-get update && sudo apt-get -y install python3.5-dev \
        python3-virtualenv python3-matplotlib python3-numpy g++ make

then create a new virtualenv, :

    cd
    python3.5 -m virtualenv env -p python3.5 --system-site-packages
    . env/bin/activate

You'll need to install a few things, including a recent version of khmer:

    pip install screed pytest PyYAML doit
    pip install git+https://github.com/dib-lab/khmer.git

Next, grab the sbt_search branch of sourmash:

    cd
    git clone https://github.com/dib-lab/sourmash.git -b sbt_search

Build and install it:

    cd sourmash && make install

Next, grab this repo:

    cd
    git clone https://github.com/dib-lab/2016-sourmash-tax.git

The `sourtax.py` script will now be in
`~/2016-sourmash-tax/pipeline/sourtax.py`.  See the demo section below.

## Preparing a database

To prepare a database, you need to calculate sourmash signatures that
contain the k-mer cardinality of the source sequence.  This can be done
using the `--with-cardinality` option:

    sourmash compute --with-cardinality genome.fa

If you have a FASTA file containing a bunch of genomes, sourmash will
by default calculate a single signature for all of them; you can fix
this by using the `--singleton` option:

    sourmash compute --singleton --with-cardinality all-genomes.fa

Once you have the signatures calculated, you can build the database
(here named 'db') with `sourmash sbt_index`:

    sourmash sbt_index db *.sig

So, for example, to build a search database from the `data/15genome.fa.gz`
file included in this repo, do:

    sourmash compute --singleton --with-cardinality data/15genome.fa.gz
    sourmash sbt_index db 15genome.fa.gz.sig

## Demo/quickstart

First, create a database:

    cd
    mkdir demo
    cd demo

    sourmash compute --singleton --with-cardinality ~/2016-sourmash-tax/pipeline/data/15genome.fa.gz
    sourmash sbt_index db 15genome.fa.gz.sig

Now, take an input sequence and break it down:

    cp ~/2016-sourmash-tax/pipeline/data/*.fa.gz .

A single genome:

    ~/2016-sourmash-tax/pipeline/sourtax.py db acido.fa.gz -o acido

A fake metagenome:

    ~/2016-sourmash-tax/pipeline/sourtax.py db 15genome.fa.gz -o 15genome

## Guide to input sequences

Main point: if you are inputting FASTQ, the input sequences need to be
error trimmed (e.g. with `trim-low-abund.py`).

Also note that currently *abundance* is not taken into account, and
the output *is* weighted by size of genome (which is easily corrected
for).
