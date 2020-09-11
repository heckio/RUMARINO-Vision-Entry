import os
from fileutils import files2list , list2file
from darknetutils import darknet_train

#creating test and train files
path = "/home/ed/RUMARINO-Vision-Entry/images"
file_extension = "jpg"
filetrain = "train.txt"
filetest = "test.txt"
list2file(filetrain, files2list(path, file_extension),path)
list2file(filetest, files2list(path, file_extension),path)


#changing path for test and train on detector.data
ddpath = "/home/ed/RUMARINO-Vision-Entry/model/detector.data"
cnpath = "/home/ed/RUMARINO-Vision-Entry/model/custom.names"
#dd for detector data
pathT ="/home/ed/RUMARINO-Vision-Entry/src/"
with open(ddpath) as oFile:
    lines = oFile.readlines()
    oFile.close()
    lines[1]=f"train={pathT}{filetrain}\n"
    lines[2]=f"valid={pathT}{filetest}\n"
    lines[3]=f"names={cnpath}\n"
    lines[4]=f"backup={pathT}\n"
with open(ddpath, 'w') as oFile:
    oFile.writelines(lines)
    oFile.close()

    
#running darknet training command
darknet = "/home/ed/darknet/darknet"
model = "/home/ed/RUMARINO-Vision-Entry/model/yolov3-tiny-generated.cfg"
trained_weights = "/home/ed/darknet/yolov3.weights"
darknet_train(darknet, ddpath, model, trained_weights)
