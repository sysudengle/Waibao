import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/home.html")

class CompanyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/company.html")

class ProductHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/product.html")

class FaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/faq.html")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/company", CompanyHandler),
        (r"/product", ProductHandler),
        #(r"/news", MainHandler),
        (r"/faq", FaqHandler),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": "./images"},),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
