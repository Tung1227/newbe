
# for item in 'string':
#    # print(item)
#     pass
# fruits = ["apple","orange","mangoes"]
# for fruit in fruits:
#     #print(fruit)
#     string_size = 0
#     for alphabet in fruit:
#         string_size += 1
#     print("nam of fruit: %s is has lenth %s" % (fruit, string_size))
#     pass
# for index, fruit in enumerate(fruits):
#     print("index is %s" % index)
#     print("fruit is %s" % fruit)
 # while blocks

# fruits = ["apples","oranges","mangoes"]
# length = len(fruits)
# i = 0
# while i < length:
#     print(fruits[i])
#     i+=1

for i in range(1,3):
        for j in range(1,3):
                print("%d x %d = %d" % (i,j,i*j))
num = 43
if num == 42:
    print("number is 42")
else:
    print("number is not 42")