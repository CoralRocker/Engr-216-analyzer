# Engr-216-analyzer
A simple api to analyze data retrieved from air tables for the TAMU ENGR 216 course. 

# Defined Variables 
`analyzer.py` defines a few variables for convenience and ease of use.
The variables automatically defined include names for the tracking sticker
markers, names for information about the markers, and timestamp and frame.

| Variable | Value | Usage |
| :-- | :-: | :-- |
| grn | 'green' | Name for green marker|
| ylw | 'yellowneon' | Name for yellow marker |
| orng | 'darkorange' | Name for dark orange marker |
| lorng | 'lightorange' | Name for light orange marker |
| pnk | 'hotpink' | Name for pink marker |
| &nbsp; | &nbsp; | &nbsp; |
| frame | 'frame_no' | Name for frame number list |
| time | 'timestamp' | Name for timestamp list |
| size | 'size_px' | Name for marker size list |
| pos_x | 'position_px_x' | Name for pixel x position list |
| pos_y | 'position_px_y' | Name for pixel y position list |
| rx | 'rx' | Name for cm position list| 
| ry | 'ry' | Name for cm position list |
| vx | 'vx' | Name for cm/s velocity list |
| vy | 'vy' | Name for cm/s velocity list |
| ax | 'ax' | Name for cm/s^2 acceleration list |
| ay | 'ay' | Name for cm/s^2 acceleration list |

# Functions
Five functions are currently defined in `analyzer.py`. They allow the user
to find indexes matching specific patterns in data, manipulate strings, and
consolidate the raw CSV data into usable dictionaries and lists of floating
point numbers.

### fgt0(x, num_consecutive=10)
`fgt0` returns the first index in the array `x` where a minimum of `num_consecutive`
numbers in a row aren't 0. If the method fails to find an index, it returns 
`None`. This will ensure that you'll get a nice IndexError if this fails, so catch
that if you're expecting it. 

### fgtdx(a, x=0, dx=0.5, num_consecutive=10)
`fgtdx` returns the first index in the array `a` where the value is between 
`(x - dx) < value < (x + dx)` for num_consecutive numbers in a row. Like `fgt0`,
this method returns `None` on failure to find an index. 

### floatify(s, default=0)
`floatify` returns the floating-point value of the number represented in the
string `s`. If `s` is not a floating point number or `float(s)` otherwise fails, 
it will return `default`.

### lab_analyze(filename, start=1)
Returns a dictionary containing numpy arrays for the frame numbers, timestamps,
and dictionaries for all the markers in the data file supplied. The marker 
dictionaries contain numpy arrays for all the data belonging to that marker.
`filename` should be given as a string, not an opened file. `start` will rarely 
be at one. Data files should be checked in excel to find the right starting index.
Note that `start` coincides with the frame number, not the index in a list. 

Example: </br>
Imagine you want to get the data for the acceleration of the light orange
marker. The code to do this is:
````
my_lab = lab_analyze('lab_data.csv', 10)
light_orange_accel_x = my_lab[lorng][ax]
````

### lab_analyze_list(filename, start=1)
Exactly the same as `lab_analyze`, but does not use numpy arrays. Only returns
python dictionaries and python lists. Really just an outdated version of 
`lab_analyze`. 