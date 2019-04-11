# require module
import argparse

# Initlize
class Args:
    def getArgs(self):
        return self.args

    def __init__(self):
        ap = argparse.ArgumentParser()
        ap.add_argument("-p", "--prototxt", required=True,
                help="path to Caffe 'deploy' prottxt file")
        ap.add_argument("-m", "--model", required=True,
                help="path to Caffe pre-trained model")
        ap.add_argument("-i", "--input", type=str,
                help="path to optional input video file")
        ap.add_argument("-o", "--output", type=str,
                help="path to optional output video file")
        self.args = vars(ap.parse_args())
