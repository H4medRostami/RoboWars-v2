import random
# random used for shuffle first location of players in game start.
from BotClass import WarRobot
# BotClass module contain Base class attribute and methods


# check sum of ability entry
def input_sum_check(robot: str, a: int, d: int, s: int) -> None:
    if a+d+s > 10 or a+d+s < 10:
        print("sum of numbers must be 10 , Please enter it again: ")
        get_input(robot)


# shuffle first location
first_position = [0, 19]
random.shuffle(first_position)


# first input that get entry for robots ability from user except location that set random
def get_input(robot: str) -> int:
    try:
        a = input("Enter ordinary Attack " + robot + ":")
        print("Attack:", a)
        d = input("Enter ordinary Defense " + robot + ":")
        print("Defense:", d)
        s = input("Enter ordinary Speed " + robot + ":")
        print("Speed:", s)
        a = int(a)
        d = int(d)
        s = int(s)
        input_sum_check(robot, a, d, s)
        return a, d, s
    except ValueError:
        print("give only number and right value!\n")
        get_input(robot)
    except TypeError:
        print("can not assign None value!\n")
        get_input(robot)


R1Result = get_input('r1')
r1 = WarRobot('r1', None, R1Result[0], R1Result[1], R1Result[2], first_position.pop())

R2Result = get_input('r2')
r2 = WarRobot('r2', r1, R2Result[0], R2Result[1], R2Result[2], first_position.pop())
r1.enemy = r2

print('''\n\n⚐⚐⚐Game Start⚐⚐⚐\n\n  instruction:\n\n * press 1 #steps and go ahead \n 
 * press 2 #shot missile to enemy\n * other key scape \n''')


# joy steak get action of robot from user
def JoySteak(action: int, usr: obj) -> None:
    if action == 1:
        print(usr.move())
    elif action == 2:
        usr.shot()


# general energy and location status
def get_status() -> None:
    print("-------------------------------------")
    print("⚡R1 energy status:{}       ⚡R2 energy status:{} ".format(r1.energy, r2.energy))

    print("⭐R1 Current Location:{}      ⭐R2 Current Location:{} ".format(r1.location, r2.location))
    print("-------------------------------------")


# get user entry action and show status of energy and location
while True:

    r1_input = input("Hi r1 \n Please type your action: ")
    JoySteak1 = int(r1_input)
    JoySteak(JoySteak1, r1)

    r2_input = input("Hi r2 \n Please type your action: ")
    JoySteak2 = int(r2_input)
    JoySteak(JoySteak2, r2)
    get_status()




