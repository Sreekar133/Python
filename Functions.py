# def multiply(a,b):
#     result = a*b
#     return result
#
#
# answer = multiply(2,3)
# print(answer)
# print(type(answer))
#
#
# for i in range(1,5):
#     result = multiply(2,i)
#     print(result)

# s = input("enter the string :")
#
# if s == s[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")


def palindrome(c):
    return c[::-1].casefold() == c.casefold()

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char


    return d[::-1].casefold() == d.casefold()


d = input("enter the word to check :")

if palindrome_sentence(d):
    print("{} is a palindrome".format(d) )
else:
    print("{} is not a palindrome".format(d))




