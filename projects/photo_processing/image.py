
# This imports the NumPy library, a powerful library for numerical operations in Python. Creating and working with arrays (like images, which are grids of pixels).Handling image data as 3D arrays (height x width x channels).
import numpy as np

# This imports the PyPNG library.
# It allows reading and writing PNG image files
import png

class Image:

    # This is the constructor method Image class

    # x_pixels: width of the image.
    # y_pixels: height of the image.
    # num_channels: number of color channels (e.g., 3 for RGB).
    # filename: optional – if you want to load an image instead of creating a blank one.
    def __init__(self, x_pixels=0, y_pixels=0, num_channels=0, filename=''):
        # you need to input either filename OR x_pixels, y_pixels, and num_channels

        # Sets a default folder path for reading images.
        self.input_path = 'input/'

        # Sets a default folder path for saving output images.
        self.output_path = 'output/'

        # This checks whether all three dimensions were provided.
        # If they are (non-zero), the user wants to create a blank image from scratch.
        if x_pixels and y_pixels and num_channels:

            # These just save the passed values as properties of the object (like width, height, and RGB channels).
            self.x_pixels = x_pixels
            self.y_pixels = y_pixels
            self.num_channels = num_channels

            # This creates a blank image array using NumPy.

            # All pixel values are initialized to 0 (black).
            # Shape of the array is (x_pixels, y_pixels, num_channels) → so a 3D array.
            # For example, (100, 100, 3) = 100×100 RGB image.
            self.array = np.zeros((x_pixels, y_pixels, num_channels))

         # This checks if a filename was passed instead of pixel dimensions.
            # So now it will load an image from disk instead of creating a new blank one.
        elif filename:

            #Calls the read_image() method to load the image data.
            # ?Stores it as a NumPy array in self.array.
            self.array = self.read_image(filename)

            # Gets the dimensions of the loaded image from the array.

            # For example, if the image is (512, 512, 3), it'll set:
            # x_pixels = 512
            # y_pixels = 512
            # num_channels = 3
            self.x_pixels, self.y_pixels, self.num_channels = self.array.shape

        # If neither the pixel values nor a filename were provided, this runs.
        else:
            # This raises an error with a custom message, telling the user they must provide either dimensions or a filename.
            raise ValueError("You need to input either a filename OR specify the dimensions of the image")



    # This is a method of a class.
    # It reads a PNG image file.
    # It also applies gamma correction (default is 2.2, which is typical for screens)
    def read_image(self, filename, gamma=2.2):

        # This uses the pypng library to read the PNG file.
        # self.input_path + filename builds the full path (e.g., 'input/lake.png').
        # .asFloat() loads the image as float values between 0.0 and 1.0.
        # im is a tuple that contains image data and metadata: -> im = (width, height, rows, info)
        im = png.Reader(self.input_path + filename).asFloat()

        # im[2] contains the image rows.
        # list(im[2]) converts them into a list of rows (each row is a 1D array).
        # np.vstack(...) stacks these rows vertically to make a 2D array.
        # Result: a 2D NumPy array where each row contains pixel data.
        resized_image = np.vstack(list(im[2]))

        # Resizes the flat 2D image into a proper 3D array:
        # im[1] = image height → rows
        # im[0] = image width → columns
        # 3 = RGB channels
        # The shape becomes (height, width, 3) → just like a normal color image.
        resized_image.resize(im[1], im[0], 3)

        # Applies gamma correction.
        # It raises each pixel value to the power of gamma (2.2 by default).
        # Why? Because human eyes and screens don't perceive brightness linearly. This corrects it.
        # If the image was encoded with gamma, we decode it here.
        resized_image = resized_image ** gamma

        # Finally, it returns the gamma-decoded 3D NumPy image.
        # You can now work with this image in Python (edit, process, etc.).
        return resized_image

  # ------------------------------------------------------------------------------------------------------

    # This defines a method that saves your image (self.array) to a PNG file.
    # The file will be saved with gamma encoding.
    # Default gamma is 2.2.
    def write_image(self, output_file_name, gamma=2.2):
        '''
        3D numpy array (Y, X, channel) of values between 0 and 1 -> write to png
        '''

        # This clips all pixel values so they stay within the valid range [0, 1].
        # If any value is below 0 or above 1, it's forced back into that range.
        # Important for PNG format which expects valid pixel values.
        im = np.clip(self.array, 0, 1)

        # Gets the image dimensions:
        # y: height (number of rows)
        # x: width (number of columns)
        y, x = self.array.shape[0], self.array.shape[1]

        # Reshapes the image from (height, width, 3) → to a 2D shape (height, width × 3).
        # Why? Because pypng expects each row to be a flat array of pixel values:
        im = im.reshape(y, x*3)

        # Creates a PNG writer object with the original image width and height.
        writer = png.Writer(x, y)

        # Opens the output file (in output/) in binary write mode ('wb').
        # Ensures the image is saved properly as a PNG.
        with open(self.output_path + output_file_name, 'wb') as f:

            # Gamma encoding is applied: each pixel is raised to the power of 1/gamma (inverse of decoding).
        # Multiplied by 255 to convert from float [0, 1] → to 8-bit PNG [0, 255].
        # Then the result is written to the file using the writer.
            writer.write(f, 255*(im**(1/gamma)))

        # After writing, the image array is reshaped back to its original form (height, width, 3).
        # This ensures the in-memory array (self.array) is restored to RGB image format.
        self.array.resize(y, x, 3)  # we mutated the method in the first step of the function
        

if __name__ == '__main__':

    # creating an object of the Image class.
    	# Reads the input image as a NumPy array
    im = Image(filename='lake.png')

    	# Writes the processed image to a new PNG file
    im.write_image('test.png')