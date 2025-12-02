import sys
import os
import cv2

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from roi_selector import ROISelector

def test_roi_logic():
    selector = ROISelector()
    
    # Simulate first click (top-left)
    print("Simulating Click 1 at (10, 10)")
    selector.mouse_callback(cv2.EVENT_LBUTTONDOWN, 10, 10, 0, None)
    assert len(selector.points) == 1
    assert selector.get_roi() == (0, 0, 0, 0) # ROI not set yet
    
    # Simulate second click (bottom-right)
    print("Simulating Click 2 at (100, 100)")
    selector.mouse_callback(cv2.EVENT_LBUTTONDOWN, 100, 100, 0, None)
    assert len(selector.points) == 2
    roi = selector.get_roi()
    print(f"ROI: {roi}")
    assert roi == (10, 10, 90, 90)
    
    # Simulate third click (should reset)
    print("Simulating Click 3 at (50, 50)")
    selector.mouse_callback(cv2.EVENT_LBUTTONDOWN, 50, 50, 0, None)
    assert len(selector.points) == 1
    assert selector.points[0] == (50, 50)
    assert selector.get_roi() == (0, 0, 0, 0)
    
    # Simulate 'r' keypress (should reset)
    print("Simulating 'r' keypress")
    selector.set_roi((0, 0, 0, 0))
    assert len(selector.points) == 0
    assert selector.get_roi() == (0, 0, 0, 0)
    print("PASS")

if __name__ == "__main__":
    test_roi_logic()
