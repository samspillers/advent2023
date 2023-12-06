INPUT_FILE_PATH = "././input/d6/problem.txt"

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        text = file.read().split("\n")
        times_unparsed = text[0].strip()
        distances_unparsed = text[1].strip()
        time = parse_line(times_unparsed)
        record = parse_line(distances_unparsed)

        output = 1

        possible = []
        for i in range(time):
            speed = i
            remaining_time = time - i
            distance = speed * remaining_time
            if distance > record:
                possible.append(i)
        output *= len(possible)

        print(output)

def parse_line(line):
    nums_unparsed = line.split(":")[1]
    nums_strings = nums_unparsed.split(" ")
    output = ""

    for x in nums_strings:
        if len(x) > 0:
            output += x
    
    return int(output)
    

if __name__ == '__main__':
    main()
