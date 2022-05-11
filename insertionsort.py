import random
#insertion sor
#sort items like cards find right place for card, shift cards to make room
def insertionsort(list):
    for i in range(1, len(list)):
        number = list[i]
        pos = i
        while pos > 0 and list[pos-1] > number:
            list[pos] = list[pos-1]
            pos = pos - 1
        list[pos] = number

def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    print(numbers[0:10])
    insertionsort(numbers)
    print(numbers)

if __name__ == '__main__':
    main()