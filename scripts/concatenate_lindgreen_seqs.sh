for filename in *-0*.fq.gz
do
    # first, make the base by removing .extract.fastq.gz
    base=$(basename $filename .fq.gz)
    echo $base

    # now, construct the R2 filename by replacing R1 with R2
    baseR2=${base/-0/-1}
    echo $baseR2

    # construct the output filename
    output=${base/-0/}.cat.fq.gz

    cat ${base}.fq.gz ${baseR2}.fq.gz > $output
done
