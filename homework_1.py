def search (x,y,z):
    if x == 0 or y ==0 or z ==0 or x+y+z != 180:
        print('삼각형이 아닙니다.')
    

x=int(input('제1각을 입력하세요'))
y=int(input('제2각을 입력하세요'))
z=int(input('제3각을 입력하세요'))

print(search(x,y,z))
