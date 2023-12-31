INPUT_FILE_PATH = "././input/d4/problem.txt"

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        total_sum = 0
        i = 0
        for line in file:
            i += 1
            winners = calculate_winners(*parse_line(line))
            if winners > 0:
                total_sum += 2 ** (winners - 1)
        print(total_sum)

def parse_line(line):
    winning, ours_whole = line.strip().split(" | ")
    _, winning_nums_whole = winning.split(": ")
    our_nums = ours_whole.split(" ")
    winning_nums = winning_nums_whole.split(" ")
    for i in range(len(our_nums) - 1, -1, -1):
        if len(our_nums[i]) == 0:
            del our_nums[i]
    for i in range(len(winning_nums) - 1, -1, -1):
        if len(winning_nums[i]) == 0:
            del winning_nums[i]

    return winning_nums, our_nums

def calculate_winners(winning_nums, our_nums):
    total_winners = 0
    for num in our_nums:
        if num in winning_nums:
            total_winners += 1
    return total_winners

if __name__ == '__main__':
    main()
