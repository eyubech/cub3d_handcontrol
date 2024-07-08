import os
import cv2
import numpy as np

def count_fingers_and_draw(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (35, 35), 0)
    _, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresholded.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=lambda x: cv2.contourArea(x))
    hull = cv2.convexHull(contour)
    hull_indices = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull_indices)
    if defects is None:
        return 1, img
    finger_count = 0
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])
        far = tuple(contour[f][0])
        
        a = np.linalg.norm(np.array(start) - np.array(end))
        b = np.linalg.norm(np.array(start) - np.array(far))
        c = np.linalg.norm(np.array(end) - np.array(far))
        
        angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))

        if angle <= np.pi / 2:
            finger_count += 1
            cv2.line(img, start, end, [0, 255, 0], 2)
            cv2.line(img, start, far, [0, 255, 0], 2)
            cv2.line(img, end, far, [0, 255, 0], 2)
            cv2.circle(img, far, 5, [0, 0, 255], -1)
    return finger_count + 1, img
def main():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        roi = frame[100:400, 100:400]
        fingers, processed_roi = count_fingers_and_draw(roi)
        frame[100:400, 100:400] = processed_roi
        cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)
        button = ""
        if fingers == 2:
            button = "w"
            os.system(f'xdotool key {button}')
        elif fingers == 3:
            button = "s"
            os.system(f'xdotool key {button}')
        elif fingers == 4:
            button = "Right"
            os.system(f'xdotool key {button}')
        elif fingers == 5:
            button = "Left"
            os.system(f'xdotool key {button}')
        cv2.putText(frame, f"Button Pressed: {button}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        small_frame = cv2.resize(frame, (640, 480))
        cv2.imshow('Finger Counter', small_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
