# Generated with my personal access to Claude 3.5 Sonnet

import random
import time


class Racer:
    def __init__(self, name):
        self.name = name
        self.total_time = 0

    def rope_swing(self):
        attempts = 0
        while True:
            attempts += 1
            if random.random() > 0.3:  # 70% success rate
                self.total_time += attempts * 5  # 5 seconds per attempt
                return attempts
            time.sleep(0.1)  # Small delay to simulate attempt

    def wall_climb(self):
        for _ in range(10):
            if random.random() > 0.3:  # 70% chance of being fast
                self.total_time += 3  # Fast climb: 3 seconds
            else:
                self.total_time += 5  # Slow climb: 5 seconds
            time.sleep(0.1)  # Small delay to simulate climb

    def door_choice(self):
        for _ in range(5):
            if random.random() > 0.4:  # 60% chance of choosing correct door
                self.total_time += 5  # Correct door: 5 seconds
            else:
                self.total_time += 15  # Wrong door: 15 seconds
            time.sleep(0.1)  # Small delay to simulate choice

    def run_course(self):
        print(f"{self.name} is starting the course!")

        print("Rope Swing:")
        attempts = self.rope_swing()
        print(f"  Completed in {attempts} attempts")

        print("Wall Climb:")
        self.wall_climb()
        print("  Completed the wall climb")

        print("Door Choice:")
        self.door_choice()
        print("  Completed the door choices")

        print(f"{self.name} finished in {self.total_time:.2f} seconds!")
        print()


def main():
    racers = [Racer("Mattie"), Racer("Matt"), Racer("Matthew")]

    for racer in racers:
        racer.run_course()

    print("Final Results:")
    for racer in sorted(racers, key=lambda x: x.total_time):
        print(f"{racer.name}: {racer.total_time:.2f} seconds")

    print("\nThank you for running the racing program!")


if __name__ == "__main__":
    main()