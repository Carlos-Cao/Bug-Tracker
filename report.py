class Data(object):
    def __init__(self, id, types, title, assigned_to, priority, status, description):
        self.id = id
        self.types = types
        self.title = title
        self.assigned_to = assigned_to
        self.priority = priority
        self.status = status
        self.description = description

class Bug(object):
    def __init__(self, connection):
        self._connection = connection
    
    def add(self, bug):
        cursor = self._connection.cursor()
        query = "INSERT INTO bugtracker(bug_type, title, assigned_to, priority, bug_status, description) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (bug.types, bug.title, bug.assigned_to, bug.priority, bug.status, bug.description))
        cursor.close()
        self._connection.commit()


    def list_bugs(self):
        cursor = self._connection.cursor()
        query = "SELECT id, bug_type, title, assigned_to, priority, bug_status, description FROM bugtracker ORDER BY id"
        cursor.execute(query)
        for (id, types, title, assigned_to, priority, status, description) in cursor:
            bug = Data(id, types, title, assigned_to, priority, status, description)
            bug.id = id
            bug.types = types
            bug.title = title
            bug.assigned_to = assigned_to
            bug.priority = priority
            bug.status = status
            bug.description = description
            yield bug
        cursor.close()
    
    def update(self, bug):
        cursor = self._connection.cursor()
        query = "UPDATE bugtracker SET bug_type = %s, title = %s, assigned_to = %s, priority = %s, bug_status = %s, description = %s WHERE id = %s"
        cursor.execute(query, (bug.types, bug.title, bug.assigned_to, bug.priority, bug.status, bug.description, bug.id))
        cursor.close()
        self._connection.commit()
        

    def delete(self):
        pass