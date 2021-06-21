# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.
import face_recognition
from PIL import Image, ImageDraw
import numpy as np



# Load a sample picture and get the feature.
hank = face_recognition.load_image_file("C:/Users/Lutfi/Downloads/face detection/capture/hank.jpg")
hank_face = face_recognition.face_encodings(hank)[0]



# Load a second sample picture and get the feature.
charan = face_recognition.load_image_file("C:/Users/Lutfi/Downloads/face detection/capture/charan.jpg")
charan_face = face_recognition.face_encodings(charan)[0]


lutfi = face_recognition.load_image_file("C:/Users/Lutfi/Downloads/face detection/capture/lutfi.jpg")
lutfi_face = face_recognition.face_encodings(lutfi)[0]


# Create arrays of known face feature and their names
known_face_encodings = [
    hank_face,
    charan_face,
    lutfi_face
]
known_face_names = [
    "hank",
    "charan",
    "lutfi"
    
]

# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("C:/Users/Lutfi/Downloads/face detection/capture/Capturing.jpg")

# Find all the faces and face features in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.3)
    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
      first_match_index = matches.index(True)
      name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
        print(name)
        f = open('result.txt', 'wb')
        
        if(name !='Unknown'):
            f.write(bytes("1", 'utf-8'))
        else:
            f.write(bytes("0", 'utf-8'))
        f.close()
    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
#display(pil_image)


