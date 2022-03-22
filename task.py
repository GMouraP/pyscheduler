

class Task():
    def __init__(self, name, target=None, args=(), kwargs={}, daemon=None):
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.daemon = daemon

    def run(self):
        try:
            return self.target(*self.args, **self.kwargs)
        except Exception as error_msg:
            return error_msg
