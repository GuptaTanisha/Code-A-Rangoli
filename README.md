# Code-A-Rangoli
# Code-Rangoli

## Libraries and packages used
- Used python libraries such as _matplotlib_ and _numpy_.
- Used _*matplotlib.pyplot*_ which is a state-based interface to matplotlib. It provides a _MATLAB-like_ way of plotting.

## What does the code do?
```python
ax1.triplot(triang, 'r:', lw=1)
```
The above code draws a unstructured triangular grid as markers as shown below.
![alt text](https://github.com/GuptaTanisha/Code-A-Rangoli/blob/main/images/Figure1.png)

```python
tpc = plotlib.tripcolor(triang, z, shading ='flat') 
plotlib.hot() 
```
The above code creates a pseudocolor plot of an unstructured triangular grid as shown below.

![alt text](https://github.com/GuptaTanisha/Code-A-Rangoli/blob/main/images/Figure2.png)

The superposition of the above two figures gives rise to the following figure which is _rangoli_.

![alt text](https://github.com/GuptaTanisha/Code-A-Rangoli/blob/main/images/Figure3.png)
