# coding:utf-8
'''
排序算法实现
1.插入排序
2.希尔排序
3.选择排序
4.冒泡排序
5.归并排序
6.快速排序

'''
def insert_sort(nums):
    l = len(nums)
    '''
    for i in range(1,l):
        tmp = nums[i]
        j = i
        while j > 0 and nums[j-1] > tmp:
            nums[j] = nums[j-1]
            nums[j-1] = tmp
            j -= 1
    '''
    for i in range(1, l):
        if nums[i-1] > nums[i]:
            tmp = nums[i]
            nums.pop(i)
            for j in range(i-1,-1,-1):
                if tmp > nums[j]:
                    nums.insert(j+1, tmp)
                    break
                if j == 0:
                    nums.insert(j, tmp)
    return nums


#希尔排序
def shell_sort(nums):
    l = len(nums)
    dk = l//2
    while dk > 1:
        for i in range(dk,l):
            if nums[i] < nums[i-dk]:
                nums[i], nums[i-dk] = nums[i-dk], nums[i]
        dk = dk // 2
    return insert_sort(nums)

 #选择排序
def select_sort(nums):
    res = []
    l = len(nums)
    while 0 < l:
        res.append(min(nums))
        nums.remove(min(nums))
        l -= 1
    return res


#冒泡排序
def bubble_sort(nums):
    h = len(nums) - 1
    l = 0
    while l < h:
        i = 0
        while i < h:
            if nums[i] > nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
            i += 1
        h -= 1
    return nums

#归并排序
def merge(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    if i == len(a) and j < len(b):
        res.extend(b[j:])
    elif j == len(b) and i < len(a):
        res.extend(a[i:])
    return res

def merge_sort(nums):
    n = len(nums)
    if n == 1:
        return nums
    else:
        left = merge_sort(nums[:n//2])
        right = merge_sort(nums[n//2:])
    return merge(left, right)

#快速排序
def partition(nums, left, right):
    x = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[right] = nums[right], nums[i + 1]
    return i+1

def quick_sort(nums, left, right):
    if left >= right:
        return
    mid = partition(nums, left, right)
    quick_sort(nums, left, mid-1)
    quick_sort(nums, mid+1, right)
    return nums



