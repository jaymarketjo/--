#import math

# 使用dir()查看模块中的所有功能
#print(dir(math))

# 使用help()获取特定功能的详细信息
#help(math.sqrt)

#print(math.sqrt(16))  # 使用math模块中的sqrt函数计算平方根

import json
import math

# 使用dir()查看模块中的所有功能
module_functions = dir(math)

# 将列表转换为JSON格式并打印出来
json_module_functions = json.dumps(module_functions, indent=4)
print(json_module_functions)
help(math.sqrt)