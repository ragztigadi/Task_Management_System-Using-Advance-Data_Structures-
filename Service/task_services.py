from Models import task, queue, stack, graph

class Task_Services:

    def __init__(self):
        self.task = []
        self.task_queue = queue()
        self.task_history = stack()