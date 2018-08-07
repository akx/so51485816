import argparse
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True)
args = ap.parse_args()

with open(args.input, 'r') as infp:
    data = [[float(v) for v in line.strip().split(" ")] for line in infp]

ns = [d[0] for d in data]
mems = [d[1] for d in data]

plt.plot(ns, mems, label='peak-memory')
plt.xlabel('n')
plt.ylabel('peak memory in KB')
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
plt.ylim(0, ymax)
plt.xlim(0, xmax)
plt.legend()
plt.savefig(args.input + '.svg')
plt.show()
