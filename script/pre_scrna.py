import os,sys,re
import subprocess
import argparse

docker="scrna:latest"

def cellbender(h5_file,outdir,prefix):
    #CellBender:https://github.com/broadinstitute/CellBender
    #CellBender is a software package for eliminating technical artifacts from high-throughput single-cell RNA sequencing (scRNA-seq) data.
    #Fleming S J, Chaffin M D, Arduini A, et al. Unsupervised removal of systematic background noise from droplet-based single-cell experiments using CellBender[J]. Nature methods, 2023, 20(9): 1323-1335.
    h5_file=os.path.abspath(h5_file)
    outdir=os.path.abspath(outdir)
    if not os.path.exists(outdir):
        subprocess.check_call(f'mkdir -p {outdir}',shell=True)
    cmd=(f'docker -v {os.path.dirname(h5_file)}:/raw_data/ -v {outdir}:/outdir {docker} sh -c\'export PATH=/opt/conda/bin/:$PATH && '
         f'cellbender remove-background --cuda --input /raw_data/{h5_file.split("/")[-1]} --output /outdir/{prefix}_cellbender_output_file.h5\'')
    subprocess.check_call(cmd,shell=True)

def scDblFinder():
    #scDblFinder:https://github.com/plger/scDblFinder
    #The scDblFinder package gathers various methods for the detection and handling of doublets/multiplets in single-cell sequencing data (i.e. multiple cells captured within the same droplet or reaction volume), including the novel scDblFinder method.
    #Germain P L, Lun A, Meixide C G, et al. Doublet identification in single-cell sequencing data using scDblFinder[J]. f1000research, 2022, 10: 979.
    pass


if __name__ == "__main__":
    parser=argparse.ArgumentParser("")