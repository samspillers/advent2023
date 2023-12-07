INPUT_FILE_PATH = "././input/d7/problem.txt"

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
HANDS = ["5", "4", "F", "3", "2", "1", "H"]

def main():
    with open(INPUT_FILE_PATH, "r") as file:
        hands = []
        for line in file:
            hands.append(parse_line(line))
        
        bubbleSort(hands, hand_compare)

        total_sum = 0
        for i, e in enumerate(hands):
            # print(len(hands) - i, e)
            total_sum += (len(hands) - i) * e[1]

        print(total_sum)
        # sorted_hands = sorted(hands, key=hand_compare)

def parse_line(line):
    split_line = line.strip().split(" ")
    cards = [x for x in split_line[0]]
    bid = int(split_line[1])
    return cards, bid

def get_hand_type(cards):
    counts = [0 for _ in range(len(CARDS))]
    
    # print(cards)

    for card in cards:
        counts[CARDS.index(card)] += 1
    
    highest = None
    next_highest = None
    for i, e in enumerate(counts):
        if highest is None or e > highest:
            if highest is not None:
                next_highest = highest
            highest = e
        elif next_highest is None or e > next_highest:
            next_highest = e
    
    if highest == 1:
        return "H"
    elif highest == 3 and next_highest == 2:
        return "F"
    elif highest == 2 and next_highest == 2:
        return "2"
    elif highest == 2 and next_highest == 1:
        return "1"
    else:
        return str(highest)

def hand_compare(cards_a, cards_b):
    a_type = get_hand_type(cards_a[0])
    b_type = get_hand_type(cards_b[0])
    diff = HANDS.index(a_type) - HANDS.index(b_type)
    if diff != 0:
        return diff
    for i in range(len(cards_a[0])):
        card_a = cards_a[0][i]
        card_b = cards_b[0][i]
        diff = CARDS.index(card_a) - CARDS.index(card_b)
        if diff != 0:
            return diff
    raise Exception("Shouldn't get here")


# Python3 program for Bubble Sort Algorithm Implementation
def bubbleSort(arr, comp):
     
    n = len(arr)
 
    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
             
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if comp(arr[j], arr[j + 1]) > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == '__main__':
    main()
