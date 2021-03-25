import os
import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0

    def __init__(self):
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        try:
            print "Frame default resolution: (" + str(camera.get(cv2.CV_CAP_PROP_FRAME_WIDTH)) + "; " + str(camera.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)) + ")"
            camera.set(cv2.CV_CAP_PROP_FRAME_WIDTH, 800)
            camera.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 600)
            print "Frame resolution set to: (" + str(camera.get(cv2.CV_CAP_PROP_FRAME_WIDTH)) + "; " + str(camera.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)) + ")"
        except:
            print("Custom resolution not available")


        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
