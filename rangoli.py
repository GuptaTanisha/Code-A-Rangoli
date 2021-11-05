import matplotlib.pyplot as plotlib
import matplotlib.tri as tri
import numpy as numpy
no_of_divisions_for_angles = 40
n_radii = 20
min_radius = 0.35
radii = numpy.linspace(min_radius, 500, n_radii)

angles = numpy.linspace(0, 2 * numpy.pi, no_of_divisions_for_angles, endpoint=False)
angles = numpy.repeat(angles[..., numpy.newaxis], n_radii, axis=1)
angles[:, 1::2] += numpy.pi / no_of_divisions_for_angles

x = (radii * numpy.cos(angles)).flatten() #Return a flattened array of x-coordinates.
y = (radii * numpy.sin(angles)).flatten() #Return a flattened array of x-coordinates.
z = (numpy.sin(4 * radii) * numpy.cos(4 * angles)).flatten() 


# Create the Triangulation; no triangles specified so Delaunay triangulation created
triang = tri.Triangulation(x, y)
#Removes the unwanted triangles
triang.set_mask(numpy.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)

fig1, ax1 = plotlib.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'r:', lw=1)
ax1.axis(False)

tpc = plotlib.tripcolor(triang, z, shading ='flat') 
plotlib.hot() #Used to set the colormap to "hot".
plotlib.show()
