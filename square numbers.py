numbers= [1,2,3,4,5,6]
def square(x):
    return x**2

squared_num= [square(i) for i in numbers]

# squared_num=list(map(square,numbers))
print(squared_num)

