from random import randint
import numpy as np

def is_it_there(arr, value: int):
    for item in arr:
        if value == item:
            return True
    return False

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
    box5 = [0,0,0,0,0,0,0,0,0]
    box6 = [0,0,0,0,0,0,0,0,0]
    box7 = [0,0,0,0,0,0,0,0,0]
    box8 = [0,0,0,0,0,0,0,0,0]
    box9 = [0,0,0,0,0,0,0,0,0]
    
    # initializing box2
    trackindex = 0
    box2 = np.array(box2)
    for i in range(0,len(box2)):
        num = randint(1,9)
        while is_it_there(box2,num) == True or num in box1[trackindex,:]:
            num = randint(1,9)
        if i == 2 or i == 5:
            trackindex+=1
        box2[i] = num
    print(box2)
    
    box2 = box2.reshape((3,3))

    # initializing box3
    # trackindex = 0
    # for i,items in enumerate(box3):
    #     num = randint(1,9)
    #     while is_it_there(box3,num) == True or num in box1[trackindex,:] or num in box2[trackindex,:]:
    #         num = randint(1,9)
    #     box3[i] = num
    #     if i == 2 or i == 5:
    #         trackindex+=1
    box3 = np.array(box3)
    box3 = box3.reshape((3,3))

    # initializing box4
    # trackindex = 0
    # for i,items in enumerate(box4):
    #     num = randint(1,9)
    #     while is_it_there(box4,num) == True or num in box1[:,trackindex]:
    #         num = randint(1,9)
    #     box4[i] = num
    #     if i == 2 or i == 5:
    #         trackindex = 0
    #     else:
    #         trackindex+=1
    box4 = np.array(box4)
    box4 = box4.reshape((3,3))

    # initializing box5
    # trackrows = 0
    # trackcols = 0
    # for i,items in enumerate(box5):
    #     num = randint(1,9)
    #     while is_it_there(box5,num) == True or num in box2[:,trackcols] or num in box4[trackrows,:]:
    #         num = randint(1,9)
    #     box5[i] = num
    #     if i == 2 or i == 5:
    #         trackrows+= 1
    #         trackcols = 0
    #     else:
    #         trackcols+=1
    box5 = np.array(box5)
    box5 = box5.reshape((3,3))

    # initializing box6
    # trackrows = 0
    # trackcols = 0
    # for i,items in enumerate(box6):
    #     num = randint(1,9)
    #     while is_it_there(box6,num) == True or num in box3[:,trackcols] or num in box4[trackrows,:] or num in box5[trackrows,:]:
    #         num = randint(1,9)
    #     box6[i] = num
    #     if i == 2 or i == 5:
    #         trackrows+= 1
    #         trackcols = 0
    #     else:
    #         trackcols+=1
    box6 = np.array(box6)
    box6 = box6.reshape((3,3))

    # initializing box7
    # trackindex = 0
    # for i,items in enumerate(box7):
    #     num = randint(1,9)
    #     while is_it_there(box7,num) == True or num in box1[:,trackindex] or num in box4[:,trackindex]:
    #         num = randint(1,9)
    #     box7[i] = num
    #     if i == 2 or i == 5:
    #         trackindex = 0
    #     else:
    #         trackindex+=1
    box7 = np.array(box7)
    box7 = box7.reshape((3,3))

    # initializing box 8
    # trackrows = 0
    # trackcols = 0
    # for i,items in enumerate(box8):
    #     num = randint(1,9)
    #     while is_it_there(box8,num) == True or num in box2[:,trackcols] or num in box5[:,trackcols] or num in box7[trackrows,:]:
    #         num = randint(1,9)
    #     box8[i] = num
    #     if i == 2 or i == 5:
    #         trackrows+= 1
    #         trackcols = 0
    #     else:
    #         trackcols+=1
    box8 = np.array(box8)
    box8 = box8.reshape((3,3))

    # initializing box 9
    # trackrows = 0
    # trackcols = 0
    # for i,items in enumerate(box9):
    #     num = randint(1,9)
    #     while is_it_there(box9,num) == True or num in box3[:,trackcols] or num in box6[:,trackcols] or num in box7[trackrows,:] or num in box8[trackrows,:]:
    #         num = randint(1,9)
    #     box9[i] = num
    #     if i == 2 or i == 5:
    #         trackrows+= 1
    #         trackcols = 0
    #     else:
    #         trackcols+=1
    box9 = np.array(box9)
    box9 = box9.reshape((3,3))

    row1 = np.hstack((box1, box2,box3))
    row2 = np.hstack((box4,box5,box6))
    row3 = np.hstack((box7,box8,box9))
    stack1 = np.vstack((row1,row2))
    main_stack = np.vstack((stack1,row3))
    return main_stack

def new_game():
    main_stack = solution()
    return ""

if __name__ == "__main__":

    print("Hello, welcome to Sudoku! In this game, I will give you a sudoku grid (9x9).")
    cont = input("Type 'Y' to begin and 'N' to quit: ")
    while cont != "N" and cont != "n":
        print("Instructions:")
        print("To input an answer to an empty slot, the game will first ask for which slot (type 'row column' from 1-9 for each). Then you can type in your answer!")
        print("You get three lives, and if you guess incorrectly three times, the game is over. You can always play another game!")
        print(" ")
        new_game()

        
        cont = input("Type 'Y' to play again and 'N' to quit: ")

    print("Thank you for playing. Have a good day!")
    # solution()
