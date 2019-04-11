import imutils

class Frame:
    def setFrame(self, frame):
        self.frame = frame
        
    def getFrame(self):
        return self.frame

    def setWidth(self, w):
        self.W = w

    def getWidth(self):
        return self.W

    def setHeight(self, h):
        self.H = h

    def getHeight(self):
        return self.H

    def readVideo(self):
        self.frame = self.video.read()
        return self.frame

    def __init__(self, args, video):
        self.video = video
        self.frame = self.video.read()
        self.frame = self.frame[1] if args.get("input", False) else self.frame
        self.W = None
        self.H = None
        #print(self.frame)
