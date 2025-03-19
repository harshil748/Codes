class Employee:
    def __init__(self, employee_id, name, status):
        self.employee_id = employee_id
        self.name = name
        self.status = status

    def __str__(self):
        return f"{self.employee_id} {self.name} {self.status}"
