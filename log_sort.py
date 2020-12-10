from node import Node
from bilateral_link_list import BilateralLinkList
import random
import time

top_log_final_length = 10  # 榜单长度
type = 2  # 若type为1, 数据从输入行获取; 若type不为1，输入数据自动生成


def print_top_log(new_log, top_log):
    print("input item:", new_log, ";my top " + str(top_log_final_length) + " logs now is:", list(top_log.items()))


if __name__ == '__main__':
    top_log = BilateralLinkList()  # 权重榜单使用双链表
    my_logs = []
    tail = top_log.head
    top_log_length = top_log.length()
    while True:
        if type == 1:
            try:  # 检测输入数据类型
                new_log = int(input())
            except:
                print("error: please input integer")
                continue
        else:
            new_log = random.randint(0, 1000)
            time.sleep(1)

        my_logs.append(new_log)  # 保存日志在数据库(如果有的话)

        if top_log_length >= top_log_final_length and top_log.head.item > new_log:  # 若榜单已满，且新log权重小于首位权重
            print_top_log(new_log, top_log)
        else:
            top_log_length, top_log = top_log.add(new_log, top_log_length, top_log_final_length)
            print_top_log(new_log, top_log)
