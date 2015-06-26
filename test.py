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

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/test.html")

class NewsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/news.html")

class FaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/faq.html")

class ComputeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/compute.html")

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/contact.html")


class CHNMainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cnhome.html")

class CHNCompanyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cncompany.html")

class CHNProductHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cnproduct.html")

class CHNTestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cntest.html")

class CHNNewsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cnnews.html")

class CHNFaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cnfaq.html")

class CHNComputeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cncompute.html")

class CHNContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./views/cncontact.html")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/^solbrighttech.com$", MainHandler),
        (r"/", MainHandler),

        (r"/company", CompanyHandler),
        (r"/product", ProductHandler),
        (r"/news", NewsHandler),
        (r"/test", TestHandler),
        (r"/faq", FaqHandler),
        (r"/compute", ComputeHandler),
        (r"/contact", ContactHandler),


        (r"/cn", CHNMainHandler),
        (r"/cn/company", CHNCompanyHandler),
        (r"/cn/product", CHNProductHandler),
        (r"/cn/news", CHNNewsHandler),
        (r"/cn/test", CHNTestHandler),
        (r"/cn/faq", CHNFaqHandler),
        (r"/cn/compute", CHNComputeHandler),
        (r"/cn/contact", CHNContactHandler),

        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": "./images"},),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css"},),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js"},),
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
