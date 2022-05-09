def binarysearch(haystack, needle):
    start = 0
    end = len(haystack)

    while start <= end:
        i = start + (end-start)//2
        if haystack[i] < needle:
            start = i+1
        elif haystack[i] > needle:
            end = i-1
        else: return 1
        