import pyrealsense2 as rs
import numpy as np
import cv2
from skimage.filters import threshold_multiotsu   

NUM_OBJETOS = 4   

# Start streaming
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        frame = np.asanyarray(color_frame.get_data())

        # grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thresholds = threshold_multiotsu(gris, classes=NUM_OBJETOS)

        regions = np.digitize(gris, bins=thresholds)

        # 4 tipos de gris
        multi = (regions * (255 // NUM_OBJETOS)).astype(np.uint8)

        contours, _ = cv2.findContours(
            multi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        contours = contours[:NUM_OBJETOS]

        # bounding box
        for i, cnt in enumerate(contours):
            if cv2.contourArea(cnt) > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
                cv2.putText(
                    frame,
                    f"Objeto {i+1}",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0,255,0),
                    2
                )

        cv2.imshow("3 objetos", frame)
        cv2.imshow("Multiumbral a 4 grises", multi)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
