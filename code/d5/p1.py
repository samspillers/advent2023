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

        seeds_unparsed = text[0].strip()
        seeds = parse_number_line(seeds_unparsed[7:])

        seed_to_soil_map = []
        soil_to_fertilizer_map = []
        fertilizer_to_water_map = []
        water_to_light_map = []
        light_to_temperature_map = []
        temperature_to_humidity_map = []
        humidity_to_location_map = []

        working_header = None
        
        min_location = None

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

        for seed in seeds:
            soil = get_mapping(seed_to_soil_map, seed)
            fertilizer = get_mapping(soil_to_fertilizer_map, soil)
            water = get_mapping(fertilizer_to_water_map, fertilizer)
            light = get_mapping(water_to_light_map, water)
            temperature = get_mapping(light_to_temperature_map, light)
            humidity = get_mapping(temperature_to_humidity_map, temperature)
            location = get_mapping(humidity_to_location_map, humidity)

            if min_location is None or location < min_location:
                min_location = location


        print(min_location)

def parse_number_line(line):
    numbers = line.split(" ")
    return [int(x) for x in numbers]

def get_mapping(in_map, source):
    for dest_start, source_start, length in in_map:
        if source_start <= source < source_start + length:
            return source - source_start + dest_start
    return source

if __name__ == '__main__':
    main()
