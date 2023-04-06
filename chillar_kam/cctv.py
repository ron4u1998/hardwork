import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture('rtsp://admin:1998Samyak@10.100.112.232')
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    x = cv2.resize(frame, (1280,720))  
    # Display the resulting frame
    cv2.imshow('frame', x)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
