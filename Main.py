import tornado.ioloop
import tornado.web

from ProductHandler import ProductItem
from UserHandler import UserItem


if __name__ == '__main__':
    application = tornado.web.Application([
        (r"/products", ProductItem),
        (r"/products/([0-9]+)", ProductItem),
        (r"/users", UserItem),
        (r"/users/([0-9]+)", UserItem),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
