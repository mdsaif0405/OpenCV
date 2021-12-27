import cv2

rec = cv2.VideoCapture(0)
while(True):
    ret, frame = rec.read()

    # Change colorspace:
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

rec.release()
cv2.destroyAllWindows()