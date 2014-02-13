import os
import tornado.ioloop
import tornado.web

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug": True,
}


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Leo_c_t", "Tom"]
        self.render("index.html", title="Sound Like Hot", name=items[0])

# route
application = tornado.web.Application([
    (r"/", IndexHandler),
], **settings
)

if __name__ == "__main__":
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
