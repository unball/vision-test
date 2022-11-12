import cv2
import numpy as np

class Homography:
    __homography = []
    __homography_points = []
    __last_configured_shape = ()

    def __calculate_homography(shape):
        height, width, _ = shape
        base = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

        key_points = np.array(
            Homography.__homography_points) * np.array([width, height])
        frame_points = base * np.array([width, height])

        homography, _ = cv2.findHomography(
            key_points, frame_points, cv2.RANSAC)
        
        Homography.__homography = homography
        Homography.__last_configured_shape = shape

    def get_homography_points(shape) -> list:
        if Homography.__last_configured_shape != shape:
            Homography.__calculate_homography(shape)

        return Homography.__homography
