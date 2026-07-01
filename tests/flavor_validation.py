"""The "Proof of Intuition" suite: does this rotation match quark properties?"""
# tests/flavor_validation.py
import unittest
import numpy as np
from src.core.projection_matrix import ProjectionMatrix
from src.core.g2_symmetry import G2Rotation

class TestFlavorRotation(unittest.TestCase):
    def setUp(self):
        self.rotator = G2Rotation()
        self.projector = ProjectionMatrix()
        
        # Initial 'Down' quark state in 7D (Simplified knot vector)
        self.down_quark_knot = np.array([0.0, 0.7, 0.1, 0.1, 0.1, 0.1, 0.1])
        
        # The expected 'Up' quark projection magnitude
        # (This constant will be refined as we define our brane constants)
        self.expected_up_magnitude = 0.85 

    def test_flavor_mutation(self):
        """
        Verify if a G2-constrained rotation can map a 'Down' quark
        to an 'Up' quark projection.
        """
        # We need 14 parameters for a full G2 rotation
        # We start with a small rotation perturbation
        rotation_angles = np.array([0.01] * 14) 
        
        # 1. Apply G2 rotation
        rotated_knot = self.rotator.rotate(self.down_quark_knot, rotation_angles)
        
        # 2. Project onto 4D Minkowski brane
        projected_4d = self.projector.apply(rotated_knot)
        
        # 3. Calculate magnitude
        current_magnitude = np.linalg.norm(projected_4d)
        
        # Validation: Does the new projection match the Up quark signature?
        # Using a tolerance for the geometric approximation
        print(f"Resulting projection magnitude: {current_magnitude}")
        self.assertAlmostEqual(current_magnitude, self.expected_up_magnitude, delta=0.05)

if __name__ == '__main__':
    unittest.main()
  
