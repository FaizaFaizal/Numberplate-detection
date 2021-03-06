import cv2
import numpy as np
#pip install pytesseract
#Download and install tesseract
#https://github.com/UB-Mannheim/tesseract/wiki
#importing and loading pytesseract
import pytesseract
#pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd=r'C:\\Users\Baiju\\Downloads\\tesseract-ocr-w64-setup-v5.1.0.20220510.exe'

pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'  # tesseract installation directory


#loading haar
car_haar=cv2.CascadeClassifier("myhaar.xml")

#loading image
img=cv2.imread("Cars\\img2.jpg")
#img=cv2.imread("cars\\car2.jpg")

#copy of input image
img_res=img.copy()
roi=img.copy()

#converting image to grayscale
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detecting car

cars=car_haar.detectMultiScale(img_gray,scaleFactor=1.35,minNeighbors=3,minSize=(300,300))
for (x,y,w,h) in cars:
	cv2.rectangle(img_res,(x,y),(x+w,y+h),(0,255,0),1)
	#saving detected car image in roi(region of interest)
	roi=img[y:y+h,x:x+w]

#DETECTING NUMBER PLATE FROM CAR roi

roi_copy=roi.copy()
#coversion of roi to gray
roi_gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
#roi_gray=cv2.cvtColor(roi_copy,cv2.COLOR_BGR2GRAY)



#smoothening of roi_gray (bilateralFilter : removes noise while preserving edges)
roi_bilateral=cv2.bilateralFilter(roi_gray,11,17,17)	#(image on which to perform,diameter of pixel neighbour,sigma color,sigma space)

#detecting edges in roi_bilateral using canny edge detection
roi_canny=cv2.Canny(roi_bilateral,140,230)				#(image on which to perform,1st thrshold value,2nd threshold value)


#finding contours of rectangle shape
contours,_=cv2.findContours(roi_canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)    #(,mode ,method)
contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]
number_plate = np.array([])
for contour in contours:
	approx=cv2.approxPolyDP(contour,0.02*cv2.arcLength(contour,True),True)	  #(approxPolyDP : for detecting the polygon. parameters (contour,approximation*length of contour(contour out of contours, is it closed fig),is it closed figure))
	print("COUNT:",approx)
	if (len(approx)==4):
		number_plate=approx
		break
	# cv2.drawContours(roi_copy,approx,-1,(0,255,0),2)


#drawing contour on the plate
# print(number_plate)												#number_plate contains numpy array of 4 points of no. plate
cv2.drawContours(roi_copy,[number_plate],-1,(255,0,0),2)			#(image on which contour to be drawn,contour,-1(for all or put here 0 for this example),color,thickness)

#Creating a mask using numpy to plot only number plate
nplate=np.zeros(roi.shape,np.uint8)
cv2.drawContours(nplate,[number_plate],-1,(255,255,255),-1)			#(image on which contour to be drawn,contour,-1(for all or put here 0 for this example),color,thickness)
nplate=cv2.bitwise_and(nplate,roi)



#detect text from image
text=pytesseract.image_to_string(nplate)

print("PLATE DATA:",text)

print("Done...")


#path for saving number plate image
save_as=r"car_plate_detection_with_number\\" + text + ".jpg"

#croping the number plate to new image
x,y,w,h = cv2.boundingRect(number_plate)
final_image = roi[y:y+h, x:x+w]
cv2.imwrite(save_as,final_image)

#Displaying
cv2.imshow("1.Original Image",img)
cv2.imshow("2.Grayscle Image",img_gray)
cv2.imshow("3.Resultant Image",img_res)
cv2.imshow("4.Detected Car",roi)
cv2.imshow("5.Detected Car Gray",roi_gray)
cv2.imshow("6.Smoothen Car Gray",roi_bilateral)
cv2.imshow("7.Edge Detection Car Gray",roi_canny)
cv2.imshow("8.Detected number plate",roi_copy)
cv2.imshow("9.Number plate",nplate)
cv2.imshow("10.Only Number plate",final_image)

#Exit from program
if cv2.waitKey(0)==27:
	cv2.destroyAllWindows()
print("Okay....bye 2.car...")
