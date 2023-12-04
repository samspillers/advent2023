INPUT_FILE_PATH = "././input/d3/problem.txt"

TOP_DOWN_DIAG = [(-1, 1), (0, 1), (1, 1), (1, -1), (0, -1), (-1, -1)]

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        total_sum = 0
        # parse_file(file)
        text = file.read().split("\n")
        for i, row in enumerate(text):
            working_start = None
            for j, alphaNum in enumerate(row):
                if working_start is None and alphaNum.isdigit():
                    working_start = j
                elif working_start is not None and not alphaNum.isdigit():
                    # check number
                    is_part_num = check_num(text, i, working_start, j - 1)
                    if is_part_num:
                        total_sum += int(row[working_start:j])
                    # print(row[working_start:j], is_part_num)
                    working_start = None
            # check if ended on number:
            if working_start is not None:
                # check number
                is_part_num = check_num(text, i, working_start, j)
                if is_part_num:
                    total_sum += int(row[working_start:])
                # print(row[working_start:], is_part_num)
                working_start = None

            # output = 0
            # print(line)

            # total_sum += output
        print(total_sum)

def check_num(text, row_num, start, end):
    for i in range(start, end + 1):
        for dx, dy in TOP_DOWN_DIAG:
            x = i + dx
            y = row_num + dy
            if 0 <= x < len(text[0]) and 0 <= y < len(text) and text[y][x] != ".":
                if text[y][x].isdigit():
                    raise Exception("Shouldn't happen")
                # print(text[row_num][start:end + 1], i - start, dx, dy, text[y][x])
                return True
    if (start > 0 and text[row_num][start - 1] != ".") or (end < len(text[0]) - 1 and text[row_num][end + 1] != "."):
        # print(text[row_num][start:end + 1], True)
        return True
    # print(text[row_num][start:end + 1], False)
    return False
            


if __name__ == '__main__':
    main()
