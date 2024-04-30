# create a list of 5 names
names=['Anil','Amol','Aditya','Avi','Alka']
print(names)
#insert a name 'Anuj before aditya'
names.insert(2,'Anuj')
print(names)
#append a name 'Zulu'
names.append('Zulu')
print(names)
# replace 'Anil with' 'Anilkumar'
i= names.index('Anil')
names[i] ='Anilkumar'
print(names)
#sort all the names in the list
names.sort()
print(names)
#print revered sorted list
names.reverse()
print(names)
