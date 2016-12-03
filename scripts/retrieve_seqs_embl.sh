for i in $(cat actinobacteria_seq_id.txt)
do
wget -O $i.fa http://www.ebi.ac.uk/Tools/dbfetch/dbfetch/embl/$i/fasta
done
