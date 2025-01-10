def bubble_sort(scores, names):
    n = len(scores)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j] > scores[j+1]:
                scores[j], scores[j+1] = scores[j+1], scores[j]
                names[j], names[j+1] = names[j+1], names[j]

# 初始化数据
names = ["张", "李", "陈"]
scores = [120, 107, 132]

# 使用冒泡排序按照分数排序
bubble_sort(scores, names)

# 打印排序后的结果
for i in range(len(names)):
    print(names[i], scores[i], "分")