FROM ubuntu:15.10
RUN apt-get update && apt-get install -y python-dev zlib1g git python-setuptools g++ make    
RUN cd /home
RUN git clone https://github.com/dib-lab/sourmash.git &&     cd sourmash &&     python setup.py install 
