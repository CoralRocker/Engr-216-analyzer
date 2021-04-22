# analyzer.py -- analyzes and puts into usable form the data from air-table tracking cameras
# By Gaultier Delbarre
# Sidenote -- be careful importing everything from here, as I define a lot of variables,
#   which you might accidentally overwrite. 

# ## Example Usage
# from analyzer import *
# lab_data = lab_analyzer('data_sheet_1.csv')
# ## To get, say, the y acceleration of the green marker, you'd use - 
# green_y_accel = lab_data[grn][ay]

import re
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

# Marker Color Variables, Cuz im a bitch who don't like typing
grn = 'green'
ylw = 'yellowneon'
orng = 'darkorange'
pnk = 'hotpink'
lorng = 'lightorange'

# OOH More dictionary key variables so i dont have to type
frame = 'frame_no'
time = 'timestamp'
size = 'size_px'
pos_x = 'position_px_x'
pos_y = 'position_px_y'
rx = 'rx' # Yes, my laziness extends to typing even two extra characters.
ry = 'ry' # Screw you, leave me be.
vx = 'vx'
vy = 'vy'
ax = 'ax'
ay = 'ay'

'''
Returns the first index in x where there are at least 
num_consecutive non-zero values.

Returns None on failure to find valid index.
'''
def fgt0(x, num_consecutive=10):
    for i in range(len(x)):
        if sum([abs(x[j])>0 for j in range(i, i+num_consecutive)]) == num_consecutive:
            return i
    return None

'''
Returns the first index in a where there are at least num_consecutive
values between x-dx < value < x+dx

Returns None on failure to find valid index. 
'''
def fgtdx(a, x=0, dx=0.5, num_consecutive=10):
    for i in range(len(a)):
        if sum([abs(x - a[j]) < dx for j in range(i, i+num_consecutive)]) == num_consecutive:
            return i
    return None

'''
Returns the float value of the given string s.
If s is not a float, it returns default (which defaults to 0)
'''
def floatify(s, default=0):
    try:
        n = float(s)
    except ValueError:
        n = default
    return n

'''
Wowza
Returns a dictionary containing the data for each marker in the specified filename.
filename is the name of the csv file containing the lab data. 
start is the index  at which to start putting data into the dictionary.
For example, if the first 3 rows of the csv are blank or not good data, start should be 4,
so the function skips the first 3 rows.

This function returns a dictionary containing markers. The markers themselves are dictionaries 
containing that marker's data. The data is in numpy arrays. The lab_analyze_list() function
returns the data for each marker in a standard python list instead of a numpy array if that works
better for you.
'''
def lab_analyze(filename, start=1):
    
    f = open(filename, 'r')
    data = list(map(lambda x: x.strip().split(','), f.readlines()))
    datacols = list(zip(*data))    
    f.close()
    
    od = dict()
    
    rxp = re.compile("(.*)-([A-z]+)$")

    for i, key in enumerate(data[0]):
        m = rxp.match(key)
        if not m:
             od[key] = np.asarray(list(map(floatify, datacols[i][start:])))
        else:
            grpnm = m.group(2)
            key = m.group(1)
            if grpnm in od.keys():
                od[grpnm][key] = np.asarray(list(map(floatify, datacols[i][start:])))
            else:
                od[grpnm] = {key: np.asarray(list(map(floatify, datacols[i][start:])))}
    return od


'''
The same as the standard lab_analyze, but returns the data in a list instead of
a numpy array. Read the standard function's description for more info.
'''
def lab_analyze_list(filename, start=1):
    
    f = open(filename, 'r')
    data = list(map(lambda x: x.strip().split(','), f.readlines()))
    datacols = list(zip(*data))    
    f.close()
    
    od = dict()
    
    rxp = re.compile("(.*)-([A-z]+)$")

    for i, key in enumerate(data[0]):
        m = rxp.match(key)
        if not m:
             od[key] = list(map(floatify, datacols[i][start:]))
        else:
            grpnm = m.group(2)
            key = m.group(1)
            if grpnm in od.keys():
                od[grpnm][key] = list(map(floatify, datacols[i][start:]))
            else:
                od[grpnm] = {key: list(map(floatify, datacols[i][start:]))}
    return od