import cv2 

# step 1 get the vid
vid = cv2.VideoCapture(r'C:\work\sms2i\sms2i-AgroDrone\finaltest.mp4') 
#test on the vid input 
if not vid.isOpened():
    print("Error opening the vid file ! ")
    exit()
#test on the frame input
maxobjects = 0 #max number of objects detected in the frame
total_objects_detected = 0 
while True: 
    ret,frame = vid.read()
    if not ret: # side note ret is a boolean value that returns true or false
        print("Error reading frame ! ")
        break
# if step 1 is all correct we have a valid input vid and frame to work with ! 
    objects_detected = 0 #num of objects detected in the frame
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # make it all gray
    _, binary_map = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV) #(If the pixel > than the threshold make it 255 (white))  
    #count pixels for each frame 
    white_pixels = cv2.countNonZero(binary_map)
    total_pixels =binary_map.size
    black_pixels = total_pixels - white_pixels 


# step 2 shape detection 
    contours, _ = cv2.findContours(binary_map, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for countor in contours:
    # Only count if the object is large enough to be an object based on the size we set 
        if cv2.contourArea(countor) > 1300: 
            objects_detected += 1 

        if objects_detected > maxobjects:
            maxobjects = objects_detected
   
#step 3 output res + data + countrol 
    cv2.imshow('Object Detection', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

total_objects_detected = maxobjects
print(f"Total objects detected: {total_objects_detected}")

vid.release()
cv2.destroyAllWindows()