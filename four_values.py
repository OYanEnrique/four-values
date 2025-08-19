#Four Values

n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))
n4 = int(input('Enter a number: '))

user_values = (n1, n2, n3, n4)
if 9 in user_values:
	print(f'The number 9 was entered {user_values.count(9)} times')

if 3 in user_values:
	
	print(f'The number 3 was found in the {user_values.index(3)+1}° position')
else:
	print(f'The value 3 was not entered in any position')

for number in user_values:
	
	if number%2 == 0:
		print(f'Even number found: {number}')