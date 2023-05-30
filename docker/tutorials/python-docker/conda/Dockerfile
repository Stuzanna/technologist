# syntax=docker/dockerfile:1

# https://pythonspeed.com/articles/activate-conda-dockerfile/
# used this for conda version

# -below is the tutorial
# FROM python:3.8-slim-buster
# WORKDIR /app
# COPY requirements.txt requirements.txt
# end

FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
# RUN conda env create -f environment.yml
RUN conda create --name envVar --file environment.yml

# Make RUN commands use the new environment:
RUN echo "conda activate envVar" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"

# The code to run when container is started:
COPY run.py entrypoint.sh ./
ENTRYPOINT ["./entrypoint.sh"]