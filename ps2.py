def inp():
    global x, y
    x = int(input("Enter position : "))  # taking position from user
    if (x > 9 or x < 1):
        print("Invalid position")
        exit()
    y = int(input("Enter number : "))  # taking number from user
    if (y > 9 or y < 1):
        print("Invalid number")
        exit()
    return x, y



def disp():
    print(a,b,c)
    print()
    print(d,e,f)
    print()
    print(g,h,i)


# def assgn():
#     global a, b, c, g, f, e, d, i, h
#     if (x == 1):
#         a = y
#     if (x == 2):
#         b = y
#     if (x == 3):
#         c = y
#     if (x == 4):
#         d = y
#     if (x == 5):
#         e = y
#     if (x == 6):
#         f = y
#     if (x == 7):
#         g = y
#     if (x == 8):
#         h = y
#     if (x == 9):
#         i = y
#     return a, b, c, d, e, f, g, h, i
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
print("Welcome to the game")
print("Player 1")  # First input
x, y = inp()
if x == 1:
    a = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 1 won")
    exit()

print("Player 2")  # Second input
x, y = inp()
if x == 1:
    a = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 2 won")
    exit()

print("Player 1")  # Third input
x, y = inp()
if x == 1:
    a = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 1 won")
    exit()

print("Player 2")  # fourth input
x, y = inp()
if x == 1:
    a = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 2 won")
    exit()

print("Player 1")  # fifth input
x, y = inp()
if x == 1:
    a = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 1 won")
    exit()

print("Player 2")  # sixth input
x, y = inp()
if x == 1:
    a = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 2 won")
    exit()

print("Player 1")  # seventh input
x, y = inp()
if x == 1:
    a = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 1 won")
    exit()

print("Player 2")  # Eighth input
x, y = inp()
if x == 1:
    a = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y==1 or y==3 or y==5 or y==7 or y==9):
        print("Invalid input,only even numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 2 won")
    exit()

print("Player 1")  # ninth input
x, y = inp()
if x == 1:
    a = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        a = y
if x == 2:
    b = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        b = y
if x == 3:
    c = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        c = y
if x == 4:
    d = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        d = y
if x == 5:
    e = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        e = y
if x == 6:
    f = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        f = y
if x == 7:
    g = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        g = y
if x == 8:
    h = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        h = y
if x == 9:
    i = y
    if (y == 2 or y == 4 or y == 6 or y == 8):
        print("Invalid input,only odd numbers for player 1")
        y = int(input("Re-enter number : "))
        i = y
disp()
if (((a + b + c) == 15) or ((d + e + f) == 15) or ((g + h + i) == 15) or ((a + d + g) == 15) or ((b + e + h) == 15) or (
        (c + f + i) == 15) or ((a + e + i) == 15) or ((g + e + c) == 15)):
    print("Player 1 won")
    exit()

if (((a + b + c) != 15) or ((d + e + f) != 15) or ((g + h + i) != 15) or ((a + d + g) != 15) or ((b + e + h) != 15) or (
        (c + f + i) != 15) or ((a + e + i) != 15) or ((g + e + c) != 15)):
    print("Match draw")
print("1. continue next game   2.exit")
q=input("Enter choice")
if q==1:
    exit()
