# src/core/octonion.py
import numpy as np

class Octonion:
    """
    Implements the 8-dimensional division algebra.
    The Fano Plane multiplication rules define the G2 symmetry space.
    """
    
    # Normalized Fano Plane lookup: { (i, j): (k, sign) }
    # Rules: (1,2,3), (1,4,5), (1,6,7), (2,4,6), (2,5,7), (3,4,7), (3,6,5)
    # Triplet (i, j, k) implies i*j = k, j*k = i, k*i = j (all +1)
    # Reversing order gives -1 (e.g., j*i = -k)
    TABLE = {
        # (1, 2, 3)
        (1, 2): (3, 1), (2, 1): (3, -1),
        (2, 3): (1, 1), (3, 2): (1, -1),
        (3, 1): (2, 1), (1, 3): (2, -1),
        # (1, 4, 5)
        (1, 4): (5, 1), (4, 1): (5, -1),
        (4, 5): (1, 1), (5, 4): (1, -1),
        (5, 1): (4, 1), (1, 5): (4, -1),
        # (1, 6, 7)
        (1, 6): (7, 1), (6, 1): (7, -1),
        (6, 7): (1, 1), (7, 6): (1, -1),
        (7, 1): (6, 1), (1, 7): (6, -1),
        # (2, 4, 6)
        (2, 4): (6, 1), (4, 2): (6, -1),
        (4, 6): (2, 1), (6, 4): (2, -1),
        (6, 2): (4, 1), (2, 6): (4, -1),
        # (2, 5, 7)
        (2, 5): (7, 1), (5, 2): (7, -1),
        (5, 7): (2, 1), (7, 5): (2, -1),
        (7, 2): (5, 1), (2, 7): (5, -1),
        # (3, 4, 7)
        (3, 4): (7, 1), (4, 3): (7, -1),
        (4, 7): (3, 1), (7, 4): (3, -1),
        (7, 3): (4, 1), (3, 7): (4, -1),
        # (3, 6, 5)
        (3, 6): (5, 1), (6, 3): (5, -1),
        (6, 5): (3, 1), (5, 6): (3, -1),
        (5, 3): (6, 1), (3, 5): (6, -1)
    }

    def __init__(self, components):
        # components: [real, e1, e2, e3, e4, e5, e6, e7]
        self.v = np.array(components, dtype=float)

    @classmethod
    def multiply(cls, o1, o2):
        res = np.zeros(8)
        
        # Real part
        res[0] = o1.v[0]*o2.v[0] - np.dot(o1.v[1:], o2.v[1:])
        
        # Imaginary parts
        res[1:] = o1.v[0]*o2.v[1:] + o2.v[0]*o1.v[1:]
        
        # Cross products (Fano Plane interactions)
        for i in range(1, 8):
            for j in range(1, 8):
                if i != j and (i, j) in cls.TABLE:
                    k, sign = cls.TABLE[(i, j)]
                    res[k] += sign * o1.v[i] * o2.v[j]
        
        return Octonion(res)
      
