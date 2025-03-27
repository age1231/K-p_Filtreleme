import random

def initializeVectors(v):
    v.append(random.randint(2, 8))
    v.append(random.randint(2, 8))

def dotProduct(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def orthogonalization(v1, v2):
    scale = dotProduct(v1, v2) / dotProduct(v1, v1)
    v2_orth = [v2[0] - v1[0]*scale, v2[1] - v1[1]*scale]
    return v2_orth

def check(v1, v2_orth):
    return abs(dotProduct(v1, v2_orth)) < 1e-6

def main():
    random.seed(10)
    v1, v2 = [], []
    initializeVectors(v1)
    initializeVectors(v2)
    print("Initial vectors:")
    print("v1:", v1)
    print("v2:", v2)

    dot = dotProduct(v1, v2)
    print("Dot product:", dot)

    v2_orth = orthogonalization(v1, v2)
    print("v2 orthogonalized:", v2_orth)

    status = check(v1, v2_orth)
    print("Orthogonalization successful?", status)

main()
