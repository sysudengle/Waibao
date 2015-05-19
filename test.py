import tornado.ioloop
import tornado.web
import tornado.autoreload
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/home.html")

class CompanyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/company.html")

class ProductHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/product.html")

class NewsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/news.html")

class FaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/faq.html")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/company", CompanyHandler),
        (r"/product", ProductHandler),
        (r"/news", NewsHandler),
        (r"/faq", FaqHandler),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": "./images"},),
    ])

    #application.add_handlers(r"^solbrighttech\.com$", [
    #    (r"/", MainHandler),
    #    (r"/company", CompanyHandler),
    #    (r"/product", ProductHandler),
    #    #(r"/news", MainHandler),
    #    (r"/faq", FaqHandler),
    #    (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": "./images"},),
    #])
    application.listen(8888)
    tornado.autoreload.start()
    for dir, _, files in os.walk('static'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]
    for dir, _, files in os.walk('static'):
        [tornado.autoreload.watch(dir + '/views/' + f) for f in files if not f.startswith('.')]
    tornado.ioloop.IOLoop.instance().start()
