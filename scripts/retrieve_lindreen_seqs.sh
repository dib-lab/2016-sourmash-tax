### This script retrieves data for Lindgreen et al 2016 An evaluation of the accuracy 
and speed of metagenome analysis tools. Scientific Reports. 6, 19233. Links were
retrieved from http://www.ucbioinformatics.org/metabenchmark.html.

for i in $(cat lindgreen_sequences.txt)
do
curl -O $i
done

