# append(value) to add new items in the list in the end

marks=[90,91,94,"maths"]
marks.append(40)
print(marks)

# insert(index,value) to add in the starting of the list 

marks.insert(0,44)
print(marks)

#in keyword checks the existence  boolean
print(90 in marks)

# len(list) lenght of the list
print("lenght  " + str(len(marks)))

# while loop for printing list
i=0
while i<len(marks) :
  print(marks[i])
  i=i+1

# clear
marks.clear()
print(marks)

