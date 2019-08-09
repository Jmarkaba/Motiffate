Background 
===============
CeO2/Pt Interfacial Surface Interactions

Description/Theory: 
    There are significant structural changes in the ceria (CeO2) interface from the oxygen exchange
on the surface. As CO molecules attached to the Platinum (Pt), O is pulled from the ceria and reacts 
with CO to form CO2 on the surface of the Pt. The dynamics that occur in these locations result in 
those atomic columns often becoming very noisy or blurry in the resulting TEM images.

Goal:
    We seek to find some correlation between the movement and intensity changes on the surface of the 
CeO2 with the dynamics of the Pt particle. We hope to find a way to proportionally represent
the oxygen exchange that occurs on the surface of the particle.

Approach:
    Each image is represent as a graph with atomic columns (both of the cerium, Ce, and the platinum, Pt)
as nodes, each of which stores the postition and intensity of the atomic column at that time. Iterating 
through the time series stack of these graphs we can create seperate time series lists to analyze the 
data (e.g., the change in positions of each column over time, or some other metric that combines 
the position and intensity).
    The metric used for analysis will be plotted along with the other selected columns to see if there is
any pattern that correlates the Pt structural dynamics with the changes on the surface of the CeO2.
    We can also compare the graph strucures (or subgraphs/individual nodes) in the time series data to see if 
there are any repeated patterns in the data, which may or may not indicate something significant about how
oxygen exchange occurs in 

Usage
===============
Python v. 3.6.8
**Note: All input image files must be TIFF files (.tif/.tiff). All data files of atom column positions  must be CSV (.csv) format.**

Install pip dependencies
`pip install -r requirements.txt` or `python -m pip install -r requirements.txt` for certain Windows users

Run the script (should act like a console for manipulating data)
`python main.py`

Examples
===============
![Single frame graph overlay of Pt on CeO2 rod in atmospheric N2](https://drive.google.com/open?id=12e_KlGYdAI1wEZyNkuFifd1UlKGQ6o47)


***Work in Progress***
