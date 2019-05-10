# Tutorial 1
# --------------  Input and Output
name = input("Enter your name:")
print("Hey, it's",name, "-- hello!")

fname = input("Input your first name:")
lname = input("Input your last name")
print("Hello " + lname + " " + fname)

num1 = input('Enter first number')
num2 = input('Ener second number')
sum = float(num1) + float(num2)
print("The sum of {0} and {1} is {2}".format(num1,num2,sum))

filename = input("Input the filename: ")
f_extns = filename.split(".")
print("The extension of the file is " + repr(f_extns[-1]))

a = int(input("Input an integer:"))
n1 = int("%s" % a)
n2 = int("%s%s" %(a,a))
n3 = int("%s%s%s" %(a,a,a))
print(n1+n2+n3)

l = []
if not l:
    print("List is empty")
else:
    print("List has values")

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
text = input("Input your text: ")
n = int(input("Input the number letter in words you want to find: "))
print(long_words(n, text))

color_list = ["Red","Green","White","Black"]
print("%s %s"%(color_list[0],color_list[-1]))

# ------------------------------------------------- Loop and list
n = int(input("Enter the number of students: "))
a =[]
for i in range(0,n):
    elem=int(input("Enter mark"))
    a.append(elem)
avg=sum(a)/n
print("Average of marks in the list", round(avg,2))


n=int(input("Enter the number of students: "))
a=[]
i=0
while(i<n):
    elem=int(input("Enter mark:"))
    a.append(elem)
    i = i + 1
avg=sum(a)/n
print("average of marks in the list", round(avg,2))


def match_words(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0]== word[-1]:
            ctr += 1
    return ctr
print(match_words(['abc','xyz','aba','1221']))


def match_words(words):
  ctr = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr
n = int(input("Enter the number of words you like to test: "))
a=[]
for i in range(0,n):
    wrd = input("Enter a word: ")
    a.append(wrd)
print(match_words(a))


a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(dup_items)


def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


# ----------------------------------- Conditional decision / branching
n=int(input("Enter the number of students: "))
c=0
a=[]
odds=[]
for i in range(0,n):
   elem=int(input("Enter mark: "))
   a.append(elem)
   if elem%2 == 1:
       odds.append(elem)
       c+=1
avg=sum(odds)/c
print("Average of odd marks in the list", round(avg,2))


n=int(input("Enter the number of elements: "))
num = []
for i in range(0,n):
   elem=int(input("Enter a number: "))
   num.append(elem)
odds = [x for x in num if x%2!=0]
print(odds)


user_input = input("Enter the password: ")
system_pw = "pw@python"
if user_input == system_pw:
   print("Welcome to the system!")
else:
   print("Sorry, the password is wrong. You are not permitted to enter the system.")


def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2
print(second_smallest([-1, 4, -3, 1, 5, 2, -8, -2, 0]))


# ----------------------------------- Using extra packages
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


from math import pi
r = float(input ("Input the radius of the circle : "))
a = pi * r**2
print ("The area of the circle" + " is: " + str(a))


from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
