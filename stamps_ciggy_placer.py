from PIL import Image

def shear_image(image_path, output_path, y_angle, expand_factor, final_width, final_height, target_location):
    # Open the input image
    input_image = Image.open(image_path)
    # Calculate the desired width based on the aspect ratio
    desired_width = int(input_image.height * 0.9643)
    # Resize the image to the desired aspect ratio
    input_image = input_image.resize((desired_width, input_image.height))
    # Resize the input image to final size
    input_image = input_image.resize((final_width, final_height))

    # Calculate the shear factor
    shear_factor_y = y_angle * 0.0174533  # Convert angle to radians
    shear_factor_x = x_angle * 0.0174533  # I'm bad at math what's a radian?
    # Calculate the maximum displacement caused by the shearing transformation
    max_displacement = abs(shear_factor_y) * input_image.height
    # Calculate the amount of expansion needed to accommodate the maximum displacement
    expand_pixels = int(max_displacement + input_image.height * expand_factor)
    #set variables
    working_height = final_height
    working_width = final_width
    # Calculate the new size for the transparent layer
    working_width += expand_pixels
    working_height += expand_pixels
    # Create a new transparent image with the expanded size
    output_image = Image.new("RGBA", (working_width, working_height), (0, 0, 0, 0))

    # Calculate the offset for pasting the input image onto the transparent image
    paste_offset = (expand_pixels, expand_pixels)
    # Paste the input image onto the transparent image
    output_image.paste(input_image, paste_offset)

    # Define the shearing matrix
    shear_matrix = (1, shear_factor_x, 0, shear_factor_y, 1, 0)
    # Apply the shearing transformation
    output_image = output_image.transform((working_width, working_height), Image.AFFINE, shear_matrix, resample=Image.BICUBIC)
    # Find the non-transparent bounding box of the sheared image
    bbox = output_image.getbbox()
    # Crop the image to the non-transparent bounding box
    output_image = output_image.crop(bbox)
    # Get the new width and height after cropping
    working_width, working_height = output_image.size
    # Resize the image
    output_image = output_image.resize((working_width, working_height))

    # Open the render image
    render_image = Image.open("render.png")
    # Perform a final resize of the image
    output_image = output_image.resize((final_width, final_height))
    # Paste the sheared and resized image onto the render image at the target location
    render_image.paste(output_image, target_location, output_image)
    # Save the output image
    render_image.save(output_path)

# Set the angles for shearing
y_angle = 10  
x_angle = 0.5

# Ask user for the image name
image_name = input("Please enter the image name: ")

# Specify the input and output file paths
input_path = image_name + ".png"
output_path = "output.png"

# Specify the expansion factor (adjust as needed)
expand_factor = 1  # Adjust the value to control the amount of expansion

# Set the final width and height before pasting the sheared image onto the render image
final_width = 675
final_height = 700

# Specify the target location to overlay the image
target_location = (585, 740)  # Adjust the coordinates as per your requirement

# Call the shear_image function
shear_image(input_path, output_path, y_angle, expand_factor, final_width, final_height, target_location)

print("\n\n\n\n\n\n\n\n                                                 ~~\n                                                  ~~\n                                                 ~~\n                                                 ~~\n                                                  ~~\n                                                  ~~\n                                                 ~~\n                                                 ~~\n____________________________________________      ~~\n|        |    cigbot    loves    you        |||||||\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n\n\n\n")
