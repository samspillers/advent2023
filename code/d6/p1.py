INPUT_FILE_PATH = "././input/d6/problem.txt"

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        text = file.read().split("\n")
        times_unparsed = text[0].strip()
        distances_unparsed = text[1].strip()
        times = parse_line(times_unparsed)
        distances = parse_line(distances_unparsed)
        races = [(times[i], distances[i]) for i in range(len(times))]

        output = 1

        for time, record in races:
            possible = []
            for i in range(time):
                speed = i
                remaining_time = time - i
                distance = speed * remaining_time
                if distance > record:
                    possible.append(i)
            print(time, record, possible)
            output *= len(possible)

        print(output)

def parse_line(line):
    nums_unparsed = line.split(":")[1]
    nums_strings = nums_unparsed.split(" ")
    output = []

    for x in nums_strings:
        if len(x) > 0:
            output.append(int(x))
    
    return output
    

if __name__ == '__main__':
    main()
