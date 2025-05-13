from rembg import remove
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import filedialog

# Function to browse and select a file
def browse_file():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]
    )
    return file_path

# Select the input image
print("Please select an input image:")
input_path = browse_file()
if not input_path:
    print("No file selected. Exiting...")
    exit()

# Select where to save the output image
print("Please select a location to save the output image:")
output_path = filedialog.asksaveasfilename(
    title="Save Output Image",
    defaultextension=".png",
    filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")]
)
if not output_path:
    print("No output file specified. Exiting...")
    exit()

try:
    # Open the input image
    with open(input_path, "rb") as input_file:
        input_data = input_file.read() 

    # Remove the background
    output_data = remove(input_data)  

    # Save the output image
    output_image = Image.open(BytesIO(output_data))  
    output_image.save(output_path)  

    print(f"Image saved successfully at {output_path}")
except FileNotFoundError:
    print("Error: The specified input file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
