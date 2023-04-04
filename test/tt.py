# coding=utf-8
# def bubble_sort(array):
#     """冒泡排序"""
#     n = len(array)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j + 1], array[j] = array[j], array[j + 1]
#     print(array)
#
#
# if __name__ == "__main__":
#     a = [23, 32, 45, 78, 543, 67, 42, 46, 90, 43, 21, 57]
#     bubble_sort(a)

for i in range(1, 10):
    """九九乘法表"""
    for j in range(1, i + 1):
        print("{}*{}={}".format(j, i, i * j), end="\t")
    print()
