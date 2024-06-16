import cv2
from pytube import YouTube
from fpdf import FPDF
import os
import datetime

# specify the URL of the YouTube video
video_url = input("Enter the URL of the YouTube video: ")

# create a YouTube object and download the video
youtube = YouTube(video_url)
video = youtube.streams.filter(res='720p').first()
video.download()

# open the video using OpenCV and extract the images
cap = cv2.VideoCapture(video.default_filename)

frame_count = 0
while cap.isOpened():
    # read the frame
    ret, frame = cap.read()
    
    if ret:
        # extract an image every 10 seconds
        if frame_count % (10 * int(cap.get(cv2.CAP_PROP_FPS))) == 0:
            # save the image
            cv2.imwrite(f'E:\PYTHON\Python_Project\Video_Images/frame_{frame_count}.jpg', frame)
        
        # increment the frame count
        frame_count += 1
    else:
        break

# release the resources
cap.release()

# create a PDF document from the generated images
pdf = FPDF()
pdf.set_auto_page_break(True)

# get the list of image files
image_folder = 'E:\PYTHON\Python_Project\Video_Images'
images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg')]

# loop through the images and add them to the PDF
for image in images:
    pdf.add_page()
    pdf.image(image, x=10, y=10, w=190)

# generate a unique name for the PDF file
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
pdf_name = f"output_File_{timestamp}.pdf"

# save the PDF document
pdf.output(pdf_name, 'F')

# delete the image files
for image in images:
    os.remove(image)