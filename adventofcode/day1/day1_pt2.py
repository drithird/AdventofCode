"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Your puzzle answer was 54249.
"""
'zoneight234'
def determine_word(word: str,character: str):
    test_word = word+character
    length = len(test_word)
    
    if length < 3 :
        return test_word, None
    if length == 3:
        if test_word == 'one':
            return test_word[1:] ,'1'
        elif test_word == 'two':
            return test_word[1:] ,'2'
        elif test_word == 'six':
            return test_word[1:] ,'6'
        elif test_word in ('thr','fou','fiv','sev','eig','nin'):
            return test_word, None
        else:
            return test_word[1:], None
    if length == 4:
        if test_word == 'four':
            return test_word[1:] ,'4'
        elif test_word == 'five':
            return test_word[1:] ,'5'
        elif test_word == 'nine':
            return test_word[1:] ,'9'
        elif test_word in ('thre','seve','eigh'):
            return test_word, None
        else:
            return determine_word(test_word[1:],'')
    if length == 5:
        if test_word == 'three':
            return test_word[1:] ,'3'
        if test_word == 'seven':
            return test_word[1:] ,'7'
        if test_word == 'eight':
            return test_word[1:] ,'8'
        else:
            return determine_word(test_word[1:],'')

with open('adventofcode/day1/file1.txt','r') as text:
    answer=0
    for line in text:
        first_num = None
        last_num = None
        current_word = None
        for character in line:
            if character == '\n':
                break
            if character.isalpha():
                if current_word == None:
                    current_word = character
                else:
                    current_word, number = determine_word(current_word,character)
                    if number != None:
                        if first_num == None:
                            first_num = number
                        else:
                            last_num = number
                        
            else:
                if first_num == None:
                    first_num = character
                else:
                    last_num = character
        if last_num == None:
            last_num = first_num
        two_digit = first_num+last_num
        answer += int(two_digit)
    print(answer)
   
