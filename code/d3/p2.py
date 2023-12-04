INPUT_FILE_PATH = "././input/d3/problem.txt"

TOP_DOWN_DIAG = [(-1, 1), (0, 1), (1, 1), (1, -1), (0, -1), (-1, -1)]

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        gear_map = {}
        text = file.read().split("\n")
        for i, row in enumerate(text):
            working_start = None
            for j, alphaNum in enumerate(row):
                if working_start is None and alphaNum.isdigit():
                    working_start = j
                elif working_start is not None and not alphaNum.isdigit():
                    # check number
                    possible_gear = find_possible_gear(text, i, working_start, j - 1)
                    if possible_gear is not None:
                        if not possible_gear in gear_map:
                            gear_map[possible_gear] = []
                        gear_map[possible_gear].append(int(row[working_start:j]))
                    # print(row[working_start:j], is_part_num)
                    working_start = None
            # check if ended on number:
            if working_start is not None:
                # check number
                possible_gear = find_possible_gear(text, i, working_start, j)
                if possible_gear is not None:
                    if not possible_gear in gear_map:
                        gear_map[possible_gear] = []
                    gear_map[possible_gear].append(int(row[working_start:]))
                # print(row[working_start:], is_part_num)
                working_start = None
        # print(gear_map)
        total_sum = 0
        for _, num_list in gear_map.items():
            if len(num_list) == 2:
                gear_ratio = 1
                for num in num_list:
                    gear_ratio *= num
                total_sum += gear_ratio
        print(total_sum)



def find_possible_gear(text, row_num, start, end):
    for i in range(start, end + 1):
        for dx, dy in TOP_DOWN_DIAG:
            x = i + dx
            y = row_num + dy
            if 0 <= x < len(text[0]) and 0 <= y < len(text) and text[y][x] == "*":
                if text[y][x].isdigit():
                    raise Exception("Shouldn't happen")
                # print(text[row_num][start:end + 1], i - start, dx, dy, text[y][x])
                return x, y
    if start > 0 and text[row_num][start - 1] == "*":
        return start - 1, row_num
    if end < len(text[0]) - 1 and text[row_num][end + 1] == "*":
        # print(text[row_num][start:end + 1], True)
        return end + 1, row_num
    # print(text[row_num][start:end + 1], False)
    return None

if __name__ == '__main__':
    main()
