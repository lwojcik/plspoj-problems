from math import fabs, sqrt

x = raw_input().split()
x0 = int(x[0])
y0 = int(x[1])
r = int(x[2])

n = int(raw_input())

for j in range(0, n):
            q = raw_input().split()
            xi = int(q[0])
            yi = int(q[1])

            ox = fabs(xi-x0)
            oy = fabs(yi-y0)
            odl = sqrt((ox**2)+(oy**2))

            if odl == r:
                print "E"
            elif odl > r:
                print "O"
            elif odl < r:
                print "I"
