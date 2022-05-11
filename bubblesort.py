import random

#starts looking at first two items. Swap them if out of order
#if goes tru the list without swapping, ends early
def bubblesort(list):
    swap = True
    while swap:
        swap = False
        for i in range(0,len(list)-1):
            if list[i] > list[i+1]:
                swap = True
                tmp = list[i]
                list[i] = list[i+1]
                list[i+1] = tmp

def main():
    numbers = []
    # let's make a list of random numbers
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    print(numbers[0:10])
    bubblesort(numbers)
    print(numbers)

if __name__ == '__main__':
    main()