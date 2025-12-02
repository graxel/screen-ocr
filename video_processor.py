import cv2

class VideoProcessor:
    def __init__(self, source=0):
        """
        Initializes the video capture.
        source: Video source index (default 0 for webcam) or file path.
        """
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise ValueError(f"Could not open video source {source}")

    def get_frame(self):
        """
        Reads a frame from the video source.
        Returns: (ret, frame)
        """
        return self.cap.read()

    def release(self):
        """
        Releases the video capture resource.
        """
        if self.cap.isOpened():
            self.cap.release()
