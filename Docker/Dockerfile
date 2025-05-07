FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends  libcurl4-openssl-dev\
    build-essential wget curl ca-certificates bzip2 gnupg git libssl-dev libffi-dev libz-dev libbz2-dev && \
    mkdir -p /ref/ /script/ /raw_data/ /outdir/ && \
    rm -rf /var/lib/apt/lists/* && ARCH=$(uname -m) && \
    wget -q -O /miniforge.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-${ARCH}.sh && \
    bash /miniforge.sh -b -p /opt/conda && \
    rm /miniforge.sh &&  \
    /opt/conda/bin/conda install -y conda-forge::r-base==4.4.3 conda-forge::r-devtools conda-forge::r-essentials conda-forge::r-biocmanager conda-forge::r-seurat==5.3.0  \
    bioconda::bioconductor-clusterprofiler bioconda::bioconductor-scdblfinder && \
    /opt/conda/bin/pip3 install --no-cache-dir cellbender==0.3.0 && \
    /opt/conda/bin/conda clean -a -y && \
    rm -f /root/.condarc
