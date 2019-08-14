import cv2
import numpy as np
import os


 def dataset():
     images = []
     labels = []
     labels_dic = {}
     people  = [person for person in os.listdir("people/")]
     for i, person in enumerate(people):
         labels_dic[i] = person
         for image in os.listdir("people/" + person):
             images.append(cv2.imread ("people/" + person + '/' + image, 0))
             labels.append(person)

    return (images, np.array(labels), labels_dic) 

images, labels, labels_dic = collect_dataset()
