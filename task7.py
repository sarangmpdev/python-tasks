with open('sample.txt', 'a') as writefile:
    line1=writefile.write('Line 1: This is a sample text file.\n')
    line2=writefile.write('Line 2: It contains multiple lines.\n')

try:
    with open('sample.txt', 'r') as readfile:
        print('Reading file content:\n')

        print(readfile.read())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


