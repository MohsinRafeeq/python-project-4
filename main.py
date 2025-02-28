print('''
 ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88                                             
''')
print("Welcome to Treasure land.")

print("your mission is to find the Treasure.")

choice1 =input("you are at a cross road. where do you want to go ? type 'left' or 'right'\n").lower()

if choice1 == "left":
     choice2 = input(
         "you\'ve come to a lake.There is an island in middle of the lake.type'wait' to wait for a boat.type 'swim' to swim across. \n ").lower()
     if choice2 =="wait":
        choice3 =input(
            "your arrive at the island unharmed.there is a house with 3 doors.one red,one yellow,and one blue.which color do you choose?\n").lower()
        if choice3 == "red":
            print("it's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("you found the treasure. you win!")
        elif choice3 == "blue":
            print("you enter a room of beasts.Game Over!")
        else:
            print("you choose a door that doesn't exits.Game Over!")
     else:
        print("you get attacked by an angry trout.Game Over.")

else:
    print("you fell into a hole.Game Over!")
        

