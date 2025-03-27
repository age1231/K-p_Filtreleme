import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def generateBoundaries():
    max_bound = random.randint(16, 19)
    min_bound = random.randint(2, 5)
    return min_bound, max_bound

def generatePointCloud():
    return np.random.randint(0, 21, size=(15, 3))

def convertPCToDataFrame(pc):
    df = pd.DataFrame(pc, columns=["axis_1", "axis_2", "axis_3"])
    return df

def findIndicesOfInnerPoints(df, min_bound, max_bound):
    condition = (
        (df["axis_1"] >= min_bound) & (df["axis_1"] <= max_bound) &
        (df["axis_2"] >= min_bound) & (df["axis_2"] <= max_bound) &
        (df["axis_3"] >= min_bound) & (df["axis_3"] <= max_bound)
    )
    return df[condition].index.tolist()

def findPoints(df, inner_indices):
    inner_df = df.loc[inner_indices]
    outer_df = df.drop(inner_indices)
    inner_df.to_csv("örnek_veriler/inner.csv", sep='*', index=False)
    outer_df.to_csv("örnek_veriler/outer.csv", sep='*', index=False)

def plotFilteredPoints():
    inner_df = pd.read_csv("örnek_veriler/inner.csv", sep='*')
    outer_df = pd.read_csv("örnek_veriler/outer.csv", sep='*')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(inner_df["axis_1"], inner_df["axis_2"], inner_df["axis_3"], color='r', label='Inner Points')
    ax.scatter(outer_df["axis_1"], outer_df["axis_2"], outer_df["axis_3"], color='g', label='Outer Points')
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.legend()
    plt.savefig("plot.png")
    plt.show()

def main():
    random.seed(20)
    np.random.seed(20)
    min_bound, max_bound = generateBoundaries()
    print("Min Bound:", min_bound, "Max Bound:", max_bound)
    pc = generatePointCloud()
    df = convertPCToDataFrame(pc)
    inner_indices = findIndicesOfInnerPoints(df, min_bound, max_bound)
    findPoints(df, inner_indices)
    plotFilteredPoints()

main()
