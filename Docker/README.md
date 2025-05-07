if (!requireNamespace("remotes", quietly = TRUE)) {
  install.packages("remotes")
}
install.packages('Signac')
remotes::install_github("satijalab/seurat-data", quiet = TRUE)
remotes::install_github("satijalab/azimuth", quiet = TRUE)
remotes::install_github("satijalab/seurat-wrappers", quiet = TRUE)


/opt/conda/bin/conda create -n r-base4.1.0 --channel conda-forge --channel bioconda --channel defaults --channel pwwang r-base==4.1.0 r-seuratwrappers && \



    /opt/conda/bin/conda create -n r-base4.4.3 --channel conda-forge --channel bioconda --channel defaults --channel dnachun r-base==4.4.3 r-seurat==5.3.0  \
    r-devtools r-essentials r-biocmanager bioconductor-clusterprofiler bioconductor-scdblfinder bioconductor-singler r-monocle3 bioconductor-deseq2 bioconductor-aucell r-cellchat celltypist && \
    /opt/conda/bin/pip3 install --no-cache-dir cellbender==0.3.0 && \
    /opt/conda/bin/conda clean -a -y && \
    rm -f /root/.condarc


/opt/conda/bin/conda create -n r-base4.0.3 --channel conda-forge --channel bioconda --channel defaults --channel bioturing r-base==4.0.3 r-nichenetr
