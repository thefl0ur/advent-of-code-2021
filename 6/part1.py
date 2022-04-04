
def read_data(file_name):
    with open(file_name, 'r') as file:
            return list(map(int, file.readline().split(',')))

data = [0 for age in range(9)]

for init_data in read_data('data/input.in'):
    data[init_data] += 1

days = 256

print('initinal')
print(f"{data[0]} {data[1]} {data[2]} {data[3]} {data[4]} {data[5]} {data[6]} {data[7]} {data[8]}")
print('--------')

for day in range(days):
    newborn = 0
    aged = 0
    for index in range(len(data)):
        if index == 0:
            newborn = data[index]
            aged += data[index] 
        else:
            data[index-1] = data[index]
        data[index] = 0
    
    data[6] += aged
    data[8] = newborn

    # print(f"{data[0]} {data[1]} {data[2]} {data[3]} {data[4]} {data[5]} {data[6]} {data[7]} {data[8]}")

print(sum(data))
