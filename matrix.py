import numpy as np
from cogwheel.config import getLogger
l=getLogger("Crystal-AI 2.0b r4173")
points_original = np.array([[100.0, 200.0], [150.0, 250.0], [200.0, 300.0]])
points_transformed = np.array([[110.0, 210.0], [160.0, 260.0], [210.0, 310.0]])

points_original = np.hstack([points_original, np.ones((3, 1))])
transformation_matrix, _, _, _ = np.linalg.lstsq(points_original, points_transformed, rcond=None)
transformation_matrix = transformation_matrix.T
l.info(points_original)

def transform_point(point, matrix):
    x, y = point
    l.info("Transforming:{},{}".format(x,y))
    point_vector = np.array([x, y, 1.0])
    transformed_point = np.dot(matrix, point_vector)
    return transformed_point[:2]

ix, iy = 120.0, 220.0

transformed_point = transform_point((ix, iy), transformation_matrix)

print("Transformed Point:", transformed_point)


import numpy as np

points_original = np.array([[100.0, 200.0], [150.0, 250.0], [200.0, 300.0]])
theta = np.radians(30)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])
print("-- T Matrix --")
print(rotation_matrix)

points_rotated = np.dot(np.hstack([points_original, np.ones((3, 1))]), rotation_matrix.T)
points_rotated = points_rotated[:, :2]

points_original_homogeneous = np.hstack([points_original, np.ones((3, 1))])
transformation_matrix = np.linalg.lstsq(points_original_homogeneous, points_rotated, rcond=None)[0].T

def transform_point(point, matrix):
    x, y = point
    point_vector = np.array([x, y, 1.0])
    transformed_point = np.dot(matrix, point_vector)
    return transformed_point[:2]

ix, iy = 120.0, 220.0
transformed_point = transform_point((ix, iy), transformation_matrix)

print("Transformed Point:", transformed_point)
