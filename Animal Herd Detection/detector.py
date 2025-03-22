import cv2

class HerdDetector:
    def __init__(self):
        pass

    def detect_herd(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not found or invalid path.")
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        herd_count = 0
        coordinates = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                herd_count += 1
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    lat = 37.7749 + (cY / img.shape[0]) * 0.01
                    lon = -122.4194 + (cX / img.shape[1]) * 0.01
                    coordinates.append((lat, lon))
        
        cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
        cv2.imwrite("output/processed_image.jpg", img)
        
        return herd_count, coordinates