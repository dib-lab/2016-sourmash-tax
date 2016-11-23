#! /usr/bin/env python
"""
Get a taxonomic breakdown of a FASTQ/FASTA file using minhashes.
"""
import os, sys

from doit_utils import run_tasks
from spg_tasklib import *


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('sbt_index')
    parser.add_argument('inp_fasta', nargs='+')
    parser.add_argument('-o', '--output-dir', default=None)

    parser.add_argument('--clean', default=False, action='store_true')
    args = parser.parse_args()

    output_dir = args.output_dir
    if not output_dir:
        output_dir = 'report'    # @CTB make this date-based or summat?

    try:
        os.mkdir(output_dir)
    except OSError:
        print('WARNING: output dir {} already exists.', file=sys.stderr)

    tasks = []
    tasks.append(task_calc_unique_kmers(output_dir, args.inp_fasta))
    tasks.append(task_build_scaled_minhash(output_dir, args.inp_fasta))
    tasks.append(task_search_index(output_dir, args.sbt_index, args.inp_fasta))

    if args.clean:
        run_tasks(tasks, ['clean'])
    else:
        run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
