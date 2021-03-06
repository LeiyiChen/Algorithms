# 排序算法总结
参考：
1.https://www.cnblogs.com/RainyBear/p/5258483.html
2.https://blog.csdn.net/sunxianghuang/article/details/51872360

##外部排序：排序的数据过大，一次不能容纳全部的排序记录，在排序过程中需要访问外存。
##内部排序：
插入类排序
- 插入排序
- 希尔排序

选择类排序
- 选择排序
- 堆排序

交换类排序
- 冒泡排序
- 快速排序

归并类排序
- 归并排序

|排序方法|平价情况|最好情况|辅助空间|
|冒泡排序|O(n^2)|O(n)|

##1.插入排序
插入排序工作原理是通过构建有序序列，对于未排序的数据，在已排序序列中从后向前扫描，找到相应位置并插入。
算法步骤：
从索引为1开始遍历待排序序列，用变量i来记录遍历的位置，为了后续比较方便，使用tmp临时存放每一个nums[i]的值。根据算法的思想，变量i之前的序列一定是有序且增序的序列，那么只要后序遍历中遇到一个nums[i] < nums[i-1]，则就要将nums[i]插入到前面合适的位置。所以这里引入变量j用来查找前i个位置中，nums[i]需要插入的位置，即j的初始值为i，只要nums[i]也就是tmp小于nums[j],将nums[j-1]后移到nums[j],而nums[j-1]用来存储tmp，j--。直到j=0或者nums[j-1]>tmp，则插入成功。这是典型的数组移动方法，通过不停后移来实现。但是在Python中我们可以实现得更友好，使用list的pop和insert。
Python代码实现：
```python
def insert_sort(nums):
    l = len(nums)
    if l == 0 or l == 1:
        return nums
    for i in range(1, l):
        if nums[i] < nums[i - 1]:
            temp = nums[i]
            for j in range(i - 1, -1, -1):
                if temp < nums[j]:
                    nums[j + 1] = nums[j]
                    if j == 0:
                        nums[j] =temp
                else:
                    nums[j + 1] = temp
                    break
    return nums
```
改进一下：
```python
def insert_sort(nums):
    l = len(nums)
    for i in range(1, l):
        tmp = nums[i]
        j = i
        while j > 0 and nums[j-1] > tmp:
            nums[j] = nums[j-1]
            j -= 1
            nums[j] = tmp
    return nums
```
以上版本是C语言版，让我们用python的方式来实现。emmm...我脑子一根筋，左写右写都是第一个版本的思路。
```python
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
```
分析：最坏时间复杂度是逆序，为O(n^2)。最好时间复杂度为数组正序O(n)。平均时间复杂度O(n^2),空间复杂度为O(1)。是稳定排序。

## 折半插入排序
由于插入排序的基本操作是在一个有序表中进行查找和插入，那么这个查找操作可以使用折半操作来进行。称为折半查找排序(Binary Insection Sort)。折半插入排序空间复杂度无变化，但是减少了关键字的比较次数，但记录的移动次数不变。时间复杂度不变。


## 2.希尔排序
也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
- 插入排序在对几乎已经排好序的数据操作时，效率高，即可达到线性排序的效率。
- 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

基本思想是：直接插入排序中，如果元素X初始化时所处的位置为i，排序后所处位置为j，那么元素x必须要经过j-i-1(j>=i)次移动。而希尔排序中，我们先取一个小于n的整数d1作为第一个增量，把数据的全部记录分组。所有距离为d1的记录放在同一个组中。先在各组内进行直接插入排序；然后，取第二个增量d2< d1重复上述的分组和排序，直至所取的增量di =1( di < di-1 …< d2< d1)，即所有记录放在同一组中进行直接插入排序为止（这时候数组已经基本有序）。平均情况下，因为分组的增量>=1，元素X从初始化位置移动到最终位置所需要的次数比原来要小。
![希尔排序示意图](https://img-blog.csdn.net/20160710201252022?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

算法步骤：
1）选择一个增量序列t1,t2,t3,...,tk，其中ti>tj,tk=1;
2)按增量序列个数k，对序列进行k躺排序；
3）每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m的子序列，分别对各子表进行直接插入排序。仅增量因子为1时，整个序列作为一个表来处理，表长度即为整个序列的长度。

代码实现：
```python
def shell_sort(nums):
    l = len(nums)
    dk = l//2
    while dk > 1:
        for i in range(dk):
            if nums[i] > nums[i+dk]:
                nums[i], nums[i+dk] = nums[i+dk], nums[i]
        dk = dk // 2
    return insert_sort(nums)
```

分析：最坏时间复杂度为O(n^2)；最优时间复杂度为O(n)；平均时间复杂度为O(n^1.3)。辅助空间O(1)。稳定性：不稳定。希尔排序的时间复杂度与选取的增量有关，选取合适的增量可减少时间复杂度。
希尔排序非常容易实现，算法代码短而简单。 此外，希尔算法在最坏的情况下和平均情况下执行效率相差不是很多，与此同时快速排序在最坏的情况下执行的效率会非常差。专家们提倡，几乎任何排序工作在开始时都可以用希尔排序，若在实际使用中证明它不够快，再改成快速排序这样更高级的排序算法。

## 3.选择排序
选择排序(Selection sort)也是一种简单直观的排序算法。
算法步骤：
1）首先在未排序序列中找到最小(大)元素，存放到排序序列的起始位置。
2）再从剩余未排序元素中继续寻找最小(大)元素，然后放到已排序序列的末尾。
3）重复第二步，直到所有元素均排序完毕。

Python实现从小到大排序。
```python
def select_sort(nums):
    res = []
    l = len(nums)
    while 0 < l:
        res.append(min(nums))
        nums.remove(min(nums))
        l -= 1
    return res
```
分析：选择排序时间复杂度为O(n^2)。传统的做法是将最小值与最小索引交换，因此为不稳定的排序方法，如[5,5,3]，第一次就将第一个5与3交换，导致最后第一个5挪到第二个5后面。但上述实现中我使用的是Python的方法，然后引入了一个新的数组res。。。。。。。这样的话不存在不稳定的现象。


## 4.冒泡排序
冒泡排序(Bubble Sort)也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
算法步骤：
1）比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2）对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3）针对所有的元素重复以上的步骤，除了最后一个。将大的沉底，故称为冒泡排序。
4）持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

Python实现
```python
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
```
分析：冒泡排序时间复杂度为O(n^2)。稳定。


## 5.归并排序
归并排序(Merge Sort)是建立在归并操作上的一种有效的排序算法。该算法是采用分治法的一个非常典型的应用。
分治法在每层递归时都有三个步骤：
1）分解原问题为若干子问题，这些子问题时原问题的规模较小的实例；
2）解决这些子问题，递归地求解子问题。若子问题的解足够小，则直接求解。
3）合并这些子问题的解成原问题的解。

归并排序完全遵循分治算法，其操作如下：
1）分解：分解待排序的n个元素的序列成各具n/2个元素的两个字序列；
2）解决：使用归并排序递归地排序两个子序列；
3）合并：合并两个已排序的子序列以产生已排序的答案。
当待排序的序列长度为1时，递归“开始回升”，在这种情况下不要做任何工作，因为长度为1的每个序列都已排好序。

实现时涉及两个函数，一个是用来合并有序数列的函数merge(a,b)。一个是归并排序函数merge_sort(nums)，这个函数执行过程中需要调用merge()函数，
merge函数算法步骤：
1）设定两个指针i,j，初始值为有序数组a,b的初始值。
2）比较两个指针所指的元素，较小的放在res数组中，然后该指针移动道下一个位置。
3）重复步骤2直到某一指针达到序列尾。
4）将另一个剩下的所有元素直接复制到合并序列尾。
merge_sort()函数算法步骤：
1）n = len(nums)
2)如果n为1，则返回nums。
3）否则left = merge_sort(nums[:n//2]),right = merge_sort(nums[n//2:])，返回merge(left,right)。
4）上一步中调用merge(left,right)返回了left数组和right数组排序后的结果。返回的是一个有序数组。因此再进行后续递归调用merge函数时，可以保证参数为有序数组。

Python实现
```python
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
```
分析：设数列长为N，将数列分开成小数列一共要logN步，每步都是一个合并有序数列的过程，时间复杂度记为O(N)，故归并排序时间复杂度为O(NlogN)。


## 6.快速排序
快速排序也使用了分治算法。
1）分解：数组nums被分解为两个子数组nums[p..q-1]和nums[q+1...r]（可能为空），使得nums[p...q-1]中的每一个元素都小于等于A[q]，而A[q]也小于等于A[q+1..r]中的每一个元素。
2）解决：通过递归调用快速排序，对子数组进行排序。
3）合并：因为子数组都是原址排序的所以不需要合并操作。

算法步骤：
1）从数列中挑出一个元素，称为”基准“，通常为数组最后一个元素（或者第一个元素）；
2）从前向后遍历数组，当遇到小于基准元素的元素时，把它和左边第一个大于基准元素的元素进行交换。再利用分治策略从已经分好的两组中分别进行以上步骤，直到排序完成。

python实现
```python
def partition(nums, left, right):
    x = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[right] = nums[right], nums[i + 1]
    return i+1

def quick_sort(nums, left, right):
    if left >= right:
        return
    mid = partition(nums, left, right)
    quick_sort(nums, left, mid-1)
    quick_sort(nums, mid+1, right)
    return nums
```
分析：最坏时间复杂度是O(n^2)，最优时间复杂度是O(nlogN)，平均时间复杂度O(nlogN)。不稳定的排序算法。空间复杂度O(nlogN)。


## 7.堆排序
简单选择排序的问题：没有把每一趟的比较结果保存下来，在后一趟的比较中，有许多比较在前一趟已经做过了。
1）堆及其特点
序列{k1,k2,...,kn}满足ki<=k2i,ki<=k2i+1，称为小顶堆。
序列{k1,k2,...,kn}满足ki>=k2i,ki>=k2i+1，称为大顶堆。其中i=1,2,...,n/2。
特点：小顶堆的堆顶（第一个元素）为最小元素，大顶堆的堆顶为最大元素。

2）判断序列是否构成堆
方法：用ki作为编号i的结点，画一棵完全二叉树，比较双亲和孩子容易判断是否构成堆。
例如判断序列[12,36,24,85,47,30,53,91]是否构成堆。
如图所示，为小顶堆。

[![](https://i.loli.net/2018/07/05/5b3dda9894fe8.png)](https://i.loli.net/2018/07/05/5b3dda9894fe8.png)

3）堆排序过程

[![](https://i.loli.net/2018/07/05/5b3ddd26ed12b.png)](https://i.loli.net/2018/07/05/5b3ddd26ed12b.png)

[![](https://i.loli.net/2018/07/05/5b3dde7d477db.png)](https://i.loli.net/2018/07/05/5b3dde7d477db.png)

Python实现
```python
# 堆排序
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if lchild < size and lists[lchild] > lists[max]:
        max = lchild
    if rchild < size and lists[rchild] > lists[max]:
        max = rchild
    if max != i:
        lists[max], lists[i] = lists[i], lists[max]
        adjust_heap(lists, max, size)  # 创建堆
def build_heap(lists, size):
    for i in range(0, (int(size / 2)))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists
```
分析：堆排序的时间复杂度是O(nlogN)。