myFile = open('myFile.txt','r+')
print('Your Current file contents:')
for lines in myFile:
	print(lines)
inputText = input('what do you want to save ')
myFile.write(inputText);
myFile.close();
print('Things saved: See below for updated contents:')

myFile = open('myFile.txt','r')
for lines in myFile:
	print(lines)

myFile.close()

