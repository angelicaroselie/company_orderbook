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

