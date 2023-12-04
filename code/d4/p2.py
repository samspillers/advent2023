INPUT_FILE_PATH = "././input/d4/problem.txt"

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        winners_record = []
        total_cards = []
        i = 0
        for line in file:
            i += 1
            winners = calculate_winners(*parse_line(line))
            winners_record.append(winners)
            total_cards.append(1)
        
        for i in range(len(winners_record)):
            for j in range(winners_record[i]):
                total_cards[i + j + 1] += total_cards[i]

        print(sum(total_cards))

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
