###To use our container



###To build this container yourself do the following

###Make directory for dockerfile 

	mkdir "path"/make_sourmash
	cd "path"/make_sourmash
	
###Make docker file 

	cat <<EOF > Dockerfile
	FROM ubuntu:15.10
	RUN apt-get update && apt-get install -y python-dev \
	zlib1g \
	git \
	python-setuptools \
	g++ \
	make    
	RUN cd /home
	RUN git clone https://github.com/dib-lab/sourmash.git && \
		cd sourmash && \
		python setup.py install 
	EOF
	
###Check it out 

	cat Dockerfile

###Build docker image 

	docker build -t sourmash_ctr .

###Test it 

	docker run -it sourmash_ctr sourmash compute 
	
###Move into directory for assembly
	
	cd "path to data"

###Link data to docker image and run 

	docker run -it sourmash_ctr sourmash compute -h
	
###Move into directory for assembly
	
	cd "path to data"

###Link data to docker image and run 

	docker run -v "path to data":/mydata -it sourmash_ctr
	
###To make container available for public use 

	docker login 

	docker build -t brooksph/sourmash .

	docker push brooksph/sourmash
