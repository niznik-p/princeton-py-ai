# Generated with my personal access to Gemini Advanced
import random
import time

def rope_swing(racer_name):
    """Simulates a rope swing challenge with retries until success."""
    attempts = 0
    while True:
        attempts += 1
        if random.random() < 0.7:  # 70% chance of success
            print(f"{racer_name} successfully swung across the rope on attempt {attempts}!")
            return
        else:
            print(f"{racer_name} missed the swing! Trying again...")

def wall_climb(racer_name):
    """Simulates a wall climb with varying leg speeds due to fatigue."""
    total_time = 0
    for leg in range(1, 11):
        if random.random() < 0.3 + 0.07 * leg:  # Increasing fatigue chance
            leg_time = random.uniform(1.5, 2.5)  # Slow leg
            print(f"{racer_name} is feeling tired on leg {leg}... (slow)")
        else:
            leg_time = random.uniform(0.8, 1.2)  # Fast leg
            print(f"{racer_name} is climbing strong on leg {leg}! (fast)")
        total_time += leg_time
    print(f"{racer_name} completed the wall climb in {total_time:.2f} seconds.")
    return total_time

def door_choice(racer_name):
    """Simulates a 5-level door choice with 2 correct doors at each level."""
    total_time = 0
    for level in range(1, 6):
        while True:
            choice = random.randint(1, 3)
            if choice in [1, 2]:  # Assuming doors 1 and 2 are correct
                print(f"{racer_name} chose the correct door on level {level}!")
                total_time += random.uniform(2, 3)  # Time to open and pass
                break
            else:
                print(f"{racer_name} chose the wrong door on level {level}! Trying again...")
                total_time += 1  # Penalty for wrong choice
    print(f"{racer_name} completed the door challenge in {total_time:.2f} seconds.")
    return total_time

# From the first attempt - time doesn't get saved properly
def run_race(racers):
    """Runs the obstacle course for the given racers and records their times."""
    results = {}
    for racer in racers:
        start_time = time.time()

        rope_swing(racer)
        wall_climb_time = wall_climb(racer)
        door_choice_time = door_choice(racer)

        total_time = time.time() - start_time
        results[racer] = total_time

        print(f"\n{racer}'s final time: {total_time:.2f} seconds\n")

    return results

# Generated after asking it to investigate a bug that showed all racers with 0.00 seconds
def run_race_2(racers):
    """Runs the obstacle course for the given racers and records their times."""
    results = {}
    for racer in racers:
        start_time = time.time()

        rope_swing(racer)
        wall_climb_time = wall_climb(racer)
        door_choice_time = door_choice(racer)

        # Accumulate the times from each obstacle
        total_time = time.time() - start_time + wall_climb_time + door_choice_time
        results[racer] = total_time

        print(f"\n{racer}'s final time: {total_time:.2f} seconds\n")

    return results

if __name__ == "__main__":
    racers = ["Mattie", "Matt", "Matthew"]
    final_times = run_race_2(racers)

    print("\n--- Final Results ---")
    for racer, time in final_times.items():
        print(f"{racer}: {time:.2f} seconds")

    print("\nThank you for running the racing program!")