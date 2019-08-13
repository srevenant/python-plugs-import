# this version works, but doesn't have a parent class to derive from

class Handler():

    def __init__(self, server):
        pass

    def hello(self, message):
        print("Do what I do. Hold tight and pretend it’s a plan! ...")
        print("<{}>{}: I heard: {}".format(__name__, self, message))
