# Generated with my work access to ChatGPT 4o
import random
import time

# Function for the rope swing challenge
def rope_swing(racer_name):
    attempts = 0
    while True:
        attempts += 1
        success = random.choice([True, False])
        if success:
            print(f"{racer_name} succeeded on the rope swing after {attempts} attempt(s).")
            return attempts * 2  # Each attempt takes 2 seconds
        else:
            print(f"{racer_name} failed the rope swing and is trying again...")

# Function for the wall climb challenge
def wall_climb(racer_name):
    total_time = 0
    for leg in range(10):
        speed = random.choice(["fast", "slow"])
        if speed == "fast":
            leg_time = 1  # Fast leg takes 1 second
        else:
            leg_time = 3  # Slow leg takes 3 seconds
        total_time += leg_time
        print(f"{racer_name} completed leg {leg + 1} of the wall climb in {leg_time} second(s) ({speed}).")
    return total_time

# Function for the door choice challenge
def door_choice(racer_name):
    total_time = 0
    for level in range(5):
        correct_door = random.choice([1, 2])
        while True:
            chosen_door = random.choice([1, 2, 3])
            if chosen_door == correct_door:
                print(f"{racer_name} chose the correct door on level {level + 1}.")
                total_time += 2  # Each correct choice takes 2 seconds
                break
            else:
                print(f"{racer_name} chose the wrong door on level {level + 1} and is trying again...")
                total_time += 5  # Each wrong choice takes 5 seconds
    return total_time

# Main function to run the race
def run_race():
    racers = ["Mattie", "Matt", "Matthew"]
    final_times = {}

    for racer in racers:
        print(f"\nStarting race for {racer}...\n")
        time.sleep(1)

        rope_swing_time = rope_swing(racer)
        wall_climb_time = wall_climb(racer)
        door_choice_time = door_choice(racer)

        total_time = rope_swing_time + wall_climb_time + door_choice_time
        final_times[racer] = total_time
        print(f"\n{racer} finished the course with a time of {total_time} seconds.\n")

    print("Final Times:")
    for racer, total_time in final_times.items():
        print(f"{racer}: {total_time} seconds")

    print("\nThank you for running the racing program!")

# Run the race
run_race()
