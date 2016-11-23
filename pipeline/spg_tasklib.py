import sys
import os.path
import glob
import shutil

from doit_utils import make_task

from doit.tools import run_once
from doit.task import clean_targets


SOURMASH_LOCATION='../../sourmash'


@make_task
def task_calc_unique_kmers(output_dir, inp_filenames, ksize=31):
    CMD_unique_kmers = "unique-kmers.py -k {ksize} -R {0}/kmers.txt {1}"
    
    CMD_unique_kmers = CMD_unique_kmers.format(output_dir,
                                               " ".join(inp_filenames),
                                               ksize=ksize)

    target = "{0}/kmers.txt".format(output_dir)

    name='calc_unique_kmers<{0},{1}>'.format(ksize, ",".join(inp_filenames))

    return dict(name=name,
                actions=[CMD_unique_kmers],
                targets=[target],
                uptodate=[run_once],
                file_dep=inp_filenames,
                clean=[clean_targets])


@make_task
def task_build_scaled_minhash(output_dir, input_filenames, ksize=31):
    def retrieve_num_kmers():
        open('/tmp/xxx', 'wt').write('foo')
        return 'touch /tmp/zzz'
        
    CMD = '{0}/sourmash compute -k {ksize} --name combined -o {1} {2}'

    output_file = '{}/combined.sig'.format(output_dir)
    CMD = CMD.format(SOURMASH_LOCATION,
                     output_file,
                     " ".join(input_filenames),
                     ksize=ksize)

    targets = [ output_file ]

    name = 'task_build_scaled_minhash<{0}.{1}>'
    name = name.format(ksize, ",".join(input_filenames))

    deps = list(input_filenames)

    return {'name': name,
            'actions': [retrieve_num_kmers, CMD],
            'targets': targets,
            'uptodate': [run_once],
            'file_dep': deps,
            'clean': [clean_targets]}
