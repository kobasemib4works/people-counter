from unit import frameClass
from unit import argsClass
from unit import loadVideo
import imutils
import cv2

#####----- Initialize -----#####

args = argsClass.Args().getArgs()
Video = loadVideo.VideoData(args)
videoData = Video.getVideoData()

Frame = frameClass.Frame(args, videoData)
frame = Frame.getFrame()

writer = None

#####----- Main loop -----#####

while True:
    # Load new video frame
    frame = Frame.readVideo()
    frame = frame[1] if args.get("input", False) else frame
    if args["input"] is not None and frame is None:
        print("Video not loaded")
    
    # Exitter
    if frame is None:
        print("End of Video file")
        break

    # Video setting optimisation
    frame = imutils.resize(frame, width=500)
    '''
    print("resize")
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print("rgb converted")
    '''

    # Play Video
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
