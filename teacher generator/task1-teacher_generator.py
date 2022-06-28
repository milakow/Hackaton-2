name = input('Enter name and surname separated with a comma: ')
missing_task = int(input('Enter a number of missing tasks: '))
grade = float(input('Enter student\'s grade:'))

with open('message') as fopen:
    text = fopen.readlines()
    print(text)
