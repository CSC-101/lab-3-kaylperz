def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body. total = 4 num = 4, total = 13 num =9, total =15 num =2, total=16 num=1
    return total

result = tally([4, 9, 2, 1]) #result = 16

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body. new_list = [4, 9, 2, 1] idx=3
    return new_list                    # How does this loop differ from that above? first loop go through list and gives total (add), and second one just builds a list (appends)

result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. new_list = [5, 10, 3, 2] value = 1

    return new_list

result = increment_all([4, 9, 2, 1])
