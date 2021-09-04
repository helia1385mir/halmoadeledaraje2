
d,v,c = int(input("a : ")) , int(input("b : ")) , int(input("c : "))
delta = ((v**2) - 4*d*c)
print("")
print("Δ = {}".format(delta))
if delta >= 0:
    x1 = (-v+(delta**0.5))/(2*d)
    x2 = (-v-(delta**0.5))/(2*d)
    print ("x1 = {}".format(x1))
    print ("x2 = {}".format(x2))
else:
    print("error")
    exit()
 