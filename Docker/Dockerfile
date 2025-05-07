FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends  libcurl4-openssl-dev\
    build-essential wget curl ca-certificates bzip2 gnupg git libssl-dev libffi-dev libz-dev libbz2-dev && \
    mkdir -p /ref/ /script/ /raw_data/ /outdir/ && \
    rm -rf /var/lib/apt/lists/* && ARCH=$(uname -m) && \
    wget -q -O /miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-${ARCH}.sh && \
    bash /miniforge.sh -b -p /opt/conda && \
    rm /miniforge.sh &&  \
    /opt/conda/bin/conda create -n r-base4.0.3 --channel conda-forge --channel bioconda --channel defaults --channel bioturing r-base==4.0.3 r-nichenetr && \
    /opt/conda/bin/conda create -n r-base4.1.0 --channel conda-forge --channel bioconda --channel defaults --channel pwwang r-base==4.1.0 r-seuratwrappers && \
    /opt/conda/bin/conda create -n r-base4.4.3 --channel conda-forge --channel bioconda --channel defaults --channel dnachun r-base==4.4.3 r-seurat  \
    r-devtools r-essentials r-biocmanager bioconductor-clusterprofiler bioconductor-scdblfinder bioconductor-singler r-monocle3 bioconductor-deseq2 bioconductor-aucell r-cellchat celltypist && \
    /opt/conda/bin/pip3 install --no-cache-dir cellbender==0.3.0 && \
    /opt/conda/bin/conda clean -a -y && \
    rm -f /root/.condarc
