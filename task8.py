with open('output.txt','w') as write_file:
    userinput = write_file.write(input("Enter text to write to the file:") + '\n')
    print('Data successfully written to output.txt\n')

with open('output.txt','a') as appender:
    user_append=appender.write(input("Enter additional text to append:") + '\n')
    print('Data successfully appended.\n')



try:
    with open('output.txt','r') as readfile:
        print('Final content of output.txt:')

        for line in readfile:
            print(line.strip())

except FileNotFoundError:
    print('File not found')
