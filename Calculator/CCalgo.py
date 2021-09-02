from math import cos
from math import sin
from math import tan
numsign = ["*", "/", "-", "+"]

def solve(inp):
    inp = list(inp)
    print(inp)

    print(dir(eval))





    
##    try:
##    for u in inp:
##        if (u == ")") and\
##           (not any(n in numsign for n in inp[inp.index(")"):])) and (not inp[-1] == u) and inp[inp.index(u)+1] != "":
##            print(") is there!")
##            inp.insert(inp.index(")")+1, "*")
##            print(''.join(inp))
    res = eval(''.join(inp))
    print(res)






##    except:
##        print("Error!")
##    
##    


while True:
    inp = input(">>> :")
    solve(inp)
