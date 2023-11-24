# CIS 40 - Lab assignment 5

# Name: Jesse Yang

# Usage:
# This program is used to set a time and print the time appropriately in hh:mm:ss format.
# This program is based on a class called Clock, It has 3 initiate variables: hours, minutes, and seconds.
# This program also has a print function for printing the time in the correct format.
# ----------------------
class Clock:
    '''def 3 init arguments: hours, minutes, and seconds. All default setting are 0'''
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    '''def a print function, print the instanced variable'''    
    def print_time (self):
        '''if minutes and seconds are less than 10, print a "0" in the front to make it look better.'''
        if self.minutes < 10 and self.seconds < 10:
            print(f'{self.hours}:0{self.minutes}:0{self.seconds}')
        elif self.minutes < 10:
            print(f'{self.hours}:0{self.minutes}:{self.seconds}')
        elif self.seconds < 10:
            print(f'{self.hours}:{self.minutes}:0{self.seconds}')
        else:
            print(f'{self.hours}:{self.minutes}:{self.seconds}')
            
'''Print the default time setting.'''
default_time = Clock()
print("The default time is: ", end="")
default_time.print_time()

'''Requirement(1): Write a instance method that changes the current time of the Clock and prints'''
time = Clock(8, 20, 59)    
print(f'{time.hours}:{time.minutes}:{time.seconds}')

'''Requirement(2): Write a instance method that changes the current time, prints
out the new time with a quick message explaining that it's a new time. '''
hours = 4
minutes = 30
seconds = 30
new_time = Clock(hours, minutes, seconds)
print("The new time is: ", end="")
new_time.print_time()

'''Requirement(3): Getting user input for new time, raise ValueError if input is not appropriate.'''
valid = False
while valid == False:
    try:
        hours = int(input("Enter the new time hours: "))
        if not 0 <= hours <= 23:
            raise ValueError()
        minutes = int(input("Enter the new time minutes: "))
        if not 0 <= minutes <= 59:
            raise ValueError()
        seconds = int(input("Enter the new time seconds: "))
        if not 0 <= seconds <= 59:
            raise ValueError()
        valid  = True
    except ValueError:
        print("Please enter appropriate input.")

'''Print out the newly updated new_time after getting the user's inputs. '''        
new_time  = Clock(hours, minutes, seconds)
print("The new time is: ", end="")
new_time.print_time()
