# To use our khmer container 



#To build this container yourself do the following

#Make directory for dockerfile 

	mkdir "path"/make_khmer
	cd "path"/make_khmer
	
#Make docker file 

	cat <<EOF > Dockerfile
	FROM ubuntu:15.10
	RUN apt-get update && apt-get install -y git \
		python2.7-dev \
		python-pip \
		gcc \
   		g++
	RUN cd /home
	RUN git clone https://github.com/dib-lab/khmer.git && \
		cd khmer && \
		git checkout v2.1.1 && \
		python setup.py install 
	EOF
	
#Check it out 

	cat Dockerfile

#Build docker image 

	docker build -t khmer_ctr .

#Test it 

	docker run -it khmer_ctr .
	
#Move into directory for assembly
	
	cd "path to data"

#Link data to docker image and run 

	docker run -v "path to data":/mydata -it khmer_ctr
	
#To make container available for public use 

	docker login 

	docker build -t brooksph/khmer .

	docker push brooksph/khmer 
