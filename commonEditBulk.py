import os
import cv2
import zipfile
from io import BytesIO
from PIL import Image
import shutil







def resizeImgs(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg"):
            file_path = os.path.join(dir_path, filename)
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            if size_mb > 1:
                print(f"{filename} ({size_mb:.2f} MB)")
                img = cv2.imread(file_path)
                height, width, channels = img.shape
                new_width = int(width * 0.5)
                new_height = int(height * 0.5)
                resized_img = cv2.resize(img, (new_width, new_height))
                cv2.imwrite(file_path, resized_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                new_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"{new_size_mb:.2f} MB")



def readfromzip():
    with zipfile.ZipFile('uploads.zip', 'r') as archive:

    # iterate over all files in the archive
        for file in archive.namelist():

        # check if the file is an image by trying to open it with Pillow
            try:
                with archive.open(file) as f:
                    img = Image.open(BytesIO(f.read()))
                    print(f"{file} is an image with dimensions {img.size}")
            except:
            # if the file cannot be opened with Pillow, it is not an image
                print(f"{file} is not an image")





def convertGrayScale(zip_file_path, output_directory):
    # Extract the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_directory)

    # Iterate over extracted files
    for root, _, files in os.walk(output_directory):
        for file in files:
            # Check if the file is an image (you can modify this condition as per your requirements)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)

                # Load the image using OpenCV
                image = cv2.imread(image_path)

                # Convert the image to grayscale
                grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # Save the grayscale image
                output_path = os.path.join(root, f"grayscale_{file}")
                cv2.imwrite(output_path, grayscale_image)

                print(f"Converted {file} to grayscale: {output_path}")

    print("Image conversion completed.")





def sharpenZipImg(zip_file_path, sharpen_percentage):
    # Create a temporary directory to extract and process the images
    temp_directory = "temp"
    os.makedirs(temp_directory, exist_ok=True)

    # Extract the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_directory)

    # Iterate over extracted files
    for root, _, files in os.walk(temp_directory):
        for file in files:
            # Check if the file is an image (you can modify this condition as per your requirements)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)

                # Load the image using OpenCV
                image = cv2.imread(image_path)

                # Sharpen the image
                sharpened_image = cv2.convertScaleAbs(image, alpha=1.0 + sharpen_percentage/100, beta=0)

                # Save the sharpened image
                output_path = os.path.join(root, f"sharpened_{file}")
                cv2.imwrite(output_path, sharpened_image)

                print(f"Sharpened {file} with {sharpen_percentage}%: {output_path}")

    # Create a new ZIP file with the sharpened images
    new_zip_path = os.path.splitext(zip_file_path)[0] + "_sharpened.zip"
    with zipfile.ZipFile(new_zip_path, 'w') as zip_ref:
        for root, _, files in os.walk(temp_directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, temp_directory))

 

    print(f"Sharpened images saved to {new_zip_path}")





def bulrImgZip(zip_file_path, blur_percentage):
    # Create a temporary directory to extract and process the images
    temp_directory = "temp"
    os.makedirs(temp_directory, exist_ok=True)

    # Extract the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(temp_directory)

    # Iterate over extracted files
    for root, _, files in os.walk(temp_directory):
        for file in files:
            # Check if the file is an image (you can modify this condition as per your requirements)
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)

                # Load the image using OpenCV
                image = cv2.imread(image_path)

                # Blur the image
                kernel_size = int(blur_percentage/10) + 1
                blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

                # Save the blurred image
                output_path = os.path.join(root, f"blurred_{file}")
                cv2.imwrite(output_path, blurred_image)

                print(f"Blurred {file} with {blur_percentage}%: {output_path}")

    # Create a new ZIP file with the blurred images
    new_zip_path = os.path.splitext(zip_file_path)[0] + "_blurred.zip"
    with zipfile.ZipFile(new_zip_path, 'w') as zip_ref:
        for root, _, files in os.walk(temp_directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, temp_directory))

    # Remove the temporary directory
    shutil.rmtree(temp_directory)

    print(f"Blurred images saved to {new_zip_path}")

# Example usage
zip_file_path = "/path/to/images.zip"
blur_percentage = 30









zip_file_path = "/path/to/images.zip"
output_directory = "/path/to/" #Change the Path to your desired directory
sharpen_percentage = 20




#bulrImgZip(zip_file_path, blur_percentage)
#convertGrayScale(zip_file_path, output_directory)    uncomment each of these methods you are willing to use
#sharpenZipImg(zip_file_path, sharpen_percentage)
#readfromzip()




#resizeImgs("/wp-content/uploads/2019/10")


