import random

def BubblesSort(li):
    """
    冒泡排序
    :param li:
    :return:
    """
    m = len(li)
    flag = 1
    while m>0 and flag == 1:
        flag = 0
        for i in range(m-1):
            if li[i]>li[i+1]:
                temp = li[i]
                li[i] = li[i+1]
                li[i+1] = temp
                flag = 1
        m -= 1
    return li



if __name__ == "__main__":
    a = []
    for i in range(20):
        a.append(random.randint(0,999))
    print(BubblesSort(a))

