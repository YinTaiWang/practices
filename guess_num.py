import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count += 1
    g = input ('請猜一個數字: ')
    g = int(g)
    if g == r:
        print('你猜中了!')
        print('你總共試了', count , '次')
        break
    elif g < r:
        print('比答案大')
    elif g > r:
        print('比答案小')
    else:
        print('只能輸入0~100的數字')
    print('這是你猜的第', count , '次')