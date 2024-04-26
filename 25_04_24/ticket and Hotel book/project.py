def travelStatus(user,a,b):
      a = int(a)
      b = int(b)
      c = a+b
      print( )
      print("user name: ",user)
      print("Ticket cost ",a)
      print("Hotel cost ",b)
      print("Total cost ",c)

userName = input(" Enter your name: ")
ticketCost = input(" Enter ticket cost ")
hotelCost = input(" Enter hotel cost ")

travelStatus(userName,ticketCost,hotelCost)