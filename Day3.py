my_list=list(input("Enter your list:"))    #input list
print(my_list)
print()

print(type(my_list))   #type of list
print()

my_list1=["Red","Green","Yellow","Blue"]        #string list
my_list2=[1,2,3,4,5,6,7,8,9]                    #integer list
my_list3=[True,True,False]                      #boolean list
my_list4=["Mango","Yellow",1,5,7,2,True,False]  #mix list
print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)
print()

print(type(my_list1))                           #type of list
print(type(my_list2)) 
print(type(my_list3)) 
print(type(my_list4))

print()
print(len(my_list))                             #lenght of list
print(len(my_list1)) 
print(len(my_list2)) 
print(len(my_list3)) 
print(len(my_list4))
print()

my_list5=list(("HELLO","WORLD"))                
print(my_list5)
print()

fruits=["Apple","Mango","Kiwi","Orange","Apple","Mango","Kiwi","Orange"]
print(fruits)
print()

fruits.append("Grapes")                     #append item
print(fruits)
print()

fruits.append(input("Enter the fruit you want to add:"))                     #append item
print(fruits)
print()

fruits.remove("Mango")                      #remove item
print(fruits)
print()

fruits.remove(input("Enter the fruit you want to remove:"))                      #remove item
print(fruits)
print()

fruits.copy()                               #copy of list
print(fruits)
print()

fruit=fruits.count("Orange")                #count the item
print(fruit)
print()

fruit=fruits.count(input("Enter the fruit you want to count:"))                #count the item
print(fruit)
print()

cars=["TATA","Creta","Mahindra","Kia","Audi"]           #Extend list to other list
fruits.extend(cars)
print(fruits)
print()

fruits.extend("Pineapple")                              #Extend list to other list
fruits.extend(cars)
print(fruits)
print()

fruits.extend(input("Enter the fruit you want to extend:"))     #Extend list to other list
print(fruits)
print()

ind_val=fruits.index("Apple")               #check the index number
print(ind_val)
print()

ind_val=fruits.index(input("Enter the fruit name check the index number: "))    #check the index number
print(ind_val)
print(ind_val)
print()

fruits.insert(2,"Watermelon")           #insert at specified position
print(fruits)
print()

ind_num=int(input("Enter the index number to insert an element: "))    #insert at specified position
value=str(input("Enter the fruit nameto insert an element: "))
fruits.insert(ind_num,value)
print(fruits)
print()

fruits.pop(2)               #Pop the element from the list
print(fruits)
print()

ind_v=int(input("Enter the inex number of the fruit you want to pop: "))   #Pop the element from the list
fruits.pop(ind_v)
print(fruits)
print()

fruits.remove("Apple")               #Pop the element from the list
print(fruits)
print()

ind_v=str(input("Enter the name of the fruit you want to remove: "))   #Pop the element from the list
fruits.remove(ind_v)
print(fruits)
print()

fruits.reverse()                    #Reverse the list
print(fruits)
print()

fruits.sort()                       #Sort the list
print(fruits)
print()

num=[1,2,3,4,5,6,7,8,9]               # Accessing & Slicing  
print(num[2])

print(num[2:5])

print(num[:5])

print(num[2:])

print(num[::2])

print(num[1:8:2])

print(num[-2])

print(num[-5:-2])

print(num[:-5])

print(num[-2:])

print(num[::-2])

print(num[-1:-8:-2])





this_tuple1=(1,2,3,4,5,6,7,8,9)           #tuples types
print(this_tuple1)
print(len(this_tuple1))
print(type(this_tuple1))

this_tuple2=("Hello","World")
print(this_tuple2)
print(len(this_tuple2))
print(type(this_tuple2))

this_tuple3=(True,True,False)
print(this_tuple3)
print(len(this_tuple3))
print(type(this_tuple3))

this_tuple4=("apple",)
print(this_tuple4)
print(len(this_tuple4))
print(type(this_tuple4))

this_tuple5=("apple")
print(this_tuple5)
print(len(this_tuple5))
print(type(this_tuple5))

this_tuple6=("apple","Yellow",1,2,True)
print(this_tuple6)
print(len(this_tuple6))
print(type(this_tuple6))

this_tup=tuple(("Yellow","Red","Green","Orange"))
print(this_tup)

colors=("Red","Black","White","Green","Blue")
print(colors)
print(colors[2])
print(colors[2:])
print(colors[:2])
print(colors[1:4])

print(colors[-2])
print(colors[-2:])
print(colors[:-2])
print(colors[-4:-1])

print(colors[1:4:2])
print(colors[-1:-4:-2])

colors[1],colors[4]==colors[4],colors[1]            #does not change value
print(colors)               

new_colors=list(colors)                 #Update
new_colors[3]="grey"
print(tuple(new_colors))

new_colors=list(colors)                 #append
new_colors.append("Olive Green")
print(tuple(new_colors))

new_colors=list(colors)                 #remove
new_colors.remove("Blue")
print(tuple(new_colors))

new_colors=list(colors)                 #pop
new_colors.pop(2)
print(tuple(new_colors))

new_colors=list(colors)                 #clear
new_colors.clear()
print(tuple(new_colors))

del colors()
print(colors)       #Error because tuple is no longe exist

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry","Lemon","kiwi","Watermelon",)

(green, yellow,*red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry","Lemon","kiwi","Watermelon",)

(green,*yellow,red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry","Lemon","kiwi","Watermelon",)

(*green,yellow,red) = fruits

print(green)
print(yellow)
print(red)


thistuple = ("apple", "banana", "cherry")           #loops
for i in range(len(thistuple)):
  print(thistuple[i])

i=0
while(i<len(thistuple)):
     print(thistuple[i])
     i=i+1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
                                        #dict
this_dict={                     
    "Name":"Apple",
    "Color":"Red",
    "Category":"Fruit",   
    "Color":"Apple Red",        #print this value because duplicats are not allowed
    "Benefits":["brain health","weight management"]
}
print(this_dict)
print(this_dict["Color"])
print(len(this_dict))
print(type(this_dict))
print()
x=this_dict.get("Category")             #loops
print(x)
x=this_dict.keys()
print(x)
x=this_dict.values()
print(x)
x=this_dict.keys()
this_dict["protect from"]="heart disease"
print(x)
print(this_dict)
if "protect from" in this_dict:
    print("Yes value is available in this dict")
else:
    print("Not available")
this_dict["protect from"]="heart disease"
print(this_dict)

flowers={"Rose","Jasmine","Lily","Orchid",}
print(flowers)
flowers={"Rose","Jasmine","Lily","Orchid","Rose"}  #duplicate values are not allowed
print(flowers)
print(len(flowers))
print(type(flowers))

set1 = {"apple", "banana", "cherry"}
print(set1)
print(type(set1))
set2 = {1, 5, 7, 9, 3}
print(set2)
print(type(set2))
set3 = {True, False, False}
print(set3)
print(type(set3))

set4={"Apple","Cherry",5,9,1,False}
print(set4)
for x in flowers:
    print(x)
print("Rose" in flowers)
flowers.add("Sunflower")
print(flowers)
flowers.pop()
print(flowers)
newflowers={"Tulip","Marigold"}
flowers.update(newflowers)
print(flowers)
flowers.remove("Orchid")
print(flowers)
