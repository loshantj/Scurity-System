import cv2
import pyttsx3
import playsound

engine = pyttsx3.init() # object creation
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

face_brain = cv2.CascadeClassifier("face-ai-brain.xml")

video_device = cv2.VideoCapture(0) # Get video / open device

while True: # Looping
	ret, frame = video_device.read() #get frame
	gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	faces = face_brain.detectMultiScale(gray_frame,1.3,5)

	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)

	def talk_function(text):
		engine.say(text)
		engine.runAndWait()

	if len(faces) > 0:
		talk_function("i am find a wrong man please activate security system")
		playsound.playsound("music.mp3")
		talk_function("door 1 closed")

	cv2.imshow("Display-1", frame)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_device.release()
cv2.destroyAllWindows()