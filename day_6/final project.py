'''Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

What you need to know
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).
'''


from turtle import right


def right_is_not_clear():
    if right_is_clear() != True:
        return True


def turn_rigth():
    turn_left()
    turn_left()
    turn_left()


def move_with_rigth_wall():
    while front_is_clear() and right_is_not_clear():
        move()


def not_way():
    if wall_in_front() and right_is_not_clear():
        return True


while not at_goal():
    if wall_in_front() and right_is_clear():
        turn_rigth()
    elif not_way():
        while not_way():
            turn_left()
        if front_is_clear():
            move()
        if not at_goal():
            if right_is_clear():
                turn_rigth()
            if front_is_clear():
                move()
        if not at_goal():
            if right_is_clear():
                turn_rigth()
            if front_is_clear():
                while front_is_clear():
                    move()
        else:
            move_with_rigth_wall()
    elif front_is_clear():
        move()
    else:
        move_with_rigth_wall()
