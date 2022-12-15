from orderbook import Orderbook

class Orderbookprogram: #creating Orderbookprogram class

    def __init__(self):
        self.program = Orderbook() 
        self.run()

    def guide(self): #guide method prints guide
        print("commands:")
        print("0 ends")
        print("1 add order")
        print("2 list completed orders")
        print("3 list incompleted orders")
        print("4 set order completed")
        print("5 programmers")
        print("6 programmer status")


    def run(self): #run method runs the program
        print()
        self.guide() #prints guide

        while True: #while loop to keep program running
            print()

            try: #try except to catch errors
                command = int(input("command: ")) #asks for command
                print()
                if command == 0: #breaks
                    print('Thank you for using the program!') #prints thank you for using the program when program is ended
                    print()
                    break
                if command == 1:
                    self.add_order()
                if command == 2:
                    self.print_completed()
                if command == 3:
                    self.print_incompleted()
                if command == 4:
                    self.mark_completed()
                if command == 5:
                    self.programmers()
                if command == 6:
                    self.programmer_status()
                if command != 0 and command != 1 and command != 2 and command != 3 and command != 4 and command != 5 and command != 6:
                    self.guide() #prints guide if command is not 0, 1, 2, 3, 4, 5 or 6
            except:
                print('Incorrect input') #prints incorrect input if command is not int
            


    def add_order(self):
        description = input("description: ") #asks for description
        programmer_and_hours = input("programmer and work amount (for example 'miu 50'): ") #asks for programmer and work amount

        *name, work_amount = programmer_and_hours.split(" ") #splits programmer and work amount to list

        if work_amount.isnumeric(): #if work amount is numeric
            programmer = " ".join(name) #joins name list to string
            work_amount = int(work_amount) #converts work amount to int
            self.program.add_order(description, programmer, work_amount) #adds order to Orderbook
            print("Order added")
        else:
            print("Incorrect input") #if work amount is not numeric prints incorrect input


    def print_completed(self): #prints completed orders
        completed_found = False

        for order in self.program.completed_orders(): #loop through completed orders
            completed_found = True
            print(order)

        if not completed_found: #if completed not found
            print("No completed orders")
        

    def print_incompleted(self):
        incompleted_found = False

        for order in self.program.incompleted_orders(): #loop through incompleted orders
            incompleted_found = True
            print(order)

        if not incompleted_found: #if incompleted orders not found
            print("All orders completed")
      

    def mark_completed(self): #marks order completed
        try: #try to mark order completed
            task_identifier = int(input("task_identifier: "))
            if 0 < task_identifier < (task_identifier+1): #if task_identifier is bigger than 0 and smaller than task_identifier + 1
                self.program.set_completed(task_identifier)
            else:
                print("Incorrect input") 
        except ValueError: #if task_identifier is not int
            print("Incorrect input")
        

    def programmers(self): #prints programmers
        programmers = self.program.programmers()
        if programmers is not None:
            for programmer in programmers:
                print(programmer)


    def programmer_status(self): #prints programmer status
        programmer = input("programmer: ")
        status = self.program.programmer_status(programmer)
        
        if status is not None:
            print(f"Orders: completed {status[0]} not completed {status[1]}, hours: done {status[2]} not done {status[3]}")
            
        else:
            print("Incorrect input")




