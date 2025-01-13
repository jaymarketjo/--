import random  # 导入random模块，用于生成随机数

def guess_number_game():
    print("欢迎来到猜数字游戏！")
    lower_bound = 1  # 设置初始猜测范围的下界
    upper_bound = 100  # 设置初始猜测范围的上界
    secret_number = random.randint(lower_bound, upper_bound)  # 生成一个1到100之间的随机整数作为秘密数字
    attempts = 0  # 初始化猜测次数为0

    while True:  # 进入游戏循环
        print(f"猜测范围：[{lower_bound}, {upper_bound}]")  # 显示当前猜测范围
        guess = int(input("请输入一个整数: "))  # 获取玩家的猜测
        attempts += 1  # 猜测次数加1

        if guess < secret_number:  # 如果猜测小于秘密数字
            print("猜小了，再试试吧！")  # 提示玩家猜小了
            lower_bound = guess + 1  # 调整猜测范围的下界
        elif guess > secret_number:  # 如果猜测大于秘密数字
            print("猜大了，再试试吧！")  # 提示玩家猜大了
            upper_bound = guess - 1  # 调整猜测范围的上界
        else:  # 如果猜测正确
            print(f"恭喜你，猜对了！你用了{attempts}次机会猜中了数字{secret_number}！")  # 提示玩家猜中了
            break  # 结束游戏循环

if __name__ == "__main__":
    guess_number_game()  # 调用猜数字游戏函数开始游戏

#(在Python中，if __name__ == "__main__": 是一个常见的用法，用于判断当前模块是否作为主程序运行。让我解释一下这段代码的意义：
#当一个Python文件被直接运行时，Python会将特殊变量__name__设置为"__main__"，表示该文件是主程序。
#如果一个Python文件被导入到另一个文件中，则__name__会被设置为该文件的模块名，而不是"__main__"。
#因此，通过使用if __name__ == "__main__":，我们可以判断当前模块是否是主程序，如果是主程序，则执行相应的代码块。
#在上面的代码示例中，if __name__ == "__main__": 的作用是确保guess_number_game()函数只有在当前文件作为主程序运行时才会被调用，而不会在该文件被导入到其他文件时执行。这样可以避免在导入时自动执行游戏逻辑。
#希望这个解释能够帮助您理解if __name__ == "__main__":的作用。如果您有任何其他问题或疑问，请随时告诉我！)