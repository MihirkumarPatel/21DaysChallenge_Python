message='hey... there...'
name='name'

print(len(message))

#slicing  
print(message[:3])            
print(message[2:])

print(message.capitalize)

print(message.lower())
print(message.upper())

print(message.count('h'))
print(message.find('hey'))

name=name.replace('name','Mihir')
print(name)

news=message + ' ' + name.upper() + " how are you?"
print(news)
news="{} {} how are you?".format(message,name.upper())
print(news)
news=f"{message} {name.upper()} how are you?"
print(news)

print(dir(message))           #with this we can se all the method which can be useb on the object passed

print(help(str))              #it shows which method used for what and whch arguement is passed

print(help(str.find))         #it shows detail for one particular method