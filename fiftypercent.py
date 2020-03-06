import numpy as np
import sys
import json
from collections import Counter
from util import domains

with open(sys.argv[1], 'r') as f:
	data = json.load(f)

counts = Counter(domains(data))
counts_flat = sorted(counts.values())[::-1]

percents = np.cumsum(counts_flat)/sum(counts_flat)
lt50 = np.count_nonzero(percents <= 0.5)
print(f'{percents[lt50] * 100}% of users contained in the top {lt50+1} instances')