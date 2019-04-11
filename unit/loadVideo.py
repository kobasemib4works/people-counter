import cv2

class VideoData:
    def getVideoData(self):
        return self.vs

    def __init__(self, args):
        print("[INFO] opening video file...")
        self.vs = cv2.VideoCapture(args["input"])
        print("video loaded")
