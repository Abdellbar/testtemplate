import io
import os


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types



# The name of the image file to annotate

def face_joy_joy_likelihood(image_file_name):

	# Instantiates a client
	client = vision.ImageAnnotatorClient()


	# Loads the image into memory
	with io.open(image_file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response_faces = client.face_detection(image=image)
	face_labels = response_faces.face_annotations



	#Creating the response of the function
	the_return = {  "faces" :[],
					"results":{
								"Joy_faces":0,
								"Sorrow_faces":0,
								"Anger_faces":0,
								"Surprise_faces":0,
								"Under_faces":0,
								"Blurred_faces":0,
								"Headwear_faces":0
							  }

				  }
	my_dict={
			"joy_likelihood": "",
			"sorrow_likelihood": "",
			"anger_likelihood": "",
			"surprise_likelihood": "",
			"under_exposed_likelihood": "",
			"blurred_likelihood": "",
			"headwear_likelihood": "",
			"detection_confidence": 0
			}
	for face in face_labels:
		if face.joy_likelihood >=2:
			the_return['results']["Joy_faces"]+=1
		if face.sorrow_likelihood >=2:
			the_return['results']["Sorrow_faces"]+=1
		if face.anger_likelihood >=2:
			the_return['results']["Anger_faces"]+=1
		if face.surprise_likelihood >=2:
			the_return['results']["Surprise_faces"]+=1
		if face.under_exposed_likelihood >=2:
			the_return['results']["Under_faces"]+=1
		if face.blurred_likelihood >=2:
			the_return['results']["Blurred_faces"]+=1
		if face.headwear_likelihood >=2:
			the_return['results']["Headwear_faces"]+=1

		my_dict['joy_likelihood']=face.joy_likelihood
		my_dict['sorrow_likelihood']=face.sorrow_likelihood
		my_dict['anger_likelihood']=face.anger_likelihood
		my_dict['surprise_likelihood']=face.surprise_likelihood
		my_dict['under_exposed_likelihood']=face.under_exposed_likelihood
		my_dict['blurred_likelihood']=face.blurred_likelihood
		my_dict['headwear_likelihood']=face.headwear_likelihood
		my_dict['detection_confidence']=face.detection_confidence
		

		the_return['faces'].append(my_dict)

	
	return the_return