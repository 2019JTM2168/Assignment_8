#taking input from user
x=input("Enter binary data : ")
n=len(x)    #string length
count=0
for i in range(0,n):
    if x[i] in '0':
        print()
    elif x[i] in '1':
        count +=1       #counting ones
    else:
        print("Invalid data")
        exit()
p=count%2   #finding parity
# print(count)
if p == 0:
    print("Even parity")
    print("Data with parity bit : {0}".format(x+"1"))       #printing even parity data to be transmitted
if p==1:
    print("Odd parity")
    print("Data with parity bit : {0}".format(x + "0"))     #printing odd parity data to be transmitted
#replacing 010 with 0100
y=x.replace("010","0100")
print("Modified string to be transmitted : {0}".format(y+"0101"))

## Testing



