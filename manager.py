class Manager:
    def __init__(self, currentstate):
        self.currentstate = currentstate

    def get_state(self):
        return self.currentstate

    def set_state(self, state):
        self.currentstate = state
