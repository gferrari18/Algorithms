import random



def binarysearch(haystack, needle):
    start = 0
    end = len(haystack)

    while start <= end:
        i = start + (end-start)//2
        if haystack[i] < needle:
            start = i+1
        elif haystack[i] > needle:
            end = i-1
        else: return i
    return -1

def main():
    numbers = []
    for i in range (0,1000):
        numbers.append(random.randrange(0,2000))

    numbers.sort()
    target = random.randrange(0,2000)
    location = binarysearch(numbers,target)
    if location == -1:
        print("Couldnt find " + str(target))
    else:
        print("found " + str(target) +  " at location " + str(location))

if __name__ == "__main__":
    main()