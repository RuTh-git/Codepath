def find_affordable_ticket(prices, budget):
    l, r = 0, len(prices) - 1

    while l <= r:
        mid = (l + r) // 2
        if prices[mid] == budget:
            return mid + 1
        elif prices[mid] > budget: # left portion
            r = mid - 1
        else:
            l = mid + 1
    return r 

# [ 50, 75, 100, 150 ]
# [ 50, 75 ]
# [ 50, 75 ]
# l = 0
# r = 1


print(find_affordable_ticket([50, 75, 100, 150], 110)) # 2
print(find_affordable_ticket([50, 75, 100, 150], 100)) # 2
print(find_affordable_ticket([75, 100, 150], 60)) # 0 

# 50 75 100 150 , t = 60
# m = 75 -> 75> 60
# r = 50, l =50 
# mid = 50 