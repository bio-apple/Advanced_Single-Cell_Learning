FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash wget ca-certificates curl bzip2 gnupg git && \
    mkdir -p /ref/ /script/ /raw_data/ /outdir/ && \
    rm -rf /var/lib/apt/lists/* && ARCH=$(uname -m) && \
    wget -q -O /miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-${ARCH}.sh && \
    bash /miniforge.sh -b -p /opt/conda && \
    rm /miniforge.sh &&  \
    /opt/conda/bin/pip install --no-cache-dir cellbender==0.3.0 && \
    conda install -y -c conda-forge r-seurat r-harmony && \
    conda install -y -c bioconda bioconductor-clusterprofiler bioconductor-scdblfinder && \
    conda clean -a -y && \
    rm -f /root/.condarc
