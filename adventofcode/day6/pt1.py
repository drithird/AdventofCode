import re


def calculate_possible_wins_and_losses(total_time,distance):
    time_held = 1
    losses = []
    wins = []
    while time_held < total_time:
        time_running = total_time - time_held
        if time_held * time_running > distance:
            wins.append((time_held,time_held*time_running))
        else:
            losses.append((time_held,time_running*time_held))
        time_held += 1
    return wins,losses

with open('adventofcode/day6/file.txt','r') as file:
    text = file.read()

pattern = r'\d+'
numbers = re.findall(pattern=pattern,string=text)
times = numbers[:4]
distance = numbers[4:]
current_race = 0
win_ways = 1
while current_race < len(times):
    wins,losses = calculate_possible_wins_and_losses(int(times[current_race]),int(distance[current_race]))
    win_ways = win_ways*len(wins)
    current_race +=1
print(win_ways)