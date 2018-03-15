# ====================================================================
# Author 				: swc21
# Date 					: 2018-03-14 09:47:15
# Project 				: ClusterFiles
# File Name 			: sat_auto_save_3x3
# Last Modified by 		: swc21
# Last Modified time 	: 2018-03-14 10:28:50
# ====================================================================
#
import numpy as np
import numpy.ma as ma

import matplotlib
import matplotlib.pyplot as pl

from mpl_toolkits.mplot3d import Axes3D

dat_satid, dat_px, dat_py, dat_pz, dat_mass = np.loadtxt(
    '/root/Documents/halo02.dat', usecols=[0, 1, 2, 3, 13], unpack=True)

unq_satid = np.unique(dat_satid)
tot_mass_by_satid = np.zeros((2, unq_satid.size))
for i, satid in enumerate(unq_satid):
    tot_mass = dat_mass[dat_satid == satid].sum()
    tot_mass_by_satid[:, i] = [satid, tot_mass]

satellites = []
for si in np.unique(dat_satid):
    indices = np.where(dat_satid == si)
    satellites.append(zip(dat_px[indices], dat_py[indices], dat_pz[indices]))


import ebf
ebf_data = ebf.read('/root/Documents/halo02_msto_subsample.ebf')

ebf_px = np.array(ebf_data['px']-8)
ebf_py = np.array(ebf_data['py'])
ebf_pz = np.array(ebf_data['pz']-0.015)

ebf_satid = np.unique(ebf_data['satid'])

assert len(ebf_satid) == len(satellites)

ebf_satellites = []
for si in np.unique(ebf_satid):
    indices = np.where(ebf_data['satid'] == si)
    ebf_satellites.append(
        zip(ebf_px[indices], ebf_py[indices], ebf_pz[indices]))

assert len(ebf_satellites) == len(satellites)

import sys

from operator import itemgetter

xop = itemgetter(0)
yop = itemgetter(1)
zop = itemgetter(2)


a = int(sys.argv[1])
b = int(sys.argv[2])

count = a
for si in range(a, b):

    X = map(xop, satellites[si])
    Y = map(yop, satellites[si])
    Z = map(zop, satellites[si])

    ebf_X = map(xop, ebf_satellites[si])
    ebf_Y = map(yop, ebf_satellites[si])
    ebf_Z = map(zop, ebf_satellites[si])

    fig = pl.figure(figsize=(16, 16))

# just ebf all three directions

    ax = fig.add_subplot(3, 3, 1, projection='3d')
    ax.plot(ebf_X, ebf_Y, ebf_Z, '.', ms=3, color='r', alpha=1)

    ax.set_xlabel('ebf-X')
    ax.set_ylabel('ebf-Y')
    ax.set_zlabel('ebf-Z')

    ax = fig.add_subplot(3, 3, 4, projection='3d')
    ax.plot(ebf_Y, ebf_Z, ebf_X, '.', ms=3, color='r', alpha=1)

    ax.set_xlabel('ebf-Y')
    ax.set_ylabel('ebf-Z')
    ax.set_zlabel('ebf-X')

    ax = fig.add_subplot(3, 3, 7, projection='3d')
    ax.plot(ebf_Z, ebf_X, ebf_Y, '.', ms=3, color='r', alpha=1)

    ax.set_xlabel('ebf-Z')
    ax.set_ylabel('ebf-X')
    ax.set_zlabel('ebf-Y')

# all combos all directions

    ax = fig.add_subplot(3, 3, 2, projection='3d')
    ax.plot(X, Y, Z, '.', ms=3, color='k', alpha=.9)
    ax.plot(ebf_X, ebf_Y, ebf_Z, '.', ms=3, color='r', alpha=.1)

    ax.set_xlabel('combo-X')
    ax.set_ylabel('combo-Y')
    ax.set_zlabel('combo-Z')

    ax = fig.add_subplot(3, 3, 5, projection='3d')
    ax.plot(Y, Z, X, '.', ms=3, color='k', alpha=.9)
    ax.plot(ebf_Y, ebf_Z, ebf_X, '.', ms=3, color='r', alpha=.1)

    ax.set_xlabel('combo-Y')
    ax.set_ylabel('combo-Z')
    ax.set_zlabel('combo-X')

    ax = fig.add_subplot(3, 3, 8, projection='3d')
    ax.plot(Z, X, Y, '.', ms=3, color='k', alpha=.9)
    ax.plot(ebf_Z, ebf_X, ebf_Y, '.', ms=3, color='r', alpha=.1)

    ax.set_xlabel('combo-Z')
    ax.set_ylabel('combo-X')
    ax.set_zlabel('combo-Y')

# just dat all three directions

    ax = fig.add_subplot(3, 3, 3, projection='3d')
    ax.plot(X, Y, Z, '.', ms=3, color='k', alpha=1)

    ax.set_xlabel('dat-X')
    ax.set_ylabel('dat-Y')
    ax.set_zlabel('dat-Z')

    ax = fig.add_subplot(3, 3, 6, projection='3d')
    ax.plot(Y, Z, X, '.', ms=3, color='k', alpha=1)

    ax.set_xlabel('dat-Y')
    ax.set_ylabel('dat-Z')
    ax.set_zlabel('dat-X')

    ax = fig.add_subplot(3, 3, 9, projection='3d')
    ax.plot(Z, X, Y, '.', ms=3, color='k', alpha=1)

    ax.set_xlabel('dat-Z')
    ax.set_ylabel('dat-X')
    ax.set_zlabel('dat-Y')

    pl.grid(True)
    pl.gcf().tight_layout()

    str_count = str(count)

    pl.savefig('/root/Documents/figure_%s.png' % str_count, format='png')
    pl.close()
    # pl.show()
    count = count + 1
