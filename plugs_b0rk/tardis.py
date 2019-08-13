from ..util.framework import Plug

class Handler(Plug):
    def hello(self, message):
        print("<I'm Bigger on the Inside>: msg={}".format(message))
