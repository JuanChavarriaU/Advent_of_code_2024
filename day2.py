



def isSafe(list1:list) -> bool:
    #monotoic verification and limits
    increasing = all(list1[i] < list1[i + 1] and 1 <= abs(list1[i] - list1[i + 1]) <= 3 for i in range(len(list1) - 1))
    decreasing = all(list1[i] > list1[i + 1] and 1 <= abs(list1[i] - list1[i + 1]) <= 3 for i in range(len(list1) - 1))
    return increasing or decreasing

def isSafeWithDampener(list1: list) -> bool:

    if isSafe(list1):
        return True

    for i in range(len(list1)):
        modList = list1[:i] + list1[i+1:]
        if isSafe(modList):
            return True
        
    return False


counter = 0
with open('C:/Users/juanj/Desktop/data.txt', 'r') as file:
    for line in file:
        int_list = list(map(int, line.split()))
    
        if isSafeWithDampener(int_list):
            counter += 1 

print(f'Safe reports: {counter}')