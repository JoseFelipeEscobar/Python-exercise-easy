def find_max(nums):
 max_num = float("-inf") # smaller than all other numbers
 for num in nums:
    if num > max_num:
        # (Fill in the missing line here)
        max_num=num
 return max_num
numbers=[1,2,3,4,5]
a=find_max(numbers)
