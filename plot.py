# ====================================================================
# Author                : swc21
# Date                  : 2018-03-14 09:42:27
# Project               : ClusterFiles
# File Name             : plot
# Last Modified by      : swc21
# Last Modified time    : 2018-03-14 12:08:35
# ====================================================================

import matplotlib.pyplot as plt
import numpy as np
#import matplotlib.cm as cm
import time

from mpl_toolkits.mplot3d import Axes3D

data = np.load('/root/SHARED/mpi_nbody_out.npy')

fig = plt.figure(dpi=60)
plt.ion()
ax = fig.add_subplot(111, projection='3d')

masses = data[0, :, 3]

for i, slice in enumerate(data):

    # Offset from 0th prticle
    # slice[:][:3]-=slice[0][:3]

    first_slice = slice.T
    #ax = fig.add_subplot(111, projection='3d')
    x, y, z, m = first_slice[0], first_slice[1], first_slice[2], first_slice[3]
    # x-=x[0]
    # y-=y[0]
    # z-=z[0]

    #fig = plt.figure()
    lim = 100  # (np.max(slice)-np.min(slice))/4.0
    ax.set_xlim([lim//-4, lim])
    ax.set_ylim([lim//-4, lim])
    ax.set_zlim([lim//-4, lim])

    C = np.stack([m, m*m*m, 1.0-m*m, m/m])
    ax.scatter(x, y, z, c=m, s=m*100, alpha=1.0)
    # plt.axis('equal')
    plt.show()
    plt.pause(0.001)
    # if not i%15:
    plt.cla()
