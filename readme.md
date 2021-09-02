# Getting Started

**Language:** Python

# Requirements

- python3
- python3-venv
- numpy

# Compilation & Execution Instructions

This code has been tested with Python 3.8.5 on Ubuntu 20.04.2 LTS.
<br><br>
This may require installing the `venv` module using

```
sudo apt-get install python3-venv
```

Create a folder for the virtual environment using

```
mkdir venv
```

Instantiate a virtual environment using

```
python3 -m venv venv
```

Activate the virtual environment using

```
. venv/bin/activate
```

Install numpy in the virtual environment using

```
pip3 install numpy
```

To run the program, invoke it with

```
python3 semester-project.py <path>/<to>/<data>/<file>
python3 semester-project.py <path>/<to>/<data>/<file> interpolation
python3 semester-project.py <path>/<to>/<data>/<file> least-squares
```

<br>
Running with

```
python3 semester-project.py data/sensors-2018.12.26-no-labels.txt interpolation
```

Should result in 4 output files should be generated in a folder named `output`.
<br>
The output file names follow the format `{basename}`-core-`{core_number}`.txt

Running

```
less output/sensors-2018.12.26-no-labels-core-0.txt
```

on the output file should display something similar to

```
        0 <= x <        30; y_0     =         61.0000 +          0.6333x; interpolation
       30 <= x <        60; y_1     =         98.0000 +         -0.6000x; interpolation
       60 <= x <        90; y_2     =         20.0000 +          0.7000x; interpolation
       90 <= x <       120; y_3     =        128.0000 +         -0.5000x; interpolation
      120 <= x <       150; y_4     =         12.0000 +          0.4667x; interpolation
      150 <= x <       180; y_5     =        112.0000 +         -0.2000x; interpolation
      180 <= x <       210; y_6     =         34.0000 +          0.2333x; interpolation
      210 <= x <       240; y_7     =        146.0000 +         -0.3000x; interpolation
      240 <= x <       270; y_8     =          2.0000 +          0.3000x; interpolation
      270 <= x <       300; y_9     =        137.0000 +         -0.2000x; interpolation
      300 <= x <       330; y_10    =        197.0000 +         -0.4000x; interpolation
      330 <= x <       360; y_11    =        -78.0000 +          0.4333x; interpolation
      360 <= x <       390; y_12    =        222.0000 +         -0.4000x; interpolation
      390 <= x <       420; y_13    =         79.0000 +         -0.0333x; interpolation
      420 <= x <       450; y_14    =       -215.0000 +          0.6667x; interpolation
      450 <= x <       480; y_15    =         85.0000 +          0.0000x; interpolation
      480 <= x <       510; y_16    =        389.0000 +         -0.6333x; interpolation
      510 <= x <       540; y_17    =        151.0000 +         -0.1667x; interpolation
      540 <= x <       570; y_18    =       -353.0000 +          0.7667x; interpolation
      570 <= x <       600; y_19    =        445.0000 +         -0.6333x; interpolation
      600 <= x <       630; y_20    =         45.0000 +          0.0333x; interpolation
      630 <= x <       660; y_21    =         87.0000 +         -0.0333x; interpolation
      660 <= x <       690; y_22    =       -375.0000 +          0.6667x; interpolation
      690 <= x <       720; y_23    =         85.0000 +          0.0000x; interpolation
      720 <= x <       750; y_24    =        541.0000 +         -0.6333x; interpolation
```

Following a similar method and running with

```
python3 semester-project.py data/sensors-2018.12.26-no-labels.txt least-squares
```

should result in output similar to

```
        0 <= x <     35610; y_0     =         77.1459 +         -0.0001x; least-squares
```
