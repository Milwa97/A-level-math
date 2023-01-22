# About this project


This repository contains post-elementary math course in form of interactive notebooks. The goal of this course is to deepen understanding of mathematics and develop mathematical intuition based on visual representations of more abstract objects. The level of the course is aligned to the Polish maturity exam and overlaps with AS/A level.

# Table of content

1. Linear function
2. Quadratic function
3. Cubic, quartic and reciprocal functions
4. Exponential and logarithmic functions (release: 15.01.2023)
5. Trigonometric functions (release: 22.01.2023)
7. Vectors in 2D (release: 29.01.2023)
8. Vectors in 3D (release: 05.02.2023)


# How to run?

This project is written in python 3.10. The required libraries include, but are note limited to: numpy, sympy, pandas, matplotlib and seaborn. All necessary libraries are listed in requirements.txt file.

#### Instruction for Windows:

1. Download Python 3.10 from: [https://www.python.org/psf-landing/](https://www.python.org/psf-landing/) and install it

2. Clone this repository (using git terminal):

```
git clone https://github.com/Milwa97/A-level-math.git
```

or download zip file from: [https://github.com/Milwa97/A-level-math.git](https://github.com/Milwa97/A-level-math.git) and unpack

3. Open Windows terminal  in the repository folded and create a virtual environment via typing: 
```
python3 -m venv path\to\venv
```

4. Activate the virtual environment:

```
path\to\venv\Scripts\activate

```

5. Install python packages from requirements.txt:
```
pip install -r requirements.txt
```

6. Run jupyter notebook:
```
jupyter notebook
```

#### Instruction for Linux:
If You are a linux user, most probably Ypu can copy repository and create virtual environment without any instructions :P 

1. Clone this repository (using git terminal):

```
git clone https://github.com/Milwa97/A-level-math.git
```

or download zip file from: [https://github.com/Milwa97/A-level-math.git](https://github.com/Milwa97/A-level-math.git) and unpack

2. Open terminal in the repository folded and check, if You have pip and virtualenv installed:

```
$ pip --version
$ virtualenv --version
```

if not, install pip and virtualenv:

```
$ sudo apt-get install python-pip
$ pip install virtualenv
```

3. Create a virtual environment via typing: 

```
$ virtualenv virtualenv_name
```

4. Activate the virtual environment:

```
$ source virtualenv_name/bin/activate
```

5. Install python packages from requirements.txt:
```
pip install -r requirements.txt
```

6. Run jupyter notebook:
```
jupyter notebook
```

If You want to enable interactive graphics (better option, but may require installing manually some dependencies according to this instruction:
[Render interactive plots with matplotlib](https://towardsdatascience.com/render-interactive-plots-with-matplotlib-2cf0918d89c9), use:
```
%matplotlib widget
```

For static graphics use (safe, always working option):
```
%matplotlib inline
```
Comment or delete option that You don't use.
