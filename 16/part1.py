import binascii

def read_data(filename):
    data = None
    with open(filename) as f:
        data = f.readline()

    # https://github.com/moink/advent2021/blob/master/day16/day16.py
    bits = bin(int(data, 16))[2:]
    len_data = len(bits)
    if len_data % 4 > 0:
        bits = "0" * (4 - len_data % 4) + bits
    return bits


data = read_data('data/input.in')

def process_pac(pac, index=0):
    # breakpoint()
    summ = 0
    #get version
    version = int(pac[index:index+3], 2)
    summ+= version
    index += 3

    #get version
    
    _type = int(pac[index:index+3], 2)
    index += 3

    #literal
    if _type == 4:
        # breakpoint()
        _data = ""
        while True:
            tmp = pac[index:index+5]
            _data+=tmp[1:]
            index+=5
            if (tmp[0] == '0'):
                break
            
        # print(f'literal {int(_data, 2)}')
    # operator
    else:
        # breakpoint()
        i = pac[index]
        index += 1

        if i == '0':
            
            sub_pac_len = int(pac[index:index+15],2)
            index += 15
            finish = index + sub_pac_len
            while True:
                # breakpoint()
                summ1, index1 = process_pac(pac, index)
                summ += summ1
                index = index1
                if index >= finish:
                    break
        else:
            #  breakpoint()
             num_of_pac = int(pac[index:index+11],2)
             index += 11
             while num_of_pac > 0:
                summ1, index1 =process_pac(pac, index)
                summ += summ1
                index = index1
                num_of_pac -=1


    return (summ, index)


print(process_pac(data))