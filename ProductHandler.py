import json
from DbConfig import Database
from tornado.web import RequestHandler


class ProductItem(RequestHandler):
    def get(self):
        db = Database.connect()
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * from product')
            data = cursor.fetchall()
            result = []

            for row in data:
                result.append({'id': row[0], 'title': row[1], 'price': row[2], 'quantity': row[3]})

            self.write(json.dumps(result))
            db.close()
        except Exception as e:
            print "An error occured while reading data." + str(e)

    def post(self):
        db = Database.connect()
        cursor = db.cursor()
        try:
            title = self.get_argument("title")
            price = self.get_argument("price")
            quantity = self.get_argument("quantity")
            cursor.execute("INSERT INTO product (title,price,quantity) VALUES ('{}', '{}', '{}')"
                           .format(title, price, quantity))
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
            title = data["title"]
            price = data["price"]
            quantity = data["quantity"]
            cursor.execute("UPDATE product SET title='{}',price='{}',quantity='{}' WHERE id='{}'"
                           .format(title, price, quantity, id))
            db.commit()
            db.close()
        except Exception as e:
            db.rollback()
            print "An error occured while updating data." + str(e)

    def delete(self, id):
        try:
            db = Database.connect()
            cursor = db.cursor()
            cursor.execute("DELETE FROM product WHERE id='{}'".format(id))
            db.commit()
            db.close()
        except Exception as e:
            print "An error occured while deleting data." + str(e)

    def data_received(self, chunk):
        pass
