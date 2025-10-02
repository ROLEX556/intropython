from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

opperand_1=int(input('enter your opperand1:'))
opperand_2=int(input('enter your opperand_2'))
opperator=input('enter the opperator(+,-,*,/): ')
#if(test expr):
#statement
#elif(text expr)
#statement
#...
#else:
#statement
#statement

if opperator=='+':
    print(opperand_1 + opperand_2)
elif opperator=='-':
    print(opperand_1 - opperand_2)
elif opperator=='*':
    print(opperand_1 * opperand_2)
elif opperator=='/':
    print(opperand_1 / opperand_2)
else:
    print('none')

print('Thank You!'*3)