"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Your puzzle answer was 76314915.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.
"""


def remove_duplicates(number_list):
    for digit in number_list:
        count = number_list.count(digit)
        while count > 1:
            number_list.remove(digit)
            count = number_list.count(digit)
    return number_list

def extract_part_numbers(x,y,engine):
    digits_found = []
    current_number = []
    spaces_to_check = [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1)]
    for x,y in spaces_to_check:
        character: str = engine[y][x]
        if character.isdigit():
            current_number.append(character)
            character = engine[y][x-1]
            if character.isdigit():
                current_number.insert(0, character)
                character = engine[y][x-2]
                if character.isdigit():
                    current_number.insert(0, character)
                    digits_found.append(current_number)
                else:
                    character = engine[y][x+1]
                    if character.isdigit():
                        current_number.append(character)
                        digits_found.append(current_number)
                    else:
                        digits_found.append(current_number)
            else:
                character = engine[y][x+1]
                if character.isdigit():
                    current_number.append(character)
                    character = engine[y][x+2]
                    if character.isdigit():
                        current_number.append(character)
                        digits_found.append(current_number)
                    else:
                        digits_found.append(current_number)
                else:
                    digits_found.append(current_number)

        current_number = []
    for digit in digits_found:
        digit = str(digit)  
    digits_found = remove_duplicates(digits_found) 
    return digits_found
with open("adventofcode/day3/file.txt",'r') as file:
    total = 0
    answers = []
    engine = [[]]
    y = 0
    ratio = 0
    symbol_set = []
    for line in file:
        for character in line:
            if character == '\n':
                y += 1
                engine.append([])
            elif (character == '.') or character.isdigit():
                engine[y].append(character)
            else:
                engine[y].append(character)
                symbol_set.append(character)
    x = 0
    y = 0     
    max_y = len(engine)
    max_x = len(engine[0])
    while y < max_y:
        while x < max_x:
            character = engine[y][x]
            if character == '*':
                numbers = extract_part_numbers(x,y,engine)
                if len(numbers) == 2:
                    gears=[]
                    for number in numbers:
                        int_num = int(''.join(number))
                        gears.append(int_num)
                    ratio = gears[0] * gears[1]
                    answers.append(ratio)
                
            x += 1
        x=0
        y += 1
    for number in answers:
        
        total += number
    print(total)