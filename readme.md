# Tier3 
This repository is combining a lot of smaller projects, sometimes the steps taken to reach a larger project.
The repo contains the following:-
## 1. Edge detection
Edge detection is a major part of computer vision. I wanted to understand it better, so decided to make a small project trying out different ways to implement my own edge detection.

#### My implementations

Motivation:
[Coursera course video](https://www.coursera.org/learn/convolutional-neural-networks/lecture/4Trod/edge-detection-example)
This is the video from the CNN course that prompted me to try out edge detection implementation.

---Single edge detection---

This shows you how to detect a single edge in a image, either vertical or horizontal.
The data was generated inside the notebook itself, so no actual image was used.

![](https://github.com/AmarCodes-22/tier-3/blob/main/edge%20detection/outputs/single%20edge%20detection%20horizontal.png)

![](https://github.com/AmarCodes-22/tier-3/blob/main/edge%20detection/outputs/single%20edge%20detection%20vertical.png)

---Boundary detection---

After grayscaling the image, i used the same filter on the binarized image two times and generated different outputs.
I then also averaged the two outputs to show both edges combined. 
The image on the right definitely has more information than the two first ones.

![](https://github.com/AmarCodes-22/tier-3/blob/main/edge%20detection/outputs/boundary_detection.png)

---Colorful edge detection---

This time the edge detection was applied on colorful image.
The results were very amusing :)

![](https://github.com/AmarCodes-22/tier-3/blob/main/edge%20detection/outputs/colorful%20edge%20detection.png)

---Canny edge detector---
This is the most popular edge detector used nowadays, it works on grayscale images only.
You can apply this easily using opencv's Canny function.

![](https://github.com/AmarCodes-22/tier-3/blob/main/edge%20detection/outputs/canny%20edges.png)

That is all for this project. I hope it helps you understand things a little better.