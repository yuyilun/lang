#!/usr/bin/env Python
# coding=utf-8
from url import url
import tornado.web
import os
settings = dict(
        template_path = os.path.join(os.path.dirname(__file__), "templates"),
        static_path = os.path.join(os.path.dirname(__file__), "statics"),
        cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        xsrf_cookies = True
)
application = tornado.web.Application(
        handlers = url,
        **settings
)