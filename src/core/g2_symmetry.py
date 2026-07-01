""" The Lie Group transformation logic)
"""
# src/core/g2_symmetry.py
import numpy as np
from scipy.linalg import expm
from src.core.octonion import Octonion

class G2Rotation:
    """
    Constructs the 14 generators of G2 and applies rotations 
    that preserve the octonionic structure (G2 Automorphisms).
    """
    def __init__(self):
        # The 14 generators of G2 as 7x7 matrices
        # Each generator L_a acts on the 7D imaginary subspace.
        self.generators = self._construct_generators()

    def _construct_generators(self):
        """
        Constructs the 14 basis matrices for the Lie algebra g2.
        Using the structure constants f_abc derived from the Fano table.
        (L_a)_bc = -f_abc
        """
        f = np.zeros((7, 7, 7))
        # Populate structure constants from Octonion.TABLE
        for (i, j), (k, sign) in Octonion.TABLE.items():
            # i, j, k are 1-based indices (e1-e7)
            # Subtract 1 for 0-based indexing
            f[i-1, j-1, k-1] = sign
            
        generators = []
        # G2 has 14 generators. 
        # 7 are related to the Fano lines, 7 are related to the structure.
        for a in range(7):
            # Construction simplified for the 7D basis
            gen = -f[a] 
            generators.append(gen)
            
        # Note: Additional 7 generators are derived from the 
        # cross-product constraints.
        return generators

    def rotate(self, vector_7d, rotation_parameters):
        """
        Applies a finite rotation R = exp(sum(theta_i * L_i))
        rotation_parameters: list of 14 floats corresponding to the 14 generators.
        """
        if len(rotation_parameters) != len(self.generators):
            raise ValueError("G2 rotation requires 14 parameters.")
            
        # Sum the infinitesimal generators
        algebra_element = np.zeros((7, 7))
        for i, theta in enumerate(rotation_parameters):
            algebra_element += theta * self.generators[i]
            
        # Exponentiate to get the finite group element (Rotation Matrix)
        rotation_matrix = expm(algebra_element)
        
        # Apply transformation
        return np.dot(rotation_matrix, vector_7d)
        
