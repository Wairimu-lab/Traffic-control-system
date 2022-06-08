#Traffic control system

#ask user for input
X5 = int(input("Enter a value below 400: "))
if  X5 <= 400:
    X1 = 600
    X2 = 200
    X3 = 400
    X4 = 500 - X5

else:
    print("Your input is invalid! Enter number below 400: ")
#print out the values of X

print('X1 = ' , X1)
print('X2 = ' , X2)
print('X3 = ' , X3)
print('X4 = ' , X4)
print('X5 = ' , X5)





#for time
print("Seconds allocated at each street at a junction.")

print("For every 50 cars 20 second will be allowed")
#to calculate the seconsd allocated for each street at a specific junction

def junctionA():
    street_1 = (500/50) * 20
    street_4 = (300/50) * 20
    (print("at A"))
    print("street 1:" ,street_1, "seconds")
    print("street 4:" ,street_4, "seconds")

def junctionB(X2,X4):
    street_1 = (X2/50) * 20
    street_2  = (X4/50) * 20
    print("at B")
    print('street1:' ,street_1, "seconds")
    print("street2:" ,street_2, "seconds")

def junctionC():
    street_2 = (400/50) * 20
    street_3 = (100/50) *20
    print("at C")
    print("street2: " ,street_2, " seconds")
    print("street3: " ,street_3, " seconds")

def junctionD(X1,X5):

        street_3 = (X5 / 50) *20
        street_4 = (X1 / 50) * 20
        print("at D")
        print("street3: ",street_3, " seconds")
        print("street4: ", street_4, " seconds")
#to call the functions
junctionA()
junctionB(X2 , X4)
junctionC()
junctionD(X1 , X5)



