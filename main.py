#code
from bubbleSort import *
from mergeSort import *

inp1 = input().split()
nums = []
for item in inp1:
    nums.append(int(item))

mergeSort(nums)

print(nums)
