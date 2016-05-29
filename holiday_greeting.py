print("Welcome to the holiday greeting generator!")

recipient = raw_input("Who would you like to send this to? ")
sender = raw_input("Who is this greeting from? ")
holiday = raw_input("What is the holiday? ")

greeting = "Happy " + holiday + ", " + recipient + "! - From " + sender

print(greeting)