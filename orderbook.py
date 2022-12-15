from task import Task

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
        

