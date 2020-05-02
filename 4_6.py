def computepay(h,r):
    if h<=40:
        g=h*r
        return g
    else:
        g=(40*r)+((h-40)*1.5*r)
        return g

h=float(input('Enter Hours:'))
r=float(input('Enter Rate:'))

p=computepay(h,r)

print("Pay",p)
