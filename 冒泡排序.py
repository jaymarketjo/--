def bubble_sort(arr):
    n = len(arr)
    
    # 遍历数组元素
    for i in range(n):
        # 标记是否发生交换
        swapped = False
        
        # 每次遍历将最大的元素“浮”到末尾
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # 交换元素
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # 如果没有发生交换，表示数组已经有序，提前结束排序
        if not swapped:
            break
    
    return arr

# 测试冒泡排序算法
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("排序后的数组：", sorted_arr)