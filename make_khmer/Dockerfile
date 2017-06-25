FROM ubuntu:15.10
RUN apt-get update && apt-get install -y git     python2.7-dev     python-pip     gcc     g++
RUN cd /home
RUN git clone https://github.com/dib-lab/khmer.git &&     cd khmer &&     git checkout v2.1.1    && python setup.py install 
