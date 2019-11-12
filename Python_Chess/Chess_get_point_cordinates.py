import cv2


img1 = cv2.imread("Python_Chess/Images/1.jpg")
img1 = cv2.resize(img1,(800,800))

# cv2.imshow("chess",img1)
cv2.waitKey(0)

ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img1,(x,y),5,(255,0,0),-1)
        ix,iy = x,y

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
# cv2.line(img1, (38,127), (774,118), (255,0,0), 2)
point1 = []
point2 = []
def draw_lines(X,Y):
    for i in range(len(X)):
        cv2.line(img1, (X[i][0],X[i][1]), (Y[i][0],Y[i][1]), (255,0,0), 2)

while(1):
    cv2.imshow('image',img1)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    elif k == ord('a'):
        print("Point a cordinates is : ",ix,iy)
        point1.append([ix,iy])
    elif k == ord('b'):
        print("Point B cordinates is : ",ix,iy)
        point2.append([ix,iy])
    elif k == ord('d'):
        draw_lines(point1,point2)


cv2.waitKey(0)

cv2.destroyAllWindows()