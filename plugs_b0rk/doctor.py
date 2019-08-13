from ..util.framework import Plug

class Handler(Plug):
    def hello(self, message):
        print("Do what I do. Hold tight and pretend it’s a plan! ...")
        print("<{}>{}: I heard: {}".format(__name__, self, message))
