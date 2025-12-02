import cv2
import sys
import argparse
from video_processor import VideoProcessor
from roi_selector import ROISelector
from ocr_engine import OCREngine
from utils import draw_roi, crop_frame, draw_cross

def parse_args():
    parser = argparse.ArgumentParser(description="Screen OCR")
    parser.add_argument("--source", default="0", help="Video source: camera index (0, 1, ...) or file path")
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Determine if source is an integer (camera index) or string (file path)
    source = args.source
    if source.isdigit():
        source = int(source)
    
    print(f"Initializing Screen OCR with source: {source}")
    
    try:
        # Initialize components
        video = VideoProcessor(source=source)
        roi_selector = ROISelector()
        ocr = OCREngine()
    except Exception as e:
        print(f"Error initializing components: {e}")
        return

    window_name = "Screen OCR"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, roi_selector.mouse_callback)

    print("Controls:")
    print("  [Click 1]    : Set Top-Left corner")
    print("  [Click 2]    : Set Bottom-Right corner")
    print("  [Space]      : Run OCR on selected region")
    print("  [r]          : Reset ROI")
    print("  [q]          : Quit")

    try:
        while True:
            ret, frame = video.get_frame()
            if not ret:
                print("Failed to grab frame")
                break

            # Draw ROI on a copy of the frame to avoid modifying the original capture for OCR
            display_frame = frame.copy()
            
            # Draw crosses for clicked points
            points = roi_selector.get_points()
            for point in points:
                draw_cross(display_frame, point)

            # Draw ROI rectangle if set
            roi = roi_selector.get_roi()
            draw_roi(display_frame, roi)

            cv2.imshow(window_name, display_frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break
            elif key == ord(' '):  # Spacebar
                if roi[2] > 0 and roi[3] > 0:  # Check if width and height > 0
                    cropped = crop_frame(frame, roi)
                    if cropped is not None:
                        # print("Running OCR...")
                        text = ocr.extract_text(cropped)
                        print()
                        # print("," + "-" * 40 + ",")
                        # print("OCR Result:")
                        print(text)
                        # print("'" + "-" * 40 + "'")
                        print()
                else:
                    print("No ROI selected. Please drag mouse to select a region.")
            elif key == ord('r'):
                roi_selector.set_roi((0, 0, 0, 0))
                print("ROI Reset")

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        video.release()
        cv2.destroyAllWindows()
        print("Screen OCR stopped.")

if __name__ == "__main__":
    main()
