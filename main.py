# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#   Task 7**********************
#   Q1
# def print_row(num):
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print(j,end =' ')
#         print( )
# num = int(input("Enter the rows "))
# print_row(num)
# Enter the rows 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Q2 *****************************************
# def sum(num):
#     sum_num =0
#     for i in range(1,num+1):
#         sum_num +=i
#     print("sum is = "+str(sum_num))
# num = int(input("Enter the number : \n"))
# sum(num)
# Q3 **************************
# def print_name1(name):
#     for i in range(len(name)-1):
#          for j in range(i+1):
#              print(name[j],end =' ')
#
#          print( )
#
# def print_name2(name11):
#   for i in range(len(name11)) :
#       for j in range(len(name11)-i):
#           print(name[j], end=' ')
#       print( )
#
# name = input("Enter the name : ")
# print_name1(name)
# print_name2(name)
# b
# b a
# b a r
# b a r a
# b a r a a
# b a r a
# b a r
# b a
# b
# Q4 **************************
# def reverse_nam(name):
#     for index in range(len(name)):
#        print(name[(len(name)-1)-index],end ='')
# name = input("Enter thr name you want to reverse : ")
# reverse_nam(name)

# Q 5 **********************************
# def reverse_num(num):
#     for index in range(0,num):
#         print((num)-index, end = ' ')
# number =int (input("Enter thr number you want to reverse : "))
# reverse_num(number)
# Q 6 ***************************************
# def mult(n):
#    if n > 0:
#      for x in range(1,11):
#       print(x * n)
# n = int(input('enter the number ' ))
# mult(n)
# Q 7 ******************************
# def multpl(limit,target,max):
#     for x in range(1,limit):
#      print(target*x)
#      if x == max:
#          break
#
# limit = int(input('enter the number of limit ' ))
# max= int(input('enter the  max number ' ))
# target = int(input('enter the target number ' ))
# multpl(limit,target,max)
