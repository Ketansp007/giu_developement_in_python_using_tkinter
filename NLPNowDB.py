import json

class Database:

    def add_data(self,name,email,pass1):

        with open('db.json','r') as rf:
            db = json.load(rf)
        if email in db:
            return 0
        else:
            db[email] = [name,pass1]
            with open('db.json','w') as wf:
                json.dump(db,wf)
            return 1

    def search(self,email,pass1):
        with open('db.json','r') as rf:
            db = json.load(rf)
        if email in db:
            if db[email][1] == pass1:
                return 1
            else:
                return 0
        return -1


