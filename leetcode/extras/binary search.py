def binary_search(l, target):
    # assumes a non empty list
    hi = len(l)
    lo = 0

    while lo < hi:
        mid = (hi + lo) // 2

        if l[mid] == target:
            return mid
        elif l[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return None


binary_search([-1,0,3,5,9,12], 12)
