import copy

INPUT_FILE_PATH = "././input/d5/problem.txt"

SEED_TO_SOIL = "seed-to-soil map:"
SEED_TO_FERTILIZER = "soil-to-fertilizer map:"
FERTILIZER_TO_WATER = "fertilizer-to-water map:"
WATER_TO_LIGHT = "water-to-light map:"
LIGHT_TO_TEMPERATURE = "light-to-temperature map:"
TEMPERATURE_TO_HUMIDITY = "temperature-to-humidity map:"
HUMIDITY_TO_LOCATION = "humidity-to-location map:"

HEADERS = [SEED_TO_SOIL, SEED_TO_FERTILIZER, FERTILIZER_TO_WATER, WATER_TO_LIGHT, LIGHT_TO_TEMPERATURE, TEMPERATURE_TO_HUMIDITY, HUMIDITY_TO_LOCATION]

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        text = file.read().split("\n")

        seeds = parse_seeds(text[0].strip())

        seed_to_soil_map = []
        soil_to_fertilizer_map = []
        fertilizer_to_water_map = []
        water_to_light_map = []
        light_to_temperature_map = []
        temperature_to_humidity_map = []
        humidity_to_location_map = []

        working_header = None

        for i in range(2, len(text)):
            line = text[i].strip()
            
            if len(line) != 0:
                if line in HEADERS:
                    working_header = line
                else:
                    parsed_line = parse_number_line(line)

                    if len(parsed_line) == 0:
                        raise Exception("Shouldn't happen")

                    if working_header == SEED_TO_SOIL:
                        seed_to_soil_map.append(parsed_line)
                    elif working_header == SEED_TO_FERTILIZER:
                        soil_to_fertilizer_map.append(parsed_line)
                    elif working_header == FERTILIZER_TO_WATER:
                        fertilizer_to_water_map.append(parsed_line)
                    elif working_header == WATER_TO_LIGHT:
                        water_to_light_map.append(parsed_line)
                    elif working_header == LIGHT_TO_TEMPERATURE:
                        light_to_temperature_map.append(parsed_line)
                    elif working_header == TEMPERATURE_TO_HUMIDITY:
                        temperature_to_humidity_map.append(parsed_line)
                    elif working_header == HUMIDITY_TO_LOCATION:
                        humidity_to_location_map.append(parsed_line)
                    else:
                        raise Exception("Shouldn't happen")

        soil = clean_ranges(get_mapping(seed_to_soil_map, seeds))
        fertilizer = clean_ranges(get_mapping(soil_to_fertilizer_map, soil))
        water = clean_ranges(get_mapping(fertilizer_to_water_map, fertilizer))
        light = clean_ranges(get_mapping(water_to_light_map, water))
        temperature = clean_ranges(get_mapping(light_to_temperature_map, light))
        humidity = clean_ranges(get_mapping(temperature_to_humidity_map, temperature))
        location = clean_ranges(get_mapping(humidity_to_location_map, humidity))

        print(min(location, key=lambda e: e[0])[0])

def parse_number_line(line):
    numbers = line.split(" ")
    return [int(x) for x in numbers]

def parse_seeds(seeds_unparsed):
    seeds = parse_number_line(seeds_unparsed[7:])
    return [(seeds[2 * x], seeds[2 * x + 1]) for x in range(int(len(seeds) / 2))]

def get_mapping(in_map, seeds):
    input_seeds = copy.deepcopy(seeds)
    output = []
    untouched = []

    while len(input_seeds) > 0:
        seed_start, seed_length = input_seeds[-1]
        touched = False

        for dest_start, source_start, source_length in in_map:

            # If clip
            if seed_start + seed_length > source_start and seed_start < source_start + source_length:
                if touched is True:
                    # Two sources shouldn't touch the same seed since we break once a seed is touched by a source
                    raise Exception("Shouldn't happen")

                touched = True
                del input_seeds[-1]

                # *Seed Inside*
                # Source: <-[-----------]->
                # Seed:         {---}
                if source_start <= seed_start and seed_start + seed_length <= source_start + source_length:
                    output.append((seed_start - source_start + dest_start, seed_length))
                # *Seed Below*
                # Source: <----[------]--->
                # Seed:     {----}
                elif seed_start < source_start <= seed_start + seed_length <= source_start + source_length:
                    inside_length = seed_start + seed_length - source_start
                    output.append((dest_start, inside_length))
                    input_seeds.append((seed_start, source_start - seed_start))
                # *Seed Above*
                # Source: <---[------]---->
                # Seed:            {----}
                elif source_start <= seed_start <= source_start + source_length < seed_start + seed_length:
                    inside_start, inside_length = seed_start, source_start + source_length - seed_start
                    output.append((inside_start - source_start + dest_start, inside_length))
                    input_seeds.append((source_start + source_length, seed_start + seed_length - source_start - source_length))
                # *Seed Surrounds*
                # Source: <----[----]---->
                # Seed:      {--------}
                elif seed_start < source_start and source_start + source_length < seed_start + seed_length:
                    output.append((dest_start, source_length))
                    if source_start - seed_start > 0:
                        input_seeds.append((seed_start, source_start - seed_start))
                    if seed_start + seed_length - source_start - source_length > 0:
                        input_seeds.append((source_start + source_length, seed_start + seed_length - source_start - source_length))
                else:
                    print(dest_start, source_start, source_length, seed_start, seed_length)
                    raise Exception("Shouldn't happen")
                break

        if touched is False:
            untouched.append(input_seeds[-1])
            del input_seeds[-1]

    for seed_start, seed_length in untouched:
        output.append((seed_start, seed_length))
    return output

def clean_ranges(seeds):
    sorted_seeds = sorted(seeds, key=lambda e: e[0])
    output = []
    for seed in sorted_seeds:
        current_start, current_length = seed
        # if output empty or
        if len(output) == 0:
            output.append(seed)
        else:
            last_start, last_length = output[-1]
            # if new seed is after end of last one
            if current_start > last_start + last_length:
                output.append(seed)
            # if extends last's length
            elif current_start + current_length > last_start + last_length:
                # add onto the last seed if intersecting/adjacent
                output[-1] = (output[-1][0], current_start + current_length - last_start)
    return output

if __name__ == '__main__':
    main()
