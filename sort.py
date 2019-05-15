"""任意两项位置的函数swap"""
def swap(list, i, j):
    """交换list 的i j位置元素"""
    list[i], list[j] = list[j], list[i]
    return list

list = [7, 3, 2, 4, 7, 5, 1, 9, 1]
#print(swap(list, 2, 3))

"""选择排序"""
def small_to_large1(s):
    new_list, j = s, 0
    while len(new_list) > 1:
        s = [swap(s, i, j) for i in range(j, len(s)) if s[i] == min(new_list)][0]  # s中一个数字可能出现多次，这里只取for循环中第一次出现得到的结果
        j = j + 1
        new_list = s[j:]
    return s

def small_to_large2(s):
    new_list, k = s, len(s)
    while len(new_list) > 1:
        s = [swap(s, i, k-1) for i in range(k) if s[i] == max(new_list)][0]  # s中一个数字可能出现多次，这里只取for循环中第一次出现得到的结果
        k = k - 1
        new_list = s[:k]
    return s

#print(small_to_large2(list))


"""改进的选择排序"""
def small_to_large_improv(s):
    new_list, j, k = s, 0, len(s)
    while len(new_list) > 2:
        s = [swap(s, i, j) for i in range(j, k) if s[i] == min(new_list)][0]
        j = j + 1
        s = [swap(s, i, k-1) for i in range(j, k) if s[i] == max(new_list)][0]
        k = k - 1
        new_list = s[j: k]
    return s
# print(small_to_large_improv(list))



"""冒泡排序"""
def bubble_sort(s):
    i, j = 1, len(s)
    while j > 0:
        while i < j:
            s = swap(s, i-1, i) if s[i-1] > s[i] else s
            i = i + 1
        j = j - 1
    return s
# print(bubble_sort(list))


"""冒泡排序改进"""
def bubble_sort_improv(s):
    j = len(s)
    while j > 0:
        if s[j-1] == max(s[:j]):
            s = s
        else:
            i = 1
            while i < j:
                s = swap(s, i-1, i) if s[i-1] > s[i] else s
                i = i + 1
        j = j - 1
    return s
print(bubble_sort_improv(list))


"""插入排序法"""
def insertation_sort(s):
    i = 1
    while i <= len(s):
        s_i, s_rest = small_to_large1(s[:i]), s[i:]
        s, i = s_i + s_rest, i + 1
    return s
#print(insertation_sort(list))



"""在成顺序的list中插入num"""
def insertation(list, num):
    i = 0
    while list[i] <= num:
        i = i + 1
    pred_list = list[:i]
    rest_list = list[i:]
    return pred_list + [num] + rest_list
# print(insertation([1,2,3,4,5,7,8,9], 6))

