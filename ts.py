import timeit
from time import sleep
# def maopao_sort(alist):
#     """mao pao pai xv"""
#     for cm in range(len(alist)-1,0,-1):
#         for cn in range(cm):
#             if alist[cn]>alist[cn+1]:
#                 temp = alist[cn+1]
#                 alist[cn+1] = alist[cn]
#                 alist[cn] = temp
def maopao_sort():
    """mao pao pai xv"""
    a = [11,12,20,10,9,8,7,30,6,5,4,3,2,1,40,1200,400,500,4210,78129,12984,0]
    for cm in range(len(a)-1,0,-1):
        for cn in range(cm):
            if a[cn]>a[cn+1]:
                temp = a[cn+1]
                a[cn+1] = a[cn]
                a[cn] = temp

def k_maopao_sort():
    """k mao pao pai xv"""
    a = [11,12,20,10,9,8,7,30,6,5,4,3,2,1,40,1200,400,500,4210,78129,12984,0]
    passnum = len(a) -1
    exchange = True
    while passnum >0 and exchange:
        exchange = False
        for cn in range(passnum):
            if a[cn]>a[cn+1]:
                exchange = True
                temp = a[cn+1]
                a[cn+1] = a[cn]
                a[cn] = temp
        passnum -=1

def selection_sort():
    """xuan ze pai xv"""
    a = [11,12,20,10,9,8,7,30,6,5,4,3,2,1,40,1200,400,500,4210,78129,12984,0]
    for cm in range(len(a)-1,0,-1):
        position_max = 0
        for location in range(1,cm+1):
            if a[location]>a[position_max]:
                position_max = location
        temp = a[cm]
        a[cm] = a[position_max]
        a[position_max] = temp

def insertion_sort():
    """cha ru pai xv"""
    a = [11,12,20,10,9,8,7,30,6,5,4,3,2,1,40,1200,400,500,4210,78129,12984,0]
    for index in range(1,len(a)):
        current_value = a[index]
        position = index
        while position > 0 and a[position-1]>current_value:
            a[position] = a[position-1]
            position = position -1
        a[position] = current_value

def shell_sort():
    """shell sort pai xv"""
    a = [11,12,20,10,9,8,7,30,6,5,4,3,2,1,40,1200,400,500,4210,78129,12984,0]
    sublist_count = len(a)//4
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a,start_position,sublist_count)
        sublist_count = sublist_count//4
    return a
def gap_insertion_sort(a,start_position,sublist_count):
    """gap insertion sort"""
    for index in range(start_position+sublist_count,len(a),sublist_count):
        current_value = a[index]
        position = index
        while position >= sublist_count and a[position-sublist_count]>current_value:
            a[position] = a[position-sublist_count]
            position = position -sublist_count
        a[position] = current_value

a = [11,12,20,10,9,8,7,30,6,5,4,3,2,1,40,1200,400,500,4210,78129,12984,0]
insertion_sort()

T1 = timeit.Timer("maopao_sort()","from __main__ import maopao_sort")
T2 = timeit.Timer("k_maopao_sort()","from __main__ import k_maopao_sort")
T3 = timeit.Timer("selection_sort()","from __main__ import selection_sort")
T4 = timeit.Timer("insertion_sort()","from __main__ import insertion_sort")
T5 = timeit.Timer("shell_sort()","from __main__ import shell_sort")
print("maopao: ",T1.timeit(10000))
print("K—maopao: ",T2.timeit(10000))
print("selection: ",T3.timeit(10000))
print("insertion: ",T4.timeit(10000))
print("shell: ",T5.timeit(10000))
# print(len(a))
# print(shell_sort())


