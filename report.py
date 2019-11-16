class Data(object):
    def __init__(self, types, title, id = None):
        self.id = id
        self.types = types
        self.title = title
        self.assigned_to = None
        self.priority = None
        self.status = None
        self.description = None

class Bug(object):
    def __init__(self, connection):
        self._connection = connection
    
    def add(self):
        pass

    def list_bugs(self):
        cursor = self._connection.cursor()
        query = "SELECT id, bug_type, title, assigned_to, priority, bug_status, description FROM bugtracker ORDER BY id"
        cursor.execute(query)
        for (id, types, title, assigned_to, priority, status, description) in cursor:
            bug = Data(types, title, id)
            bug.assigned_to = assigned_to
            bug.priority = priority
            bug.status = status
            bug.description = description
            yield bug
        cursor.close()
    
    def update(self):
        pass

    def delete(self):
        pass