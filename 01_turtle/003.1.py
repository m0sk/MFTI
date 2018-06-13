#!C:\UDISK\ProgramFiles\python\3.6.2\python.exe

'''
    by coordinate (x,y), define in which quarter point is
          
          ^y
      II  |  I
          |
      ----+---->
          |0   x
     III  |  IV

    x>0, y>0 = I
    x<0, y>0 = II
    x<0, y<0 = III
    x>0, y<0 = IV   
'''

x = int(input())
y = int(input())

if x>0 and y>0:
    print('I - First quarter')
elif x>0 and y<0:
    print('IV - Fourth quarter')
elif y>0:
    print('II - Second quarter')
else:
    print('III - Third quarter')

input()