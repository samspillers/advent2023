INPUT_FILE_PATH = "././input/d2/problem.txt"

NUMBER_OF_RED = 12
NUMBER_OF_GREEN = 13
NUMBER_OF_BLUE = 14

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        total_sum = 0
        i = 0
        for line in file:
            i += 1
            output, why = verify_line(parse_line(line))
            print(output if why is None else why, line.strip())

            total_sum += output
        print(total_sum)

def parse_line(line):
    game, all_pulls = line.split(": ")
    gameId = int(game.split("Game ")[1].strip())
    pulls = all_pulls.split("; ")
    output = []
    for pull in pulls:
        colors = pull.split(", ")
        r = None
        g = None
        b = None
        for color in colors:
            if color.find("red") != -1:
                r = int(color.split("red")[0].strip())
            elif color.find("green") != -1:
                g = int(color.split("green")[0].strip())
            elif color.find("blue") != -1:
                b = int(color.split("blue")[0].strip())
            else:
                raise Exception("Shouldn't happen")
        output.append((r, g, b))
    return gameId, output

def verify_line(parsed_line):
    game_id, pulls = parsed_line
    for pull in pulls:
        r, g, b = pull
        if r is not None and r > NUMBER_OF_RED:
            return 0, "red"
        if g is not None and g > NUMBER_OF_GREEN:
            return 0, "green"
        if b is not None and b > NUMBER_OF_BLUE:
            return 0, "blue"
    # print(parsed_line)
    return game_id, None

if __name__ == '__main__':
    main()
