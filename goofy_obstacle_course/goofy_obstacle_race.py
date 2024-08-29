import numpy as np
import random

racers = {}
racer_names = ['Mattie', 'Matt', 'Matthew']
# racer_names = ['Mattie', 'Matt', 'Matthew', 'Madison', 'Matilda', 'Matty', 'Maddie', 'Mathias', 'Mattias', 'Mateo']


def run_course(racer_name, racer_attributes):
    # Rope Swing
    success_rate = 0.7 + 0.3*racer_attributes['skill']
    while np.random.rand() > success_rate:
        racer_attributes['time'] += 5.0
        print('Rope Swing failed for', racer_name)
    racer_attributes['time'] += 2.0
    print('Rope Swing succeeded for', racer_name)
    print('Split: ', racer_attributes['time'])

    # Wall Climb
    fast_advance_rate = 0.3 + 0.7*racer_attributes['skill']
    for i in range(10):
        if np.random.rand() < fast_advance_rate:
            racer_attributes['time'] += 1.0
            print('Fast advance for', racer_name)
        else:
            racer_attributes['time'] += 2.0
            print('Slow advance for', racer_name)
    print('Wall Climb succeeded for', racer_name)
    print('Split: ', racer_attributes['time'])

    # Door Choice
    for i in range(5):
        doors = [1, 1, 0, 0, 0]
        random.shuffle(doors)
        while True:
            choice = random.randint(0, len(doors)-1)
            if doors[choice] == 1:
                racer_attributes['time'] += 1.0
                print('Level {i}: Door ', choice, 'was correct for', racer_name)
                break
            else:
                racer_attributes['time'] += 3.0
                print('Level {i}: Door ', choice, 'was incorrect for', racer_name)
                doors.pop(choice)

    print('{racer} finished in {time} seconds'.format(racer=racer_name, time=racer_attributes['time']))


for name in racer_names:
    racers[name] = {'time': 0.0, 'skill': np.random.rand()}
    run_course(name, racers[name])
    print('---')

print('Recap:')
for name in racer_names:
    print('{racer} finished in {time} seconds'.format(racer=name, time=racers[name]['time']))
print('Thanks for racing!')
