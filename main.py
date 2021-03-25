import render as r

import numpy as np


def add_bounds(point,dist = 5) -> np.array:
    x, y, z = point
    return np.array([[(x, y, z, 1), (dist, y, z, 1), (dist, 0, z, 1), (x, 0, z, 1)],
                     [(x, y, z, 1), (dist, y, z, 1), (dist, y, dist, 1), (x, y, dist, 1)],
                     [(x, y, z, 1), (x, y, dist, 1), (x, 0, dist, 1), (x, 0, z, 1)]])


def create_bounds(points) -> np.array:
    vertexes = add_bounds(np.squeeze(points[:1]))
    for point in enumerate(points):
        if not(point[0] == 0):
            vertexes = np.append(vertexes, add_bounds(point[1]), axis=0)
    return vertexes


squares = create_bounds(np.array([[1, 2, 3], [2, 3, 4], [1.5, 2.5, 2]]))
app = r.Render(squares)
app.run()
