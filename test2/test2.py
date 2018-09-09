from direct.stdpy.file import *
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.interval.IntervalGlobal import *
import cv2
import subprocess

# To see if threading is supported
# print Thread.isThreadingSupported()

X = 000
Y = 3000
Z = 0
# To display camera from cv2
def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()

def drawPanda():
	#loading model
	m = loader.loadModel("./panda-model.egg")
	m.reparentTo(render)
	#set zise
	m.setPos(X, Y, Z)

def test():
	subprocess.Popen("/Users/flor/Documents/Desarrollo/GitHub/panda3d-opencv/test1/test1.py 1")
 
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        drawPanda()
    	# show_webcam(mirror=True)
    	
test()
#app = MyApp()
#app.run()

