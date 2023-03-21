"""
Calculator functions
"""

def add(x,y):
    "Add x and y and return result"
    return x + y
def subtract(x,y):
    """subtract x from y and return result"""
    return y - x

def removeDuplicate(numbers = []):
    prev_num = numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i]==prev_num:
            numbers.pop(i)
            prev_num = numbers[i]
        else:
            continue
    return numbers