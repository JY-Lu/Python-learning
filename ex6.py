types_of_people = 10 #变量types_of_people的value为10
x = f"There are {types_of_people} types of people." #将变量x的值设为一个str, 这个str中还包含了另外一个变量的值

binary = "binary" #将变量的值设为str
do_not = "don't" #讲变量的值设为str
y = f"Those who know {binary} and those who {do_not}." #将变量y的值设为一个str, 这个str中还包含了两个另外的变量的值

print(x) #输出x
print(y) #输出y

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
