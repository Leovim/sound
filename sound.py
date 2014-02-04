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
        items = ["Leo", "Tom"]
        self.render("index.html", title="Sound Like", name=items[0])


# route
application = tornado.web.Application([
    (r"/", IndexHandler),
], **settings
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
