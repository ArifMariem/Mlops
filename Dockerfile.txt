FROM jupyter/scipy-notebook
FROM centos:7

RUN yum -y install python3-pip \
    pip3 install joblib


USER root

RUN yum update && \
    yum install -y jq \
    mkdir model raw_data  results


ENV RAW_DATA_DIR=/home/mariem/raw_data
ENV MODEL_DIR=/home/jovyan/model
ENV RESULTS_DIR=/home/jovyan/results
ENV RAW_DATA_FILE=Iris.csv


COPY Iris.csv ./raw_data/Iris.csv
COPY train.py ./train.py
COPY test.py ./test.py