# panda3d-opencv

The idea is to project in a screen a 3D model of a model made on Panda3D whose position and orientation matches the position and orientation of some predefined flat surface in real time, so that if the surface changes its position or orientation the projected model does so accordingly.

We need to identify the flat surface of reference in an image or video frame. Then, determine the transformation from the reference surface image (2D) to the target image (2D). This transformation is called homography. However, if what we want is to project a 3D model placed on top of the reference surface to the target image we need to extend the previous transformation to handle cases were the height of the point to project in the reference surface coordinate system is different than zero. This can be achieved with a bit of algebra. Finally, we should apply this transformation to our 3D model and draw it on the screen.

For this project I'm using:
1) <b>Python</b>
2) <b>OpenCV</b>
3) <b>numpy</b>
4) <b>Panda3D</b>

