def main():
    is_armed = False
    motion_detected = False
    door_open = False
    is_afternoon = True
    displey_alarm(is_armed, motion_detected, door_open, is_afternoon)

def displey_alarm(iar, ms, dop, an):
    if iar:
        if ms:
            print("INTRUDER!!!!!")
        if dop:
            print("door is open")
    else:
        if an and ms:
            print("Welcome home! Turning the light on!")


main()