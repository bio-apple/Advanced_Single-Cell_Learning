FROM alpine:latest
RUN apk add --no-cache bash wget ca-certificates && mkdir -p /lib64/ /ref/ /script/ /raw_data/ /outdir/ &&  \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.35-r1/glibc-2.35-r1.apk &&  \
    apk add --no-cache --force-overwrite glibc-2.35-r1.apk && rm glibc-2.35-r1.apk && \
    for lib in /usr/glibc-compat/lib/*; do \
      ln -sf "$lib" /lib/ && \
      ln -sf "$lib" /lib64/ || true; \
    done && \
    wget -q -O /opt/Miniforge3-Linux-x86_64.sh https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh && \
    bash /opt/Miniforge3-Linux-x86_64.sh -f -b -p /opt/conda/ && rm -rf /opt/Miniforge3-Linux-x86_64.sh /var/cache/apk/* &&  \
    /opt/conda/bin/pip3 install cellbender==0.3.0 &&  \
    /opt/conda/bin/conda install conda-forge::r-seurat  \
    bioconda::bioconductor-clusterprofiler bioconda::bioconductor-scdblfinder conda-forge::r-harmony &&  \
    rm -f /root/.condarc && /opt/conda/bin/conda clean -a -y

