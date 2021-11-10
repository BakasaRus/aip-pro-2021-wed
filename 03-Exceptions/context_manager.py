with open('text.txt', 'w') as file:
    file.write('Hello World!')

file = open('text.txt', 'w')
try:
    file.write('Hello World!')
finally:
    file.close()
