input1 = int(input("Enter the value1 :")) #value1 taken from the user
input2 = int(input("Enter the value2 :")) #value2 taken from the user
input3 = int(input("Enter the value3 :")) #value3 taken from the user
input4 = int(input("Enter the value4 :")) #value4 taken from the user
input5 = int(input("Enter the value5 :")) #value5 taken from the user

x=open("Answer.txt","a")  #creating Answer.txt and appending all 5 values in that file
total=input1+input2+input3+input4+input5

print("Adding all values would be :",total)
print("Adding all  values would be :",total,file=x) 