s=input('Enter Score:')
try:
    s=float(s)
    if s<0.0 or s>1.0:
        print('error')
    elif s>=0.9:
        print('A')
    elif s>=0.8:
        print('B')
    elif s>=0.7:
        print('C')
    elif s>=0.6:
        print('D')
    elif s<0.6:
        print('F')

except:
    print('not a number')
