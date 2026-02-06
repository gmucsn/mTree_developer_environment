FROM  continuumio/miniconda3:25.3.1-1
LABEL version="MTREE-DEV-CONTAINER-1"

RUN apt-get update && apt-get install -y build-essential

WORKDIR /tmp

RUN git clone -b version_2 https://github.com/gmucsn/mTree.git && \ 
pip install -e /tmp/mTree

WORKDIR /dev
# RUN /opt/conda/bin/pip install -e /workspaces/mTree