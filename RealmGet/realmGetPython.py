file = open('InputText.txt', 'a')
file.write("helloWorld")
file.close()

f = open('InputText.txt', 'r')
print(f.read())
f.close()