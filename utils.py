import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np


def degrees_to_radians(x):
    return x*2*np.pi/360

def sin(x):
    return np.sin(degrees_to_radians(x))

def cos(x):
    return np.cos(degrees_to_radians(x))

def tan(x):
    return np.tan(degrees_to_radians(x))

def cot(x):
    return 1/np.tan(degrees_to_radians(x))


def get_background_figure_sine(min_degree, max_degree):
    
    min_radian = degrees_to_radians(min_degree)
    max_radian = degrees_to_radians(max_degree)
    
    #x = np.linspace(min_degree, max_degree, 1001)
    x_radians = np.linspace(min_radian, max_radian, 1001)
    x_degrees = np.linspace(min_degree, max_degree, 1001)
    degrees_ticks_positions = np.arange(min_degree, max_degree, step=30)
    degrees_ticks = [str(degree) + '$^o$' for degree in degrees_ticks_positions]

    fig = plt.figure(figsize=(10, 4), tight_layout=True)
    gs = gridspec.GridSpec(1, 5)

    ax1 = fig.add_subplot(gs[0, 3:])
    ax1.plot(np.cos(x_radians), np.sin(x_radians), color = 'black', alpha = 0.7)
    ax1.grid(color='gray', alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)

    ax2 = fig.add_subplot(gs[0, :3])
    ax2.plot(x_degrees, sin(x_degrees), color='blue')
    ax2.grid(color='gray', alpha=0.3)
    ax2.set_xlabel('x')
    ax2.set_ylabel('sin(x)')
    ax2.set_xticks(degrees_ticks_positions, degrees_ticks)
    ax2.tick_params(axis='x', rotation=45)
    ax2.set_xlim(min_degree, max_degree)
    ax2.set_ylim(-1.1, 1.1)
    
    ax1.hlines(y=0, color='black', xmin=0, xmax = 1)
    ax1.hlines(y=0, color='gray', xmin=-1.1, xmax = 1.1, linestyles='dashed', alpha=0.5)
    ax1.vlines(x=0, color='gray', ymin=-1.1, ymax = 1.1, linestyles='dashed', alpha=0.5)
    ax2.hlines(y=0, color='gray', xmin=min_degree, xmax = max_degree, linestyles='dashed', alpha=0.5)

    return fig, ax1, ax2


def get_background_figure_cosine(min_degree, max_degree):
    
    min_radian = degrees_to_radians(min_degree)
    max_radian = degrees_to_radians(max_degree)
    
    #x = np.linspace(min_degree, max_degree, 1001)
    x_radians = np.linspace(min_radian, max_radian, 1001)
    x_degrees = np.linspace(min_degree, max_degree, 1001)
    degrees_ticks_positions = np.arange(min_degree, max_degree, step=30)
    degrees_ticks = [str(degree) + '$^o$' for degree in degrees_ticks_positions]

    fig = plt.figure(figsize=(6, 8), tight_layout=True)
    gs = gridspec.GridSpec(5, 2)

    ax1 = fig.add_subplot(gs[:2, 0])
    ax1.plot(np.cos(x_radians), np.sin(x_radians), color = 'black', alpha = 0.7)
    ax1.grid(color='gray', alpha=0.3)
    ax1.set_aspect('equal')
    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)

    ax2 = fig.add_subplot(gs[2:, 0])
    ax2.plot(cos(x_degrees), x_degrees, color='blue')
    ax2.grid(color='gray', alpha=0.3)
    ax2.set_xlabel('cos(x)')
    ax2.set_ylabel('x')
    ax2.set_yticks(degrees_ticks_positions, degrees_ticks)
    ax2.tick_params(axis='y', rotation=45)
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(min_degree, max_degree)
    
    ax1.hlines(y=0, color='black', xmin=0, xmax = 1)
    ax1.hlines(y=0, color='gray', xmin=-1.1, xmax = 1.1, linestyles='dashed', alpha=0.5)
    ax1.vlines(x=0, color='gray', ymin=-1.1, ymax = 1.1, linestyles='dashed', alpha=0.5)
    ax2.vlines(x=0, color='gray', ymin=min_degree, ymax = max_degree, linestyles='dashed', alpha=0.5)

    return fig, ax1, ax2


def draw_sine(degrees, min_degree=0, max_degree=360):
    
    x_pos = cos(degrees)
    y_pos = sin(degrees)
    
    fig, ax1, ax2 = get_background_figure_sine(min_degree, max_degree)
    ax1.plot([0, x_pos], [0, y_pos], color='black', linewidth=2)
    ax1.plot([x_pos, x_pos], [0, y_pos], color='red', linewidth=2)
    ax1.text(0.15, 0, str(degrees) + "$^o$", size=12, ha='left', va='bottom')
    ax2.scatter([degrees], [y_pos], color='red', s=30, label= f"x={degrees}" + "$^o$" + f"\nsin({degrees})={y_pos:.2f}")
    ax2.legend(loc='upper left' if min_degree<0 else 'lower left')
    
    ax1.hlines(y=y_pos, color='purple', xmin=-1.1, xmax = 1.1, linestyles='dashed', alpha=0.5)
    ax2.hlines(y=y_pos, color='purple', xmin=min_degree, xmax = max_degree, linestyles='dashed', alpha=0.5)
    ax2.vlines(x=degrees, color='purple', ymin=min(0, y_pos), ymax = max(y_pos, 0), linestyles='dashed', alpha=0.5)

    tt = np.linspace(0, degrees, 1001)
    ax1.plot(0.5*cos(tt), 0.5*sin(tt), color = 'black', alpha = 0.7)

    
def draw_cosine(degrees, min_degree=0, max_degree=360):
    
    x_pos = cos(degrees)
    y_pos = sin(degrees)
    
    fig, ax1, ax2 = get_background_figure_cosine(min_degree, max_degree)
    ax1.plot([0, x_pos], [0, y_pos], color='black', linewidth=2)
    ax1.plot([0, x_pos], [0, 0], color='red', linewidth=2)
    ax1.text(0.15, 0, str(degrees) + "$^o$", size=12, ha='left', va='bottom')
    ax2.scatter([x_pos], [degrees], color='red', s=30, label= f"x={degrees}" + "$^o$" + f"\ncos({degrees})={x_pos:.2f}")
    ax2.legend(loc='lower right' if min_degree<0 else 'upper right')
    
    ax1.vlines(x=x_pos, color='purple', ymin=-1.1, ymax = 1.1, linestyles='dashed', alpha=0.5)
    ax2.vlines(x=x_pos, color='purple', ymin=min_degree, ymax = max_degree, linestyles='dashed', alpha=0.5)
    ax2.hlines(y=degrees, color='purple', xmin=min(0, x_pos), xmax = max(0, x_pos), linestyles='dashed', alpha=0.5)

    tt = np.linspace(0, degrees, 1001)
    ax1.plot(0.5*cos(tt), 0.5*sin(tt), color = 'black', alpha = 0.7)

    
    
def get_info_graphics():

    x = np.linspace(-np.pi, np.pi, 1001)
    x_pos = 0.5
    y_pos = 0.866


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (11, 5))

    ax1.plot([0, x_pos], [0, 0], color='green', linewidth=2)
    ax1.plot([0, x_pos], [0, y_pos], color='red', linewidth=2)
    ax1.plot([x_pos, x_pos], [0, y_pos], color='blue', linewidth=2)

    ax1.text(x_pos/2 - 0.1, 0+0.05, "adjacent", size=15, ha='left', va='bottom', color='green')
    ax1.text(x_pos - 0.1, y_pos/2, "opposite", size=15, ha='left', va='center', rotation=90, color='blue')
    ax1.text(x_pos/2 - 0.1, y_pos/2, "hypotemuse", size=15, ha='left', va='bottom', rotation=60, color='red')
    ax1.axis('off')

    ax2.plot(np.cos(x), np.sin(x), color = 'black', alpha = 0.7)
    ax2.plot([0, x_pos], [0, 0], color='green', linewidth=2)
    ax2.plot([0, x_pos], [0, y_pos], color='red', linewidth=2)
    ax2.plot([x_pos, x_pos], [0, y_pos], color='blue', linewidth=2)

    ax2.vlines(x=0, color='gray', ymin=-1.1, ymax = 1.1, linestyles='dashed', alpha=0.5)
    ax2.hlines(y=0, color='gray', xmin=-1.1, xmax = 1.1, linestyles='dashed', alpha=0.5)
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-1.1, 1.1)
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid('gray', alpha=0.2)

    degrees = np.arcsin(y_pos)
    tt = np.linspace(0, degrees, 1001)
    ax2.plot(0.25*np.cos(tt), 0.25*np.sin(tt), color = 'black', alpha = 0.7)
    ax2.text(0.1, 0.1, "$\phi$", size=12, ha='left', va='center')
    ax2.text(x_pos/2 - 0.1, y_pos/2, "r=1", size=12, ha='left', va='bottom', rotation=60)
    ax2.text(0.2, -0.2, "$cos(\phi)$", size=12, ha='left', va='bottom')
    ax2.text(0.55, 0.4, "$sin(\phi)$", size=12, ha='left', va='center')

    ax1.set_aspect('equal')
    ax2.set_aspect('equal')