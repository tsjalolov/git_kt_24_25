mas1 = ['xona1','xona2','xona3','xona4']
def salom():
    return('salom men ishladim !!!!!')
def xonalar2(y):
   try:

       print(f'siz {mas1[y - 1]} ni tanladingiz')
       w = salom()
       print(w)
   except:
       print('bunday xona yo`q')
while True:
    print('1 -->xonalar')
    print('2 -->Gost')
    print('3 -->Gost Add')
    x = int(input('tanlang -->'))
    xonalar2(x)