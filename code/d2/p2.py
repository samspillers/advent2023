INPUT_FILE_PATH = "././input/d2/problem.txt"

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        total_sum = 0
        i = 0
        for line in file:
            i += 1
            output = verify_line(parse_line(line))
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
    min_r = 0
    min_g = 0
    min_b = 0
    _, pulls = parsed_line
    for pull in pulls:
        r, g, b = pull
        if r is not None and r > min_r:
            min_r = r
        if g is not None and g > min_g:
            min_g = g
        if b is not None and b > min_b:
            min_b = b
    return min_r * min_g * min_b

if __name__ == '__main__':
    main()
