import os
import cv2

dir = "E:/Vedant/Projects/Pothole Detection and Severity Prediction"

paths = ['Pothole 1/images', 'Pothole 2/train/Plain', 'Pothole 2/train/Pothole', 'Pothole 2/test/Plain', 'Pothole 2/test/Pothole']

count = 0

for path in paths:
    for file in os.listdir(os.path.join(dir, path)):
        count += 1
        img = cv2.imread(os.path.join(dir, path, file))
        cv2.imshow(str(count) + " " + file, img)
        key = cv2.waitKey(0)
        if key == ord('1'):
            cv2.imwrite(os.path.join(dir, "PotholeData/PlainRoad", file), img)
            cv2.destroyWindow(str(count) + " " + file)
        elif key == ord('2'):
            cv2.destroyWindow(str(count) + " " + file)
            cv2.imshow("Pothole: Low, Medium or High " + file, img)
            key_in = cv2.waitKey(0)
            if key_in == ord('1'):
                cv2.imwrite(os.path.join(dir, "PotholeData/PotholeRoad/Low", file), img)
                cv2.destroyWindow("Pothole: Low, Medium or High " + file)
            elif key_in == ord('2'):
                cv2.imwrite(os.path.join(dir, "PotholeData/PotholeRoad/Medium", file), img)
                cv2.destroyWindow("Pothole: Low, Medium or High " + file)
            elif key_in == ord('3'):
                cv2.imwrite(os.path.join(dir, "PotholeData/PotholeRoad/High", file), img)
                cv2.destroyWindow("Pothole: Low, Medium or High " + file)
            else:
                cv2.imwrite(os.path.join(dir, "PotholeData/unallocated", file), img)
                cv2.destroyWindow("Pothole: Low, Medium or High " + file)
        else:
            cv2.imwrite(os.path.join(dir, "PotholeData/unallocated", file), img)
            cv2.destroyWindow(str(count) + " " + file)

print(count)