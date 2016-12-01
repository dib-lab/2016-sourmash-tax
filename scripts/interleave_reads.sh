for filename in *_1*.cat.fq.gz
do
    # first, make the base by removing .extract.fastq.gz
    base=$(basename $filename .cat.fq.gz)
    echo $base

    # now, construct the R2 filename by replacing R1 with R2
    baseR2=${base/_1/_2}
    echo $baseR2

    # construct the output filename
    output=${base/_1/}interleaved.cat.fq.gz

    interleave-reads.py ${base}.cat.fq.gz ${baseR2}.cat.fq.gz | \
          gzip > $output
done

