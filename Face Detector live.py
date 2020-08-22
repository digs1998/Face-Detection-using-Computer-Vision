#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


#capture the video from webcam
cap = cv2.VideoCapture(0)

#Using CascadeClassifier
face_cascade = cv2.CascadeClassifier('C:/Users/digvi/Downloads/haarcascade_frontalface_alt.xml')


# In[3]:


while True:
    
    #Read the webcam Image
    ret, frame = cap.read()
    
    #if not able
    if ret == False:
        continue
    # Detecting faces on current frame
    faces = face_cascade.detectMultiScale(frame)
    
    # Plot rectangle around all the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


    # Display the frame
    cv2.imshow("Video Frame", frame)


    # Find the key pressed
    key_pressed = cv2.waitKey(1) & 0xFF

    # If keypressed is q then quit the screen
    if key_pressed == ord('q'):
        break


# release the camera resource and destroy the window opened.
cap.release()
cv2.destroyAllWindows()


# In[ ]:




