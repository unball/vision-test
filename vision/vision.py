import numpy as np
import cv2

from config.vision import VisionConfig
from vision.math_utils import normToAbs
from vision.frame_utils import crop

def warp_field(frame):
    if not VisionConfig.useHomography:
        crop_points = VisionConfig.cropPoints
        if crop_points:
            rect_p0 = normToAbs(crop_points[0], frame.shape)
            rect_p1 = normToAbs(crop_points[1], frame.shape)
            return crop(frame, rect_p0, rect_p1)
        else:
            return frame
    else:
      homography_matrix = get_homography(homography_points, frame.shape)
      try:
        return cv2.warpPerspective(frame, np.array(homography_matrix), (frame.shape[1], frame.shape[0]))
      except:
        return frame

def get_homography(points, shape):
    
    VisionConfig.get_homography(homography.shape)
    return homography

