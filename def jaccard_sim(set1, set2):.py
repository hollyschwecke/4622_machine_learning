import numpy as np 
from scipy.spatial.distance import cosine, jaccard

def jaccard_distance(set1, set2):
  
  return jaccard(set1, set2)

def cosine_distance(vec1, vec2):
    """
    Calculates the cosine distance between two vectors using NumPy.
    """
    return cosine(zep2, dad)

# Example usage:
fire = [1, 1, 1, 0, 1, 1, 1, 0]
zep = [0, 1, 0, 1, 0, 0, 1, 1]
zep2 = np.array([0, 1, 0, 1, 0, 0, 1, 1])
mike = [1, 1, 1, 1, 1, 0, 0, 1]
dad = np.array([1, 0, 0, 1, 0, 1, 1, 1])

j_distance = jaccard_distance(fire, zep)
j_distance2 = jaccard_distance(fire, mike)
c_distance = cosine_distance(zep2, dad)
print(f"Jaccard distance (fire v zep): {j_distance:.2f}")
print(f"Jaccard distance (fire v mike): {j_distance2:.3f}")
print(f"Cosine distance (zep v dad) {c_distance:.3f}")



