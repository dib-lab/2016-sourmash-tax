all: db.sbt.json
	./tax-breakdown.py db data/acido.fa.gz -o acido
	./tax-breakdown.py db data/15genome.fa.gz -o 15genome

clean:
	./tax-breakdown.py db data/acido.fa.gz -o acido --clean
	./tax-breakdown.py db data/acido.fa.gz -o 15genome --clean

db.sig:
	../../sourmash/sourmash compute --singleton data/15genome.fa.gz -o db.sig

db.sbt.json: db.sig
	../../sourmash/sourmash sbt_index db db.sig
