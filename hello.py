def reverse_list(lst):
    if len(lst) <= 1:
        return lst

    # left and right for the list 
    left, right = 0, len(lst) - 1
    # check till it meets in the middle - l > r - while loop
    while left < right: 
        t = lst[left]
        lst[left] = lst[right]
        lst[right] = t
        left += 1
        right -= 1
    return lst
 
    # empty list, one element list
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]     
print(reverse_list(lst))
