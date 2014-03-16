import numpy as np
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def draw(filename):
    fig = plt.figure(figsize=(8,6))

    ax = fig.add_subplot(111,projection='3d')

    x=[]
    y=[]
    z=[]
    v=[]

    file_obj = open(filename,'r')
    for line in file_obj:
        line = line.rstrip()
        fields = line.split()
        if fields[2]!='0':
            x.append(float(fields[0].split('-')[0]))
            y.append(float(fields[0].split('-')[1]))
            z.append(float(fields[1]))
            v.append(float(fields[2]))
    file_obj.close()
    x=np.array(x)
    y=np.array(y)
    z=np.array(z)
    v=np.array(v)
    colors = cm.Reds(v/max(v))
    #print colors
    colmap = cm.ScalarMappable(cmap=cm.Reds)
    colmap.set_array(v)
    
    yg = ax.scatter(x, y, z, c=colors,s=100,marker='o',alpha=0.5)
    #edgecolor='none',
    cb = fig.colorbar(colmap)
    
    ax.set_xlabel('SampleA')
    ax.set_ylabel('SampleB')
    ax.set_zlabel('SampleC')
    
    
    plt.show()
    
    
    return 1
    
    

#draw("../data/comb_Empirical_1X_A_B_C.count")
#draw("../data/comb_Empirical_20X_A_B_C.count")
#draw("../data/comb_Empirical_6X_1A_1B_1C.count")
draw("../data/comb_Empirical_6X_1A_1B_1C_keep.count")
