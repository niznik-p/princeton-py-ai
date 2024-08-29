# Generated with my work access to Copilot
import random

def rope_swing():
    while True:
        success = input("Did you successfully complete the rope swing? (yes/no): ")
        if success.lower() == "yes":
            break

def wall_climb():
    legs = ["slow", "fast"]
    total_time = 0
    for i in range(10):
        leg_time = random.choice(legs)
        if leg_time == "slow":
            total_time += 2
        else:
            total_time += 1
    return total_time

def door_choice():
    correct_doors = random.sample(range(1, 6), 2)
    for level in range(1, 6):
        print(f"Level {level}: Choose the correct door (1-5): ")
        choice = int(input())
        if choice not in correct_doors:
            print("Wrong door! Try again.")
            return False
    return True

def run_obstacle_course(racer):
    print(f"--- {racer}'s Turn ---")
    rope_swing()
    total_time = wall_climb()
    if door_choice():
        print(f"{racer} completed the obstacle course in {total_time} seconds.")

run_obstacle_course("Mattie")
run_obstacle_course("Matt")
run_obstacle_course("Matthew")

print("Thank you for running the racing program!")