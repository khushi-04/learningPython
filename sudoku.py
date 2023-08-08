import random
import numpy as np

def solution():
    # rows = 3
    # columns = 3

    oned_array = np.arange(1,10)
    oned_array = np.random.choice(oned_array, size=9, replace=False)
    box1 = oned_array.reshape((3,3))

    box2 = []
    box3 = []
    box4 = []

    for i,items in enumerate(box2):
        for j,item in enumerate(items):
            num = random.randint(1,9)
            while num in box2 or num in box1[i]:
                print(num)
                num = random.randint(1,9)
            box2[i][j] = num
    print(box1)
    print(box2)


if __name__ == "__main__":
    print("test")
    solution()



