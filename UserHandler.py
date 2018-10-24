import json
from DbConfig import Database
from tornado.web import RequestHandler


class UserItem(RequestHandler):
    def get(self):
        db = Database.connect()
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * from user')
            data = cursor.fetchall()
            result = []

            for row in data:
                result.append({'id': row[0], 'nick': row[1], 'nameSurname': row[2], 'email': row[3]})

            self.write(json.dumps(result))
            db.close()
        except Exception as e:
            print "An error occured while reading data." + str(e)

    def post(self):
        db = Database.connect()
        cursor = db.cursor()
        try:
            nick = self.get_argument("nick")
            nameSurname = self.get_argument("nameSurname")
            email = self.get_argument("email")
            cursor.execute("INSERT INTO user (nick,nameSurname,email) VALUES ('{}', '{}', '{}')"
                           .format(nick, nameSurname, email))
            db.commit()
            db.close()
        except Exception as e:
            db.rollback()
            print "An error occured while inserting data." + str(e)

    def put(self, id):
        db = Database.connect()
        cursor = db.cursor()
        try:
            data = json.loads(self.request.body)
            nick = data["nick"]
            nameSurname = data["nameSurname"]
            email = data["email"]
            cursor.execute("UPDATE user SET nick='{}',nameSurname='{}',email='{}' WHERE id='{}'"
                           .format(nick, nameSurname, email, id))
            db.commit()
            db.close()
        except Exception as e:
            db.rollback()
            print "An error occured while updating data." + str(e)

    def delete(self, id):
        try:
            db = Database.connect()
            cursor = db.cursor()
            cursor.execute("DELETE FROM user WHERE id='{}'".format(id))
            db.commit()
            db.close()
        except Exception as e:
            print "An error occured while deleting data." + str(e)

    def data_received(self, chunk):
        pass
