class User:
    def name(self, name, password):
        self.password = password
        self.name = name
        sql = f"insert into bankaccount({'self.name'},{'self.password'})"
