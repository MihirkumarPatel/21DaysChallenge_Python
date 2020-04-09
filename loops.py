nums = [1, 2]

for num in nums:                             
     for letter in 'abc':
          if num == 1 and letter == 'b':
               continue
          if num == 2 and letter == 'b':
               break
          print(num,letter)

num=0
for num in range(1,4):
     print(num)

while num < 10:
     print(num)
     num += 1

# using enumerate also provides the use of a counter 
# when we use enumerate it returns [counter , value]
# it returns the things in the order described above
# so the use of enumerate is iterating through something(object) with provision of counter
