# What is the output of the following Python 3 code:
def Filter1(nums):
    for num in nums:
        if num % 2 == 0:
            yield num
def Filter2(nums):
    for num in nums:
        yield num * 3
def Filter3(nums):
    for num in nums:
        yield num

nums = [0, -1, -4, -9, -16, -25, -36, -49]
result = Filter3(Filter2(Filter1(nums)))
for num in result:
    print(num, end=' ')

# 0 -12 -48 -108  -> correct output
# 0 -48 -12 -108
# 12 -48 0 -108
# TypeError