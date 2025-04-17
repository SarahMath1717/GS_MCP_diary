class TodoManager:
    class Todo:
        def __init__(self, task):
            self.task = task
            self.complete = False

        def mark_complete(self):
            self.complete = True

        def __repr__(self):
            return f"<Todo task='{self.task}' complete={self.complete}>"

    def __init__(self):
        self.list = []

    def add(self, task):
        self.list.append(self.Todo(task))

    def incomplete(self):
        return [todo for todo in self.list if not todo.complete]

    def complete(self):
        return [todo for todo in self.list if todo.complete]

    def give_up(self):
        for todo in self.list:
            todo.mark_complete()