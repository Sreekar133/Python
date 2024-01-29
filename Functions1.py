#def sum_eo(n,t):
#
#     if t=='e':
#         start =2
#     elif t=='o':
#         start =1
#     else:
#         return -1
#     return sum(range(start,n,2))
#
#
# x = sum_eo(11,'spam')
#
# print(x)
#
# def finonacci(n):
#     """Return the nth fibonacii number, for posotive 'n'"""
#     if 0 <= n <=1:
#         return n
#     n_minus1,n_minus2=1,0
#
#     for f n range(n-1):

#
# a = {"a" : "sreekar" , "b" : "reddy"}
#
# if type(a) == dict:
#         for i in a:
#             print(i)

#
# for i in range(0,5):
#      for j in range(0,i+1):
#         print("*" , end= "")
#      print("\n")
#

value_list=[]
d = { "a" : "sreekar" , "b" : "reddy" ,"c" :{"d" : "hello"}}
for i in d:
    if type(d[i]) ==dict:
         values(d[i])
    else:
        value_list.append(d[i])
print(value_list)


