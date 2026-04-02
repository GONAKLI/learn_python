# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

class Train:
    seats = 100
    def bookTicket(self):
        Train.seats -=1
        print('Ticket Booked')
    @staticmethod
    def getStatus():
        print('available Seats are : ', Train.seats)
    def fare(self):
        print('price per ticket is 50 Rs')


pass1 = Train()
pass1.getStatus()
pass1.bookTicket()
pass1.getStatus()


pass2 = Train()
pass2.bookTicket()
pass2.getStatus()