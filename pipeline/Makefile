all: db.sbt.json
	./sourtax.py db data/acido.fa.gz -o acido
	./sourtax.py db data/15genome.fa.gz -o 15genome

clean:
	./sourtax.py db data/acido.fa.gz -o acido --clean
	./sourtax.py db data/acido.fa.gz -o 15genome --clean

db.sig:
	../../sourmash/sourmash compute --singleton data/15genome.fa.gz -o db.sig \
		--with-cardinality

db.sbt.json: db.sig
	../../sourmash/sourmash sbt_index db db.sig
