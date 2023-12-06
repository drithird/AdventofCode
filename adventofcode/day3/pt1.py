"""
    --- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

Your puzzle answer was 544433.
    """


def remove_duplicates(number_list):
    for digit in number_list:
        count = number_list.count(digit)
        while count > 1:
            number_list.remove(digit)
            count = number_list.count(digit)
    return number_list

def extract_part_numbers(x,y,engine):
    print("SymbolFound")
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
            if character in symbol_set:
                numbers = extract_part_numbers(x,y,engine)
                answers.append(numbers)
                
            x += 1
        x=0
        y += 1
    
    for symbol_set in answers:
        for number in symbol_set:
            string_int = ''
            for character in number:
                string_int += character
            total += int(string_int)
    print(total)