list_1 = [1,1,1]
list_2 = [1,1,1]

def give_sum(l1, l2):
    return sum(x*x2 for x in l1 for x2 in l2)

print give_sum(list_1, list_2)