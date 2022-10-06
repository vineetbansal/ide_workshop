import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread



images = []
for subject_no in range(1, 21):
    image = imread('datasets/att_faces_centered/subject_{}_1.jpg'.format(subject_no)).flatten()
    images.append(image)

X = np.vstack(images)

average_face = np.mean(X, axis=0)
matplotlib.use('TkAgg')
plt.imshow(average_face.reshape((64, 64)), cmap='gray')
plt.show()
