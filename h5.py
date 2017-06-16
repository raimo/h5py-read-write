import argparse
import h5py
import sys
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--out')
parser.add_argument('--file')
args = parser.parse_args(sys.argv[1:])

ar = None
if args.file:
    with h5py.File(args.file, 'r', driver='core') as f:
        ar = f['array']
        print(ar[...])
if args.out:
    with h5py.File(args.out, 'w', driver='core') as f:
        ar = ar or np.array([1,2,3])
        a =f.create_dataset('array', (len(ar),), dtype='i')
        a[...] = ar




