"""
--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""
def get_game_num(file_line: str)->int:
    #Code below isolates the game number from the file.txt
    start_index = file_line.find("e")+1
    end_index = file_line.find(":")
    game_num = file_line[start_index:end_index]
    return int(game_num)
def get_game_rounds(file_line: str)->str:
    index = file_line.find(":")+1
    game = file_line[index:]
    current_round = []
    round_list =  []
    for character in game:
        if character == '\n':
            round_list.append(current_round)
            return round_list
        if character == ';':
            round_list.append(str(current_round))
            current_round = []
        else:
            current_round.append(character)
    round_list.append(current_round)
    return round_list

def get_results_from_cycle(cycle: str):
    pulling_data = False
    value = None
    results = []
    current_digits = []
    for character in cycle:
        if pulling_data == True:
            if character.isalpha():
                num=''
                for char in current_digits:
                    num += char 
                results.append((int(num),character))
                current_digits = []
                pulling_data = False
            elif character.isdigit():
                current_digits.append(character)
        elif character.isdigit():
            pulling_data = True
            current_digits.append(character)
        
    return results

def calculate_minimum_cubes(results):
    min_red = 0
    min_green = 0
    min_blue = 0
    for cycle in results:
        for result in cycle:
            if result[1] == 'r':
                if result[0]>min_red:
                    min_red = result[0]
            if result[1] == 'g':
                if result[0]>min_green:
                    min_green = result[0]
            if result[1] == 'b':
                if result[0]>min_blue:
                    min_blue = result[0]
    return min_red,min_green,min_blue

with open("adventofcode/day2/file.txt",'r') as file:
    answer = 0
    count = 0
    for line in file:
        game_num = get_game_num(line)
        
        rounds = get_game_rounds(line)
        round_possible = True
        results = []
        for cycle in rounds:
            results.append(get_results_from_cycle(cycle))
        minimum_cubes = calculate_minimum_cubes(results)
        answer += minimum_cubes[0]*minimum_cubes[1]*minimum_cubes[2]
    print(answer)
        
        