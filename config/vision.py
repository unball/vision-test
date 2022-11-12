import numpy as np
import cv2


class VisionConfig():
    useHomography = False
    cropPoints = []
    points = []
    shape = []

    __homography = []
    __homography_points = []

    def __update_homography_points(shape):
        height, width, _ = shape
        base = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

        key_points = np.array(
            VisionConfig.__homography_points) * np.array([width, height])
        frame_points = base * np.array([width, height])

        homography, _ = cv2.findHomography(
            key_points, frame_points, cv2.RANSAC)

        VisionConfig.__homography = homography

    def get_homography_points() -> list:

        return VisionConfig.__homography
