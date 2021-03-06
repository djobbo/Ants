import numpy as np
from math import sin, cos, floor


def create_circle(canvas, x, y, r, color, **kwargs):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=color, **kwargs)


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f'#{floor(r):02x}{floor(g):02x}{floor(b):02x}'


def vect_rot(vect, angle):
    rot = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
    return np.dot(rot, vect)


def distance(v, w):
    return np.linalg.norm(w - v)


def angle(v, w):
    return np.arccos(v.dot(w) / (np.linalg.norm(v) * np.linalg.norm(w)))


def rotate(v, angle):
    r = np.array(([np.cos(angle), -np.sin(angle)],
                 [np.sin(angle), np.cos(angle)]))
    return r.dot(v)


def random_inside_circle():
    length = np.sqrt(np.random.uniform(0, 1))
    angle = np.pi * np.random.uniform(0, 2)

    return np.array([length * np.cos(angle), length * np.sin(angle)])
