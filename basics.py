# Numbers --------------------------------------------------

# myNum = 5+5
# print(myNum)

# myString = 'Hello World'
# x = myString.split('o')

# print(x)

# x = "Item One: {x} Item Two: {y}".format(x = "dog", y = "cat")
# print(x)

# String list ----------------------------------------------

# myList = [ 1, 2, 3]
# # myList = ['string',1,2,3,23.2,True,'asdf',[1,2,3]]

# print('Before')
# print(myList)

# # print(len(myList))

# myList[0] = 'New Item'
# print('After')
# print(myList)

# myList.append('New Item')
# print('Append')
# print(myList)

# myList.extend([ 'a', 'b', 'c'])
# print(myList)

# myList = [ 'a' , 'b', 'c']
# item = myList.pop()
# print(myList)
# print(item)

# myList.reverse()
# print(myList)

# myList = [1,2,['x','y','z']]
# print(myList[2][1])

# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# first_col = [row[0] for row in matrix]
# print(first_col)

# myStuff = {"key":"value", "key2":"value2","key3":{'123':[1,2,'grabMe']}}
# print(myStuff["key3"]["123"][2].capitalize())

# myStuff = {'lunch':'pizza','bfast':'eggs'}
# myStuff['lunch'] = 'burger'
# myStuff['dinner'] = 'pasta'
# print(myStuff['lunch'])
# print(myStuff)

# t = (1,2,3)
# print(t[0])

# myList = ['a', True, 123]
# myList[0] = 'new'
# print(myList)

# x = set()

# x.add(1)
# x.add(2)
# x.add(0.5)

# print(x)

# Exercise

# s = 'django'

# newString = s[:1]
# print(newString)
# newString = s[-1]
# print(newString)
# newString = s[:4]
# print(newString)
# newString = s[1:4]
# print(newString)
# newString = s[4:]
# print(newString)
# newString = s[::-1]
# print(newString)

# if 1>2:
#   print('yes!')
# elif (3==3) or (3>1):
#   print("YES!")
# else:
#     print('no!')

# seq = [1,2,3,4,5,6]

# for item in seq:
#   print(item)

# d = {"Sam":1,"Frank":2,"Dan":3}

# for item in d:
#   print(d[item])

# mypairs = [(1,2),(3,4),(5,6)]

# for tup1,tup2 in mypairs:
#   print(tup2)

i = 1

while 5 <= i:
  print("i is: {}".format(i))
  i = i + 1