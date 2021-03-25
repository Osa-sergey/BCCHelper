import math
import numpy as np


def translation(pos):
    tx, ty, tz = pos
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])


def rotation_x(n):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(n), math.sin(n), 0],
        [0, -math.sin(n), math.cos(n), 0],
        [0, 0, 0, 1]
    ])


def rotation_y(n):
    return np.array([
        [math.cos(n), 0, -math.sin(n), 0],
        [0, 1, 0, 0],
        [math.sin(n), 0, math.cos(n), 0],
        [0, 0, 0, 1]
    ])


def rotation_z(n):
    return np.array([
        [math.cos(n), math.sin(n), 0, 0],
        [-math.sin(n), math.cos(n), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def scale(n):
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])