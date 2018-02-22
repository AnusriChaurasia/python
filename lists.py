""" using list and including a list in another"""
list=[1,2,3]
fruits=["banana","apple","grapes",list]  # a list is included in other
print(fruits[2][2])
print(fruits+list)
print("the list is ",fruits)             # prints the items in list fruits
b=3
c=fruits[b]                              # specifies an item in fruits
a=print(fruits[b])
print("the item number",b,"is",c)
