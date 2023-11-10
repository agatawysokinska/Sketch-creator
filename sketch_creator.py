import cv2

def create_sketch(image_path):

    image = cv2.imread(image_path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_invert = cv2.bitwise_not(image_gray)
    blurred = cv2.GaussianBlur(image_invert, (39, 39), 0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(image_gray, inverted_blur, scale=256.0)

    return image, sketch

def main():

    image_path = 'example.jpg'

    try:
        original_image, sketch_image = create_sketch(image_path)

        cv2.imshow("Original", original_image)
        cv2.imshow("Sketch", sketch_image)
        cv2.waitKey(0)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
