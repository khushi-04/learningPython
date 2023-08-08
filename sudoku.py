import random
import numpy as np

def is_it_there(arr, value: int):
    boole = False
    for item in arr:
        if value == item:
            boole = True
    return boole

def solution():
    rows = 3
    columns = 3
    # initializing box1
    oned_array = np.arange(1,10)
    oned_array = np.random.choice(oned_array, size=9, replace=False)
    box1 = oned_array.reshape((3,3))

    box2 = [0,0,0,0,0,0,0,0,0]
    box3 = [0,0,0,0,0,0,0,0,0]
    box4 = [0,0,0,0,0,0,0,0,0]

    # initializing box2
    trackindex = 0
    for i,items in enumerate(box2):
        num = random.randint(1,9)
        while is_it_there(box2,num) == True or num in box1[trackindex,:]:
            num = random.randint(1,9)
        box2[i] = num
        if i == 2 or i == 5:
            trackindex+=1
    box2 = np.array(box2)
    box2 = box2.reshape((3,3))

    # initializing box3
    trackindex = 0
    for i,items in enumerate(box3):
        num = random.randint(1,9)
        while is_it_there(box3,num) == True or num in box1[:,trackindex]:
            num = random.randint(1,9)
        box3[i] = num
        if i == 2 or i == 5:
            trackindex = 0
        else:
            trackindex+=1
    box3 = np.array(box3)
    box3 = box3.reshape((3,3))

    trackrows = 0
    trackcols = 0
    for i,items in enumerate(box4):
        num = random.randint(1,9)
        while is_it_there(box4,num) == True or num in box2[:,trackcols] or num in box3[trackrows,:]:
            num = random.randint(1,9)
        box4[i] = num
        if i == 2 or i == 5:
            trackrows+= 1
            trackcols = 0
        else:
            trackcols+=1
    box4 = np.array(box4)
    box4 = box4.reshape((3,3))

    print(np.hstack((box1, box2)))
    print(np.hstack((box3,box4)))
    print(box1)
    print(box2)
    print(box3)
    print(box4)

if __name__ == "__main__":
    solution()