import numpy as np

class ProjectionMatrix:
    """
    Handles the mapping from 7D state space to 4D Minkowski brane.
    Uses a 4x7 matrix to collapse higher-dimensional data.
    """
    def __init__(self): # Note the double underscores here
        # Initial projection matrix based on 7D-4D orthogonality
        # This will be refined as we define the Minkowski curvature constants
        self.matrix = np.array([
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0]
        ], dtype=float)

    def apply(self, vector_7d):
        return np.dot(self.matrix, vector_7d)
      
