import cv2

img = cv2.imread(r'C:\work\sms2i\sms2i-AgroDrone\infectedplanttest.jpg') #get img 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # make it all gray 

_,binary_map = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) #(If the pixel > than the threshold make it 255 (white)) 

#count pixels 
white_pixels = cv2.countNonZero(binary_map)
total_pixels =binary_map.size
black_pixels = total_pixels - white_pixels

#Shape Detection
contours, _ = cv2.findContours(binary_map, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

shape_name="Unknown"
infection=0
for points in contours: 
    #this so we skip logos/text so it doesnt count them as objects 
    area = cv2.contourArea(points)
    if area < 20:
        continue
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
        infection=infection+1


#output 
    print(f"I found a {shape_name}!")
    
    if not contours:
        print("No contours found")
#print total num of products based on test img num 2 !
print("this plant is infected :"+" "+ str(infection) )