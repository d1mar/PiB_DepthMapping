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
    Depth = get_depth()
    print(get_depth())
    image = cv2.imwrite('depth_img.jpg', Depth)
    Video = get_video()
    np.savetxt('depth_data.csv', Depth, delimiter=',')
    #image_data('depth_data.csv'.format('123','456'),Depth)
    print(get_video())
    video = cv2.imwrite('video_img.jpg', Video)
    #image_data('{}/{}_rgb_data.csv'.format(directory,directory),get_video)

main()
