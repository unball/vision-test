from  behave import given, when, then
import cv2
import unittest

tc = unittest.TestCase()

@given(u'I have the {path}')
def i_have_the_image(context, path):
    img = cv2.imread(f'features/steps/fixtures/{path}', cv2.IMREAD_UNCHANGED)
    tc.assertIsNotNone(img)
    
    width = int(img.shape[1] / 100)
    height = int(img.shape[0] / 100)
    tc.assertGreater(width, 0)
    tc.assertGreater(height, 0)


@when(u'I calc the robot positions')
def calc_robot_positions(context):
    
    raise NotImplementedError(u'STEP: When I calc the robot positions')
 
   
@then(u'It should have the {return_tuple}')
def check_image_extraction(context):
    raise NotImplementedError(u'STEP: Then It should have the {return_tuple}')