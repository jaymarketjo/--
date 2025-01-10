def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 分解数组
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 递归排序左右子数组
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # 合并已排序的左右子数组
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 测试归并排序算法
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("归并排序后的数组：", sorted_arr)