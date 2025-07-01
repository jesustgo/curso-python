nums = [4,5,6,2]
goal = 8

def find_first_sum(nums, goal):
    for i in nums:
        for a in nums:
            if i + a == goal and nums.index(i) != nums.index(a):
                return f"{nums.index(i)}, {nums.index(a)}"
    return None   
print(find_first_sum(nums, goal))

