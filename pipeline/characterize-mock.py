#! /usr/bin/env python
"""
characterize a "mock community" in terms of k-mer cardinality of each genome.
"""
import khmer
import screed
import re

total_hll = khmer.HLLCounter(.01, 31)
x = []
for record in screed.open('15genome.fa.gz'):
    hll = khmer.HLLCounter(.01, 31)

    seq = re.sub('[^ACGT]', 'A', record.sequence.upper())
    hll.consume_string(seq)

    print(record.name, hll.estimate_cardinality())
    x.append((hll.estimate_cardinality(), record.name))
    total_hll.merge(hll)

print('total', total_hll.estimate_cardinality())
total = total_hll.estimate_cardinality()

y = []
for (c, n) in x:
    y.append((c / total, n))

y.sort()
y.reverse()

for c, n in y:
    print('{:.2f} {}'.format(c, n))
