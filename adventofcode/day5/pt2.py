"""--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?"""


def reverse_the_map(index,map) -> int:
    for row in map:
        if index in range(row[0],row[0]+row[2]):
            new_location = row[1]+index-row[0]
            return new_location
    return index
seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
current_list = None
locations = []
with open("adventofcode/day5/file.txt",'r') as file:
    file_text = file.read()
lines = file_text.strip().split('\n')
for line in lines:
    if line.startswith('seeds:'):
        current_list = seeds
    elif line.startswith('seed-to-soil map'):
        current_list = seed_to_soil_map
    elif line.startswith('soil-to-fertilizer map'):
        current_list = soil_to_fertilizer_map
    elif line.startswith('fertilizer-to-water'):
        current_list = fertilizer_to_water_map
    elif line.startswith('water-to-light map'):
        current_list = water_to_light_map
    elif line.startswith('light-to-temperature map'):
        current_list = light_to_temperature_map
    elif line.startswith('temperature-to-humidity map'):
        current_list = temperature_to_humidity_map
    elif line.startswith('humidity-to-location map'):
        current_list = humidity_to_location_map
    elif line.startswith('\n') or line == '':
        pass
    else:
        numbers = [int(num) for num in line.split()]
        current_list.append(numbers)
index = 0
seed_ranges = []
seeds = seeds[0]
while index < len(seeds):
    seed_ranges.append(range(seeds[index],seeds[index]+seeds[index+1]-1))
    index += 2
location = 0
seed_found = False
while seed_found == False:
    humid = reverse_the_map(location, humidity_to_location_map)
    temp = reverse_the_map(humid,temperature_to_humidity_map)
    light = reverse_the_map(temp,light_to_temperature_map)
    water = reverse_the_map(light,water_to_light_map)
    fertilizer = reverse_the_map(water, fertilizer_to_water_map)
    soil = reverse_the_map(fertilizer,soil_to_fertilizer_map)
    seed = reverse_the_map(soil,seed_to_soil_map)
    for spread in seed_ranges:
        if seed in spread:
            seed_found = True 
    print(seed)       
    location += 1
print(seed)    
print(location-1)
    

#print(seeds)
#print(seed_to_soil_map)
#print(soil_to_fertilizer_map)
#print(fertilizer_to_water_map)
#print(water_to_light_map)
#print(light_to_temperature_map)
#print(temperature_to_humidity_map)
#print(humidity_to_location_map)
