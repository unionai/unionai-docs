---
title: Nucleotide Sequence Querying with BLASTX
weight: 1
variants: +flyte -serverless -byoc -selfmanaged
sidebar_expanded: false
---

# Nucleotide Sequence Querying with BLASTX

This tutorial demonstrates the integration of computational biology and Flyte.
The focus will be on searching a nucleotide sequence against a local protein database to identify possible homologues.
The steps include:

- Data loading
- Creation of a {ref}`ShellTask <shell_task>` to execute the BLASTX search command
- Loading of BLASTX results and plotting a graph of "e-value" vs "pc identity"

This tutorial is based on the reference guide ["Using BLAST+ Programmatically with Biopython"](https://widdowquinn.github.io/2018-03-06-ibioic/02-sequence_databases/03-programming_for_blast.html).

## BLAST

The Basic Local Alignment Search Tool (BLAST) is a program that identifies similar regions between sequences.
It compares nucleotide or protein sequences with sequence databases and evaluates the statistical significance of the matches.
BLAST can be used to deduce functional and evolutionary relationships between sequences and identify members of gene families.

For additional information, visit the [BLAST Homepage](https://blast.ncbi.nlm.nih.gov/Blast.cgi).

### BLASTX

BLASTx is a useful tool for searching genes and predicting their functions or relationships with other gene sequences.
It is commonly employed to find protein-coding genes in genomic DNA or cDNA, as well as to determine whether a new nucleotide sequence encodes a protein or to identify proteins encoded by transcripts or transcript variants.

This tutorial will demonstrate how to perform a BLASTx search.

## Data

The database used in this example consists of predicted gene products from five Kitasatospora genomes.
The query is a single nucleotide sequence of a predicted penicillin-binding protein from Kitasatospora sp. CB01950.

> [!NOTE]
> To run the example locally, you need to download BLAST.
> You can find OS-specific installation instructions in the [user manual](https://www.ncbi.nlm.nih.gov/books/NBK569861/).

## Dockerfile

```dockerfile
FROM ubuntu:focal

ENV VENV /opt/venv
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONPATH /root

RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install -y \
    && apt-get update \
    && apt-get install -y \
    cmake \
    curl \
    python3.8 \
    python3.8-venv \
    python3.8-dev \
    make \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-pip \
    zlib1g-dev \
    vim \
    wget

# Install the AWS cli separately to prevent issues with boto being written over
RUN pip3 install awscli

WORKDIR /opt
RUN curl https://sdk.cloud.google.com > install.sh
RUN bash /opt/install.sh --install-dir=/opt
ENV PATH $PATH:/opt/google-cloud-sdk/bin
WORKDIR /root

# Virtual environment
ENV VENV /opt/venv
RUN python3 -m venv ${VENV}
ENV PATH="${VENV}/bin:$PATH"

# Download BLAST
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.13.0/ncbi-blast-2.13.0+-x64-linux.tar.gz && \
    tar -xzf ncbi-blast-2.13.0+-x64-linux.tar.gz

# Set the working directory
WORKDIR /root

# Install Python dependencies
COPY requirements.in /root
RUN ${VENV}/bin/pip install -r /root/requirements.in

# Copy data
# COPY blast/kitasatospora /root/kitasatospora

# Copy the actual code
COPY . /root/

# Copy over the helper script that the SDK relies on
RUN cp ${VENV}/bin/flytekit_venv /usr/local/bin/
RUN chmod a+x /usr/local/bin/flytekit_venv

# Check if BLAST is installed
ENV PATH=$PATH:/root/ncbi-blast-2.13.0+/bin
RUN echo $PATH
RUN output="$(which blastx)" && echo $output

# This tag is supplied by the build script and will be used to determine the version
# when registering tasks, workflows, and launch plans
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
```

Initiate the workflow on the Flyte backend by executing the following two commands in the "bioinformatics" directory:

```shell
$ pyflyte --pkgs blast package --image ghcr.io/flyteorg/flytecookbook:blast-latest
$ flytectl register files --project flytesnacks --domain development --archive flyte-package.tgz --version v1
```