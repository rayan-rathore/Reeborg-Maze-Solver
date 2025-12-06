def turn_right():
    turn_left()
    turn_left()
    turn_left()   
def go_ahead():
    turn_right()
    move()
  
while not at_goal():
    if right_is_clear():
        go_ahead()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        
