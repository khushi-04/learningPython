import random
import numpy as np

def is_it_there(arr: list, value: int):
    boole = False
    for item in arr:
        for items in item:
            if value == items:
                boole = True
    return boole

def solution():
    rows = 3
    columns = 3

    oned_array = np.arange(1,10)
    oned_array = np.random.choice(oned_array, size=9, replace=False)
    box1 = oned_array.reshape((3,3))

    box2 = [[0]*columns]*rows
    box3 = []
    box4 = []

    for i,items in enumerate(box2):
        for j,item in enumerate(items):
            num = random.randint(1,9)
            
            while is_it_there(box2,num) == True or is_it_there(box1[i],num):
                print(num)
                num = random.randint(1,9)
            box2[i][j] = num
    print(box1)
    print(box2)


if __name__ == "__main__":
    print("test")
    solution()



