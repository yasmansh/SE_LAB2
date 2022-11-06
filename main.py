from bubbleSort import *
from mergeSort import *

my_arr = [12, 14, 5, 7, 13, 72, 55, 11]
print('Before Bubble Sort: ' + str(my_arr))

result1 = bubbleSort(my_arr)
print('After Bubble Sort: ' + str(result1))

my_arr = [12, 14, 5, 7, 13, 72, 55, 11]
print('Before Merge Sort: ' + str(my_arr))
mergeSort(my_arr)
print('After Merge Sort: ' + str(my_arr))