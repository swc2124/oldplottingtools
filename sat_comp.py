# ====================================================================
# Author 				: swc21
# Date 					: 2018-03-14 09:47:15
# Project 				: ClusterFiles
# File Name 			: sat_comp
# Last Modified by 		: swc21
# Last Modified time 	: 2018-03-14 10:27:02
# ====================================================================
#
import matplotlib
import numpy as np
import numpy.ma as ma

from matplotlib import pyplot as pl
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
fig = pl.figure()
ax1 = fig.add_subplot(111, projection='3d')
fig = pl.gcf()
fig.set_size_inches(15, 15)
xop = itemgetter(0)
yop = itemgetter(1)
zop = itemgetter(2)
a = int(sys.argv[1])
for si in [a]:
    X = map(xop, satellites[si])
    Y = map(yop, satellites[si])
    Z = map(zop, satellites[si])
    ax1.plot(X, Y, Z, '.', ms=3, color='k', alpha=1)
    ebf_X = map(xop, ebf_satellites[si])
    ebf_Y = map(yop, ebf_satellites[si])
    ebf_Z = map(zop, ebf_satellites[si])
    ax1.plot(ebf_X, ebf_Y, ebf_Z, '.', ms=3, color='r', alpha=.3)
    # ax1.set_xlim([0,40])
    # ax1.set_ylim([-180,0])
    # ax1.set_zlim([0,30])
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    pl.grid(True)
    pl.show()
    #save("/root/NAS/Shared/Documents/sat_plt_%s" % file_number, ext='png', close=True, verbose=True)
