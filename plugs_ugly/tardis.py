# this one includes the parent class, just as a sanity check:
class Plug():
    server = None

    def __init__(self, server):
        """override if you want the plugin to do anything on server startup"""
        self.server = server
        # override but pass up to this object with super().__init__(server)
        #
        # here you can do something like install a "/path/to/thing" route,
        # on server, if this were used on an HTTP framework with routing

    def hello(self, message):
        """
        There are actually a set of 4 functions that are always called when
        a plug is used as part of the main server framework, but for this example,
        we will use .hello()
        """
        print("<{}>{}: I heard: {}".format(self.__name__, self, message))

class Handler(Plug):
    def hello(self, message):
        print("<I'm Bigger on the Inside>: msg={}".format(message))
