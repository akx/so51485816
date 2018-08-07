import argparse

import numpy as np
import os
import pandas as pd
import resource
import sys
import time

# rusage maxrss is bytes on darwin
rss_divisor = (1024 if sys.platform == 'darwin' else 1)


def fn(n):
    a = np.arange(n, dtype=np.int64)
    b = pd.unique(a)
    assert len(b) == len(a)


def do_task(n):
    pid = os.fork()
    if pid == 0:
        t0 = time.perf_counter()
        fn(n)
        t1 = time.perf_counter()
        r = resource.getrusage(resource.RUSAGE_SELF)
        rss = r.ru_maxrss / rss_divisor
        print(n, rss, t1 - t0, r.ru_utime, r.ru_stime)
        sys.exit(0)
    else:
        pid, stat = os.waitpid(pid, 0)
        if stat:
            raise RuntimeError(f'child ended with error {stat}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--start', default=0, type=int)
    ap.add_argument('--end', default=100_000_000, type=int)
    ap.add_argument('--step', default=25_000, type=int)
    ap.add_argument('--step-delta', default=0, type=int)
    args = ap.parse_args()
    x = args.start
    while x <= args.end:
        do_task(x)
        x += args.step
        args.step += args.step_delta
