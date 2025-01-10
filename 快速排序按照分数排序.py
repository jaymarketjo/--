def quick_sort(scores, names, low, high):
    if low < high:
        pivot_index = partition(scores, names, low, high)
        quick_sort(scores, names, low, pivot_index - 1)
        quick_sort(scores, names, pivot_index + 1, high)

def partition(scores, names, low, high):
    pivot = scores[high]
    i = low - 1
    
    for j in range(low, high):
        if scores[j] < pivot:
            i += 1
            scores[i], scores[j] = scores[j], scores[i]
            names[i], names[j] = names[j], names[i]
    
    scores[i+1], scores[high] = scores[high], scores[i+1]
    names[i+1], names[high] = names[high], names[i+1]
    
    return i + 1

# 初始化数据
names = ["张", "李", "陈"]
scores = [120, 107, 132]

# 使用快速排序按照分数排序
quick_sort(scores, names, 0, len(scores) - 1)

# 打印排序后的结果
for i in range(len(names)):
    print(names[i], scores[i], "分")