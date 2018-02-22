""" counting back using for loop"""
for x in range(21):
    while(x<21):            #here x should be less than 21 since x is in range of 21 
        print(20-x) 
        break               # breaks the loop as without breakit continues to execute again and again
""" counting back using only while loop"""
num=20
while(num>=0):              # considers the value of num till it is greater than or equal to 0
    print(num)              
    num-=1                  # lessens the value of num after every execution
