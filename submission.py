"""
2D visual odometry

"""

import numpy as np
import cv2
import math
import os 

def get_test_images(img,theta_deg,tx,ty):
    rows,cols = img.shape[:2]
    #the point around which we rotate
    rot_center = (rows/2,cols/2)
    # Get the 2X3 tranformation matrix around the center of the image
    M1 = cv2.getRotationMatrix2D(rot_center,-theta_deg,1) 
    dst = cv2.warpAffine(img,M1,(cols,rows))
    M2 = np.float32([[1,0,-tx],[0,1,-ty]])
    dst = cv2.warpAffine(dst,M2,(cols,rows))
    return dst


def get_transform(img1, img2, lens_hight = 1, censor_lens_dist = 1):
    
    ## Create ORB object to find features with 
    orb = cv2.ORB_create()
    
    
    ## Find the keypoints and descriptors with ORB
    kpts1, descs1 = orb.detectAndCompute(img1,None)
    kpts2, descs2 = orb.detectAndCompute(img2,None)
    
    ## match descriptors and sort them by distance
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descs1, descs2)
    dmatches = sorted(matches, key = lambda x:x.distance)
    
        
    ## extract the matched keypoints from "kpts" objects and convert them to type np.float32
    src_pts  = np.float32([kpts1[m.queryIdx].pt for m in dmatches]).reshape(-1,1,2)
    dst_pts  = np.float32([kpts2[m.trainIdx].pt for m in dmatches]).reshape(-1,1,2)
    ## Find the homography matrix (which is just a matrix [R|T] in this scenario)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    mask = mask.ravel()
    ## Select inlier data points
    src_pts=src_pts[mask == 1]
    dst_pts=dst_pts[mask == 1]
    ## draw 10 matched points
    res = cv2.drawMatches(img1, kpts1, img2, kpts2, dmatches[:10],None,flags=2)
    cv2.imshow("orb_match", res)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    ## get the robot's rotation angle from the homography matrix
    robot_rot = math.acos(M[0][0])*180/np.pi
    ## The homography matrix "M" is given relative to img1's coordinate system,
    ## thus the translation in M's 3rd column is the upper left corner translation.
    ## Assuming the camera is positioned inbetween the differential drive, the 
    ## axis of rotation is in the middle, and so we need the translation of img1's
    ## center point.
    h,w = img1.shape[:2]
    center_pt = np.float32( [h/2,w/2]).reshape(-1,1,2)       # image center point
    T_center_pt = cv2.perspectiveTransform(center_pt,M)      # center point transformed 
    robot_translation = center_pt-T_center_pt
    
    ## check result:
    print("angle: {0}, translation: {1}" .format(robot_rot,robot_translation) )
    ## return transformation vector
    pos = [np.float32(robot_rot), robot_translation*lens_hight/censor_lens_dist]
    return(pos)
    
   
    
def main():
    img1 = cv2.imread("wood floor.jpg")
    rot_angle = input("Please enter the robot's rotation angle (degrees):")
    rot_angle=np.float32(rot_angle)
    tran_x = input("Please enter the robot's x translation:")
    tran_x=np.float32(tran_x)
    tran_y = input("Please enter the robot's y translation:")
    tran_y=np.float32(tran_y)
    
    
    img2 = get_test_images(img1,rot_angle,tran_x,tran_y)
    
    print(get_transform(img1, img2))
    
    
    
    
    cv2.imshow('img at time t',img1)
    cv2.imshow('img at time t+1',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    
    
if __name__ == "__main__":
    main()