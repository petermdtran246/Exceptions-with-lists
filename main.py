names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

try:
    name_index = names[index]
    print(f'Name: {name_index}')
except IndexError:
    # Handle invalid index
    if index > 0 and index >= len(names):
        print(f'Exception! list index out of range')
        print(f'The closest name is: {names[-1]}')
    else:
        print(f'Exception! list index out of range')
        print(f'The closest name is: {names[0]}')


