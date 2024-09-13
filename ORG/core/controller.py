class BaseController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def execute(self):
        raise NotImplementedError("Execute method not implemented.")