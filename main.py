print('Lists')
my_list = []
print(my_list)
my_list = [1,2,3,'example',3.14]
print(my_list)

print('Sets')
my_set = {1,2,3,4}
my_set2 = {3,4,5,6}

print(my_set.union(my_set2), '-----OR-----', my_set | my_set2)
print(my_set.intersection(my_set), '-----OR-----', my_set & my_set2)
print(my_set.difference(my_set2), '-----OR-----', my_set - my_set2)
print(my_set.symmetric_difference(my_set2), '-----OR-----', my_set ^ my_set2)
my_set.clear()
print(my_set)

print('while and loop')
num = 1
odd_nums = []
while num:
    if num % 2 != 0:
        odd_nums.append(num)
    if num >= 20:
        break
    num += 1
print('odd numbers: ', odd_nums)

print('for loop')
list= [1,2,3,4,5]
for num in list:
    print(num)
    
def pow(a):
    return a**2
print(pow(3))

def pow(a):
    print(a**2)
pow(4)

print('function recursive')
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

num = 3
print('Nilai faktorial dari',num, 'adalah ', factorial(num))