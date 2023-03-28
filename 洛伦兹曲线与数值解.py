import numpy as np;
from mpl_toolkits.mplot3d import Axes3D;
from scipy.integrate import odeint;
import matplotlib.pyplot as plt;
def dmove1(Point,t,sets) :
    p,r,b = sets;
    x,y,z = Point;
    return np.array([p*(y - x), x*(r - z), x*y-b * z]);
t = np.arange(0,30,0.001);
P1 = odeint(dmove1, (0.,1., 0.), t , args=([10.,28.,3.],));
P2 = odeint(dmove1, (0., 1.01, 0.), t, args=([10.,28.,3.],));
fig = plt.figure;
ax = Axes3D(fig);
ax.plot(P1[:,0], P1[:, 1],P1[:,2]);
ax.plot(P2[:,0], P2[:, 1],P2[:,2]);
plt.show()