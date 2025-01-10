def merge_sort(arr, names):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_names = names[:mid]
        right_names = names[mid:]

        merge_sort(left_half, left_names)
        merge_sort(right_half, right_names)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                names[k] = left_names[i]
                i += 1
            else:
                arr[k] = right_half[j]
                names[k] = right_names[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            names[k] = left_names[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            names[k] = right_names[j]
            j += 1
            k += 1

# 初始化数据
names = ["张", "李", "陈"]
scores = [120, 107, 132]

# 使用归并排序按照分数排序
merge_sort(scores, names)

# 打印排序后的结果
for i in range(len(names)):
    print(names[i], scores[i], "分")