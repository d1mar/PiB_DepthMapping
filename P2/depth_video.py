#file needs to be in python directory under libfreenect
import freenect
import cv2
import frame_convert2
import numpy as np


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])

def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])

def main():
#Depth
    Depth = get_depth()
    print(get_depth())
    #saving depth as jpg
    image = cv2.imwrite('depth_img.jpg', Depth)
    #saving depth as csv file
    np.savetxt('depth_data.csv', Depth, delimiter=',')
#Video
    Video = get_video()
    print(get_video())
    #saving video as jpg
    video = cv2.imwrite('video_img.jpg', Video)
    #savign video as csv file
    np.savetxt('video_data.csv', Video, delimiter=',') 
main()
