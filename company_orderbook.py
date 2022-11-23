class Task: #creating Task class

    _id = 1 #setting protected start id value, can't be changed from outside
    def __init__(self, description: str, programmer: str, work_amount_prediction: int):
        self.description = description
        self.work_amount = work_amount_prediction
        self.programmer = programmer
        self.is_ready = "NOT COMPLETED" 
        self.id = Task._id
        Task._id += 1 #always adding +1 to id when creating new task so that id's are unique
    
    def __str__(self): #creating string method
        return f"{self.id} {self.description} ({self.work_amount} hours), programmer {self.programmer} {self.is_ready}"

    def set_completed(self): #setter 
        self.is_ready = 'COMPLETED'

    def is_task_completed(self):
        if self.is_ready == "NOT COMPLETED": #if not completed return false
            return False
    
        return True #if completed return true



class Orderbook: #creating Orderbook class
    
    def __init__(self):
        self.orders_list = [] #creating orders list

    def add_order(self, description, programmer, work_amount):
        self.orders_list.append(Task(description, programmer, work_amount)) #adding Task objects to Orderbooks orders_list

    def get_all_orders(self):
        return self.orders_list #return orders_list

    def programmers(self):
        programmer_found = False
        programmers_list = []

        for order in self.orders_list: #loop through orders_list
            programmer_found = True
            programmers_list.append(order.programmer) #append programmers to programmers_list

        programmers_list = list(set(programmers_list)) #remove duplicates from programmers_list

        if not programmer_found: #if programmer not found print programmer not found
            print('Programmers not found')
        else: #return programmers_list
            return programmers_list


    def set_completed(self, id: int): #sets order to completed

        order_found = False #setting order_found to false

        for order in self.orders_list: #loop through orders_list
            if order.id == id: #if order id is same as id
                order.set_completed() #set order to completed
                order_found = True #set order_found to true
                print('Order completed') #print order completed
        
        if order_found == False: #if order not found
            raise ValueError("Order not found") #raises value error if order not found


    def completed_orders(self): #returns completed orders

        completed_list = []

        for order in self.orders_list: #loop through orders_list
            if order.is_task_completed(): #check if order is completed with is_task_completed method
                completed_list.append(order) #append completed orders to completed_list


        return completed_list #returns completed orders list


    def incompleted_orders(self): #returns incompleted orders

        incompleted_list = []

        for order in self.orders_list: #loop through orders_list
            if not order.is_task_completed(): #check if order is not completed with is_task_completed method
                incompleted_list.append(order) #append incompleted orders to incompleted_list


        return incompleted_list #returns incompleted orders list


    #returns tuple that contains completed and incompleted orders and time spent on them
    def programmer_status(self, programmer: str):

        completed_tasks = 0
        completed_hours = 0
        incompleted_tasks = 0
        incompleted_hours = 0
        coder_found = False

        for order in self.orders_list: #loop through orders_list
            if order.programmer == programmer: #if order programmer is same as programmer that is given as parameter
                coder_found = True #set coder_found to true
                if order.is_task_completed(): #if order is completed
                    completed_tasks += 1 #add +1 to completed_tasks
                    completed_hours += order.work_amount #add work_amount to completed_hours
                if not order.is_task_completed(): #if order is not completed
                    incompleted_tasks += 1 #add +1 to incompleted_tasks
                    incompleted_hours += order.work_amount #add work_amount to incompleted_hours
            
        

        if coder_found == False: #if coder not found
            return None #return none

        return (completed_tasks, incompleted_tasks, completed_hours, incompleted_hours) #return tuple with completed_tasks, incompleted_tasks, completed_hours, incompleted_hours
        

class Orderbookprogram: #creating Orderbookprogram class
    def __init__(self):
        self.program = Orderbook() 

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
        programmer_and_hours = input("programmer and work amount: ") #asks for programmer and work amount

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


    
if __name__ == "__main__": #runs program

    program = Orderbookprogram()
    program.run()


