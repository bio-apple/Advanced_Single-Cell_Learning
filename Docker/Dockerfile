FROM alpine:latest
RUN apk add --no-cache bash wget ca-certificates && mkdir -p /lib64/ /ref/ /script/ /raw_data/ /outdir/ &&  \
    wget -q -O /opt/Miniforge3-Linux-x86_64.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
    bash /opt/Miniforge3-Linux-x86_64.sh -f -b -p /opt/conda/ && rm -rf /opt/Miniforge3-Linux-x86_64.sh /var/cache/apk/* &&  \
    /opt/conda/bin/pip3 install cellbender==0.3.0 &&  \
    /opt/conda/bin/conda install conda-forge::r-seurat  \
    bioconda::bioconductor-clusterprofiler bioconda::bioconductor-scdblfinder conda-forge::r-harmony &&  \
    rm -f /root/.condarc && /opt/conda/bin/conda clean -a -y

