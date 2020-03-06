import matplotlib.pyplot as plt
import seaborn as sb
import sys
import json

with open(sys.argv[1], 'r') as f:
	data = json.load(f)

domains = [
	u['addr'].split('@')[2]
	for u in data
]

counts = dict()
for dom in domains:
	counts[dom] = counts.get(dom, 0) + 1

print(sorted(counts.items(), key=lambda p: p[1])[::-1])

counts_flat = sorted(counts.values())[::-1]
plt.fill_between(range(len(counts_flat)), 0, counts_flat)
plt.show()