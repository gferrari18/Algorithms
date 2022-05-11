#start at the beginning, find smallest item
#swap smallest for first, find second smalles, place it in second....
import random
from re import L

def selectionsort(list):
    for i in range(0, len(list)):
        min = i
        #look for item smalllert
        for j in range(i, len(list)):
            if list[j] < list[min]:
                min = j #found it
        #swap it into this location:
        tmp = list[i]
        list[i]=list[min]
        list[min] = tmp

def main():
    numbers = []
    for i in range(0,1000):
        numbers.append(random.randrange(0,2000))

        print(numbers[0:10])
        selectionsort(numbers)
        print(numbers[0:10])
    
if __name__ == "__main__":
    main()
