h=float(input('Enter hours:'))
r=float(input('Enter rate:'))

if h<=40:
    g=r*h
else:
    g=(40*r)+((h-40)*r*1.5)

print (g)
