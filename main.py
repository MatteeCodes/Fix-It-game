def welcome():
    print ("Welcome to the Fix IT Game")
def one():
    print ("1.")
    print ("Fix this code")
    print (" Code:printf("") ")
    print ("1.echo")
    print ("2.say()")
    print ("3.print("")")
    one = input ("Put Number Here:")
    if one == "3":
        print ("Correct")
        input("")
        two()
    else:
        print ("Wrong")
        input("")
        two()
def two():
    print ("1.")
    print ("Fix this code")
    print (" Code:input==input("") ")
    print ("1.input = input ("")")
    print ("2.input======--input()")
    print ("3.input -- raw_input()")
    two = input ("Put Number Here:")
    if two == "1":
        print ("Correct")
        input("")
    else:
        print ("Wrong")
        input("")
welcome()
one()
