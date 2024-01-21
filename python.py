file = open('sample.txt')
text = file.read()
file.close()

print(text)

with open('sample.txt', 'r') as f:
    text = f.read()
print(text)