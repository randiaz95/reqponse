class AuthCache:
    def __init__(self, dbname):
        self.dbname = dbname
        authDB = open(dbname, "r+")
        self.auth_server = map(lambda x: x.split("|"), authDB.readlines())
        self.auth = {
            payload[0]: payload[1] for payload in self.auth_server
        }
        authDB.close()
        
    def authenticate(email, password):
        return email in self.auth and password == self.auth[email]
    