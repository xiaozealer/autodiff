from Variable import *

a = Variable(4, 'a')
b = Variable(3, 'b')
c = a + b
d = a * c
gradient = d.get_gradient()
print(gradient[b])