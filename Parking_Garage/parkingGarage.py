# print(currentTicket)
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary
class Garage():
    '''
        - tickets -> list
        - parkingSpaces -> list
        - currentTicket -> dictionary
    '''
    def __init__(self,tickets,parkingSpaces,currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket   
        
    def takeTicket(self):
        self.currentTicket[self.tickets[0]] = ''
        del self.tickets[0]
        del self.parkingSpaces[0]
        print(self.parkingSpaces)
        print(self.tickets)
        print(self.currentTicket)
    
# Angelica -- payForParking lines 25 -29 (collaboration for remaining lines)
    def payForParking(self):
        paid = int(input("What's your ticket number? "))
        self.currentTicket[paid] = 'paid'
        print ("Your ticket has been paid and you have 15 min to leave the garage")
        print (self.currentTicket)
        
  # Monica -- def leaveGarage lines: 39-47 (collaboration for remaining lines)
    def leaveGarage(self):
        answer = int(input("What's your ticket number? "))
        if self.currentTicket[answer] != 'paid':
            print ("Pay Ticket")
        elif self.currentTicket[answer] == 'paid':
            print ("Thank you, come again")
        self.tickets.append(answer)
        self.parkingSpaces.append(answer)
        del self.currentTicket[answer]

# Denise -- parkingGarage lines: 49-62 (collaboration for remaining lines)           
parkingGarage = Garage([1,2,3,4,5],[1,2,3,4,5],{})      
def run():

    while True:
        response = input('What would you like to do? Park / Pay / or Leave? ')
        
        if response.lower() == 'park':            
            parkingGarage.takeTicket()
           
        if response.lower() == "pay":
            parkingGarage.payForParking()
        
        if response.lower() == 'leave':
            parkingGarage.leaveGarage()

run()