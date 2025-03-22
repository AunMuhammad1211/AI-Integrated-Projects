from detector import HerdDetector
from map_alert import generate_map_alert


def main():
    detector = HerdDetector()
    
    # Use raw string for Windows path (already correct in your code)
    image_path = r"C:\Users\Aun Awan\Desktop\Animal Herd Detection\images\cato.jpg"
    herd_count, coordinates = detector.detect_herd(image_path)
    
    if herd_count > 0:
        print(f"Detected {herd_count} herd clusters.")
        generate_map_alert(coordinates)
    else:
        print("No herd detected in the image.")

if __name__ == "__main__":
    main()