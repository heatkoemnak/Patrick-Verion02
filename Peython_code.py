while True:



  #reciving the data from user
    P=float(input("Enter Amount: "))#Amount's investment
    i=float(input("Enter Interest rate: ")) #interest rate
    n=int(input("Enter Year: "))#each years

  
    print("\n{:<10} {:<15} {:<20} {:<27}".format("years","Interest rate", "Principale","Return's Amount "))
    print("_"*70)#print line
    

    for x in range(n):

        years = x+1 
        x += 1
        P = 250000
        Final_value=P
        end_of_the_year = Final_value*(1+(i/100))**x
        print("{:2}".format(years),
          "{:14.2f}".format(i),
          "{:18.2f}".format(P),
          "{:20.2f}".format(end_of_the_year))
        print("_"*70)
    check = input("Do you want to quit or start gain, enter Y to restart or another to end ?:")
    if check.upper() == "Y": #loop back to the start


        continue
    print("Bye..!Have a nice day")

    break #exit the program