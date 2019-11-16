class Data(object):
    def __init__(self, types, title, id = None):
        self.id = id
        self.type = types
        self.title = title
        self.assigned_to = None
        self.priority = None
        self.status = None
        self.description = None

class Bug(object):
    def __init__(self):
        pass
    
    def add(self):
        pass

    def list_bugs(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass