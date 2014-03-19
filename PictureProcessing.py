#!/usr/python
# -*- coding: utf-8 -*-

"""
------------------------------------------------
date: 18/03/2014
author: Kévin Renévot, Thomas Elain
version : 1.1
------------------------------------------------

"""

import sys, os
import cv2, time
from PIL import Image

class PictureProcessing:
  
    def detectFaces (image):
        """  Detect the faces on the picture passed in parameter and return the area of faces detected  """

        img = cv2.imread(image) # Picture loading in memory

        face_model = cv2.CascadeClassifier("/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml") 
     
        faces = face_model.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))   # Face detection
        faces [:, 2:] += faces[:, :2]

        return faces


    def facesBlurring (faces, image):
        """  Apply a blur on face detected thanks to the first parameter and return the picture blurred  """

        img = cv2.imread(image)

        for x1, y1, x2, y2 in faces:

            crop_img = img[y1:y2, x1:x2]
            crop_img = cv2.GaussianBlur(crop_img,(51,51),0)

            img[y1:y2, x1:x2] = crop_img

        return img


    def saveImage (img):
        """  Save the picture passed in first parameter under the picture name passed in second parameter """

        date = time.strftime('%Y-%m-%d', time.localtime())
        hour = time.strftime('%H:%M:%S', time.localtime())

        folder = "out/"+ date + "/"

        # If the folder doesn't exist
        if not os.path.isdir( folder ):
            os.makedirs( folder )

        file_name = date + "-" + hour + ".jpg"
        sucessSave = cv2.imwrite(folder + file_name, img)

        file_name = "current.jpg"
        sucessSave = cv2.imwrite(folder + file_name, img)

        # If the picture recording failed
        if not sucessSave:
            print "The picture could not be saved here : " + folder + file_name
        else:
            print "Picture has been saved at " + date + "-" + hour


    if __name__ == "__main__":

        """  Allowed file formats : png,jpg, jpeg
             Every picture files will be processed (detection and blurring of the faces) abd then saved.
             Files containing 'faces' at the beginning of their names are not processed  """

        for file in os.listdir(".") :                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

            if file.startswith("visage") : continue # déjà traité

            if os.path.splitext(file)[-1].lower() in [".jpg", ".jpeg", ".png" ] :
                faces = detecte_visages (file)
                img = imageBlurring (faces, file)
                saveImage (img, "visage_" + file)
