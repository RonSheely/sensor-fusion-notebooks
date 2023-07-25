# Michael P. Hayes UCECE, Copyright 2018--2022
import numpy as np
from ipywidgets import interact
from matplotlib.pyplot import subplots
from .lib.robot import robot_draw, Robot
from .lib.pose import Pose


def velocity_motion_model_demo1_plot(x0=3, y0=1, heading0=90,
                                     v=1, omega=0, steps=0):

    x = np.zeros(steps + 1)
    y = np.zeros(steps + 1)
    theta = np.zeros(steps + 1)

    robot = Robot(x0, y0, heading=np.radians(heading0))

    for m in range(steps + 1):
        x[m] = robot.x
        y[m] = robot.y
        theta[m] = robot.heading
        robot.transition(v, np.radians(omega), dt=1)

    fig, ax = subplots(figsize=(10, 5))
    Pose(0, 0, 0).draw_axes(ax)
    Pose(x0, y0, np.radians(heading0)).draw_axes(ax, linestyle=':')

    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 5)
    ax.grid(True)

    for m in range(len(x)):
        colour = ['red', 'orange', 'green', 'blue', 'magenta'][m % 5]
        robot_draw(ax, x[m], y[m], theta[m], colour=colour)


def velocity_motion_model_demo1():
    interact(velocity_motion_model_demo1_plot,
             x0=(-4, 4, 0.5),
             y0=(-4, 4, 0.5),
             heading0=(0, 180, 15),
             v=(0, 2, 0.1),
             omega=(-60, 60, 15),
             steps=(0, 10),
             heading=(0, 180, 15),
             continuous_update=False)
