data = [1,2,3,4,5,6,87,98,34,54,65,32,70,11,12,1,3,1,4,15,250,150,50,350,360]

# del data[0:2]
# # print(data)
# #
# # del data[16:]
# # print(data)
#
# min_valid=100
# max_valid=200
#
# for index,value in enumerate(data):
#     if value < min_valid or value > max_valid :
#         del data[index]
#         index = index-1
#
# print(data)
#
#
# a=2
# b=3
#
# temp=a
# a=b
# b=temp
#
#
# print(a)
# print(b)

# p = 3

#
# if p > 1:
#     for i in range(2, int(p / 2) + 1):
#         if p % i == 0:
#             print(p, "it is not a prime number")
#             break
#     else:
#         print(p, "it is a prime number")

n=35

primes = []

for i in range(2,n+1):
    for j in range(2,i):
        if i % j==0:
            break
    else:
        primes.append(i)
print(primes)
