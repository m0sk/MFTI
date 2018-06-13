#!C:\UDISK\ProgramFiles\python\3.6.2\python.exe

'''
    by coordinate (x,y), define in which quarter point is
          
          ^y
      II  |  I
          |
      ----+---->
          |0   x
     III  |  IV
'''


x = int(input())   # intput() - enter from input (keyboard)
y = int(input())

'''
    x>0, y>0 = I
    x<0, y<0 = II
    x<0, y<0 = III
    x>0, y<0 = IV
'''

if x>0:
    if y>0:
        print('I (First quarter)')
    else:
        print('IV (Fourth quarter)')
else:
    if y>0:
        print('II (Second quarter)')
    else:
        print('III (Third quarter)')


input()