import cv2

img = cv2.imread('path_to_img.jpg') #get img 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # make it all gray 

_,binary_map = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY) #(If > 190 make it 255 (white)) + this will loop on its own + 190 threshold 

#count pixels 
white_pixels = cv2.countNonZero(binary_map)
total_pixels =binary_map.size
black_pixels = total_pixels - white_pixels

#Shape Detection
contours, _ = cv2.findContours(binary_map, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for points in contours:
    epsi = cv2.arcLength(points, True)
    approx = cv2.approxPolyDP(points, 0.04 * epsi, True)
    corners = len(approx)
#testing by number of courners
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    else:
        shape_name = "Circle"

#output 
print(f"I found a {shape_name}!")