def list(list):
    list=[]
    print('Type \'q\' to finish adding the numbers.')
    while True:
        num = input('Please input some numbers: ')
        if num == 'q':
            break
        else:
            list.append(num)
    return(list)


def find_max(list):
    if not list:
        print('There\'s no number in the list')
    else:
        max_num = int(list[0])
        for num in list:
            if int(num) > int(max_num):
                max_num = num
        return max_num


def main():
    user_list = list(list)
    max = find_max(user_list)
    print('The maximum number in the list: ', max)


main()