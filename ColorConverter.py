## Color Converter - HSSP World, 2021 [Friday, March 26]
"""
Thus program was created to solve the problem of
having to browse the internet to convert color,
we hope everyone loves this program :)
"""


HexDict = {"0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
while True:
    Hex = str(input("Enter color in hex: "))
    Hex = Hex.upper()
    ##FFFFFF
    #0123456
    if Hex[0] == "#":
        R, G, B = Hex[1:3], Hex[3:5], Hex[5:7]
    ##    print("rgb({}, {}, {})".format(R, G, B))
        r1, r2 = HexDict[R[0]], HexDict[R[-1]]
        RR = r1*(16**1)+(r2*(16**0))
    ##    print(RR)
        RRKV = RR/255
        g1, g2 = HexDict[G[0]], HexDict[G[-1]]
        GG = g1*(16**1)+(g2*(16**0))
    ##    print(GG)
        GGKV = GG/255
        b1, b2 = HexDict[B[0]], HexDict[B[-1]]
        BB = b1*(16**1)+(b2*(16**0))
    ##    print(BB)
        BBKV = BB/255
        print("Color in rgb format: rgb({}, {}, {})".format(RR, GG, BB))
        print("Color in Kivy rgb format: rgb({}, {}, {})".format(RRKV, GGKV, BBKV))
        

        
    else:
        #FFFFFF
        #012345
        R, G, B = Hex[:2], Hex[2:4], Hex[4:6]
    ##    print("rgb({}, {}, {})".format(R, G, B))
        r1, r2 = HexDict[R[0]], HexDict[R[-1]]
        RR = (r1*(16**1))+r2*(16**0)
    ##    print(RR)
        RRKV = RR/255
        g1, g2 = HexDict[G[0]], HexDict[G[-1]]
        GG = (g1*(16**1))+g2(16**0)
    ##    print(GG)
        GGKV = GG/255
        b1, b2 = HexDict[B[0]], HexDict[B[-1]]
        BB = (b1*(16**1))+b2*(16**0)
    ##    print(BB)
        BBKV = BB/255
        print("Color in rgb format: rgb({}, {}, {})".format(RR, GG, BB))
        print("Color in Kivy rgb format: rgb({}, {}, {})".format(RRKV, GGKV, BBKV))












##Color Converter by HSSP World





    
