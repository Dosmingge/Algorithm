import random
def Partition(li, low, height):
    pivotkry = li[low]
    while low<height:
        while low<height and li[height]>pivotkry:
            height -= 1
        li[low] = li[height]
        while height>low and li[low]<pivotkry:
            low += 1
        li[height] = li[low]
    li[low] = pivotkry
    return low


def QSort(li, low, height):
    """
    快排
    :param li:
    :param low:
    :param height:
    :return:
    """

    if low<height:
        pivotloc = Partition(li, low, height)
        QSort(li, low, pivotloc-1)
        QSort(li, pivotloc+1, height)
    return li



if __name__ == "__main__":
    a = []
    for i in range(20):
        a.append(random.randint(0,999))
    h = len(a)
    print(QSort(a, 0, h-1))
