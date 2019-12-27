import cv2
import numpy as np


device = cv2.VideoCapture("http://192.168.1.136:4812/video")
# cv2.waitkey(100)
ret , img = device.read()
img  = img[582:582+1090,0:1078]
img = cv2.resize(img,(800,800))

# img = cv2.imread("Python_Chess_initial_programs/Images/1.jpg")
# img = cv2.resize(img,(800,800))
# cv2.imshow("img",img)

# gaussian_blur = cv2.GaussianBlur(img,(5,5),0)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,iterations=2)
# opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)

HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# # for White
# lower_1 = np.array([16,25,179])
# lower_2 = np.array([255,255,255])

# # for Black
# lower_1 = np.array([0,0,0])
# lower_2 = np.array([255,62,77])

# for testing 
lower_1 =  np.load("Python_chess_intermediate_programs/numpy_saved/chess_w_color_points.npz")['lower']
lower_2 = np.load("Python_chess_intermediate_programs/numpy_saved/chess_w_color_points.npz")['upper']

mask = cv2.inRange(HSV, lower_1, lower_2)
cv2.imshow("Mask",mask)


# points = [[[ 40.,35.],[132.,34.],[223.,32.],[314., 33.],[405. , 30.],[500. , 29.],[589. , 26.],[683. , 26.] ,[777. , 25.]],
#           [[ 38., 127.],[129., 126.],[221., 124.],[313., 123.],[405., 123.], [496., 121.],[589., 119.],[680., 118.],[774., 118.]],
#           [[36., 218.],[128., 217.],[220., 216.],[312., 215.],[403., 214.],[495., 212.],[588., 210.],[680., 210.],[773., 209.]],
#           [[33., 310.],[124., 309.],[219., 308.],[310., 307.],[400., 305.],[492., 302.],[584., 302.],[677., 301.],[772., 300.]],
#           [[ 32., 399.],[124., 398.],[216., 398.],[309., 395.],[400., 394.],[491., 394.],[583., 394.],[679., 393.],[771., 393.]],
#           [[ 28., 493.],[120., 489.],[214., 488.],[306., 486.],[399., 485.],[491., 483.],[584., 484.],[676., 483.],[769., 483.]],
#           [[ 27., 583.],[120., 582.],[212., 580.],[304., 579.],[396., 579.],[490., 576.],[583., 577.],[677., 576.],[772., 576.]],
#           [[ 24., 677.],[118., 675.],[210., 674.],[304., 672.],[396., 672.],[488., 670.],[583., 670.],[676., 670.],[768., 670.]],
#           [[ 24., 770.],[116., 770.],[209., 770.],[301., 767.],[395., 766.],[488., 766.],[582., 767.],[675., 765.],[769., 766.]]]

points = np.load("Python_chess_intermediate_programs/numpy_saved/chess_board_points.npz")['points']

boxes = np.zeros((8,8,4))

for i in range(8):
    for j in range(8):
        # print(i,j)
        boxes[i][j][0] = points[i][j][0]
        boxes[i][j][1] = points[i][j][1]
        boxes[i][j][2] = points[i+1][j+1][0]
        boxes[i][j][3] = points[i+1][j+1][1]

# print(boxes)


# for i in range(8):
#     for j in range(8):
#         box1 = boxes[i,j]
#         cv2.rectangle(mask, (int(box1[0]), int(box1[1])), (int(box1[2]), int(box1[3])), (255,0,0), 2)
#         cv2.putText(mask,"({},{})".format(i,j),(int(box1[2])-70, int(box1[3])-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
#         cv2.imshow("Mask",mask)
#         # cv2.waitKey(0)

# cv2.waitKey(0)


contours,_= cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

required_contoures = []
required_contoures_mid_point = []
cnt_rect = []

for cnt in contours:
    area = cv2.contourArea(cnt)
    if(area > 300):
        # M = cv2.moments(cnt)
        # cX = int(M["m10"] / M["m00"])
        # cY = int(M["m01"] / M["m00"])
        # required_contoures.append(cnt)
        # required_contoures_mid_point.append([cX,cY])
        (x, y, w, h) = cv2.boundingRect(cnt)
        # cnt_rect.append([x,y,w,h])
        required_contoures.append(cnt)
        required_contoures_mid_point.append([x+int(w/2),y+int(h/2)])
        # cv2.circle(img,(required_contoures_mid_point[-1][0],required_contoures_mid_point[-1][1]),2,(0,0,255),-1)
        # cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
        # cv2.drawContours(img,cnt,-1,(0,0,255),2)

def rectContains(rect,mid_point):
    logic = rect[0]<mid_point[0]<rect[2] and rect[1]<mid_point[1]<rect[3]
    return logic

for i in range(8):
    for j in range(8):
        for mid_point in required_contoures_mid_point:
            if(rectContains(boxes[i][j],mid_point)):
                cv2.rectangle(img,(int(boxes[i][j][0]),int(boxes[i][j][1])),(int(boxes[i][j][2]),int(boxes[i][j][3])),(255,0,0),2)
                cv2.putText(img,"({},{})".format(i,j),(int(boxes[i][j][2]-70),int(boxes[i][j][3])-50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
cv2.imshow("img",img)


cv2.waitKey(0)
cv2.destroyAllWindows()