
class Executor():
    def __init__(self, executeQueue, workers=None):
        self.executeQueue = executeQueue

        self.results = {}
        self.pooling = False

    def stop_pool(self):
        self.pooling = False

    def start_pool(self):
        self.pooling = True
        self.__pooling__()

    def __pooling__(self):
        while self.pooling:
            task = self.executeQueue.get()
            self.results[task.name] = task.run()

    def get_results(self, task_name):
        return self.results[task_name]
