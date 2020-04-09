name =['Rakesh','Parul','Mihir','Nikhil']
print(len(name))              
print(name)

print(name[:2])               #slicing
print(name[2:])
print(name[-1])               # here -1 index means the last index. it is useful when index is not known

name.append("vinu")
name.insert(4,'bhavesh')

name_2=['Hemant','Krishna','Riddhi']

name.append(name_2)
print(name)

name.remove(name_2)           
print(name)

name.append('kanchan')

name.append('daji')
popped_name=name.pop()
print(popped_name)

name.extend(name_2)
print(name)

name_2.reverse()
print(name_2)

name.sort()
print(name)
name.sort(reverse=True)
print(name)

new_list=sorted(name)
print(name)
print(new_list)

#min,max,sum for ints

new_list.index('Mihir')

print('Mihir' in new_list)

for index,item in enumerate(new_list,start=1):
     print(index, item)

list_str = ', '.join(new_list)
print(list_str)

new_list=list_str.split(' - ')

#lists are mutable
#tuples are immutable

tuple1=(8,5,4,9,3,7)
tuple2=tuple1

print(tuple1)
print(tuple2)

#print(dir(tuple1))
#tuple1[0]=1             #but it is immutable
#they are used for unchanging lists

#sets
s1={1,3,4,2}
print(s1)

s1.add(1)
print(s1)

print(1 in s1)           #efficient then lists or tuples

s2={2,4,6,8}

s1.intersection(s2)
s1.difference(s2)
s1.union(s2)
s1.issubset(s1)
s1.__xor__(s2)

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
#empty_set = {} # This isn't right! It's a dict
empty_set = set()