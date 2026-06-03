import pyrealsense2 as rs
import numpy as np
import cv2
from skimage.filters import threshold_multiotsu
 
# PARÁMETROS
NUM_CLASES = 4      # 3 objetos + fondo
NUM_OBJETOS = 3     # Detectar solo 3 regiones
AREA_MINIMA = 3000  
 
#CÁMARA
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
        
        #Escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
        #Multi-Otsu
        thresholds = threshold_multiotsu(gray, classes=NUM_CLASES)
        regions = np.digitize(gray, bins=thresholds)
        segmented = (regions * (255 // (NUM_CLASES - 1))).astype(np.uint8)
 
        #Detección
        frame_deteccion = frame.copy()
        regiones_detectadas = 0
        for clase in range(1, NUM_CLASES):
            mask = np.uint8(regions == clase) * 255
            contours, _ = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
 
            if len(contours) > 0:
                cnt = max(contours, key=cv2.contourArea)
                if cv2.contourArea(cnt) > AREA_MINIMA:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(
                        frame_deteccion,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        2
                    )
 
                    cv2.putText(
                        frame_deteccion,
                        f"Clase {clase}",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )
 
                    regiones_detectadas += 1
            if regiones_detectadas >= NUM_OBJETOS:
                break
 
        cv2.imshow("Segmentacion Multi-Otsu", segmented)
        cv2.imshow("Deteccion de Clases", frame_deteccion)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
finally:
 
    pipeline.stop()
 
    cv2.destroyAllWindows()