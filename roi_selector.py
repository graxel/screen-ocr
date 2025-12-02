class ROISelector:
    def __init__(self):
        self.roi = (0, 0, 0, 0)  # x, y, w, h
        self.points = []

    def mouse_callback(self, event, x, y, flags, param):
        """
        OpenCV mouse callback function.
        """
        import cv2

        if event == cv2.EVENT_LBUTTONDOWN:
            # If we already have 2 points, start over
            if len(self.points) >= 2:
                self.points = []
                self.roi = (0, 0, 0, 0)
            
            self.points.append((x, y))

            # If we now have 2 points, calculate ROI
            if len(self.points) == 2:
                p1 = self.points[0]
                p2 = self.points[1]
                
                x_start = min(p1[0], p2[0])
                y_start = min(p1[1], p2[1])
                w = abs(p1[0] - p2[0])
                h = abs(p1[1] - p2[1])
                
                self.roi = (x_start, y_start, w, h)

    def get_roi(self):
        return self.roi

    def get_points(self):
        return self.points

    def set_roi(self, roi):
        self.roi = roi
        self.points = []  # Clear points when manually setting/resetting ROI
