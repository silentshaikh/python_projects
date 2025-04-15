from image import Image
import numpy as np
    # newImg.array = image.array * factor


# image: An instance of the Image class (like the one you created with im = Image(filename='lake.png'))
# factor: A number (e.g., 1.5 to make the image 50% brighter or 0.5 to make it darker
def adjust_brightness(image,factor):

    # image.array is a 3D NumPy array of shape (xPixels, yPixels, numChannels)
    # xPixels: Height (number of rows)
    # yPixels: Width (number of columns)
    # numChannels: Color channels (usually 3 for RGB)
    xPixels,yPixels,numChannels = image.array.shape

    # This is where the adjusted (brightened/darkened) image will be stored.
    # A new Image object is created with the same dimensions and number of channels, initialized with zeros (black).
    newImg = Image(xPixels,yPixels,numChannels)

    # Outer loop: goes through each row (x)
    # Middle loop: goes through each column (y)
    # Inner loop: goes through each color channel (c) → Red, Green, Blue
    for x in range(xPixels):
        for y in range(yPixels):
            for c in range(numChannels):

                # Multiplies each color value by the brightness factor.
                # If factor > 1, it makes it brighter
                # If factor < 1, it makes it darker
                # The result is stored in the corresponding pixel of newImg
                newImg.array[x,y,c] = image.array[x,y,c] * factor

    # Returns the new Image object with brightness adjusted
    return newImg
    # -------------------------------------------------------------------------------------------------------


# image: An instance of your Image class.
# factor: How much to increase or decrease the contrast.
# > 1: increases contrast.
# < 1: reduces contrast.
# mid: Midpoint for contrast stretching, default is 0.5 (for normalized pixel values between 0 and 1).
def adjustContrast(image,factor,mid=0.5):
     
    #  From the 3D numpy array image.array:
    # xPixels: height (rows)
    # yPixels: width (columns)
    # numChannels: number of color channels (typically 3 for RGB)
     xPixels,yPixels,numChannels = image.array.shape

    #  Initializes a blank image with the same dimensions as the original.
    #  All pixel values are initially set to 0 (black).
     newImg = Image(xPixels,yPixels,numChannels)


    # Iterates over:
    # every row x
    # every column y
    # every color channel c (Red, Green, Blue)
     for x in range(xPixels):
        for y in range(yPixels):
            for c in range(numChannels):

                # image.array[x, y, c]: the original pixel value (between 0 and 1)
                # mid: the midpoint (usually 0.5)
                # What it does:
                # Shifts the pixel away from the midpoint (pixel - mid)
                # Scales the difference using factor (spreads or squeezes the contrast)
                # Shifts it back by adding mid
                newImg.array[x,y,c] = (image.array[x,y,c]-mid) * factor + mid

    # Returns the newImg object with contrast adjusted.
     return newImg
#  --------------------------------------------------------------------------------------------------------------


# image: Your input image (an Image object with a .array property).
# kernel_size: Size of the square filter used for blurring (e.g., 3 means a 3x3 grid).
def blur(image,kernel_size):

    # Extracts height, width, and number of channels (e.g. 3 for RGB) from the image’s array.
    xPixels,yPixels,numChannels = image.array.shape

    # Will store the blurred version of the image.
    newImg = Image(xPixels,yPixels,numChannels)

    # For a 3x3 kernel → neighbourRange = 1
    # For a 5x5 kernel → neighbourRange = 2
    # This tells us how many pixels to look around the center pixel in all directions.
    neighbourRange = kernel_size // 2

    # Go through each position (x, y) and each color channel c (R, G, B).
    for x in range(xPixels):
        for y in range(yPixels):
            for c in range(numChannels):
                # Will hold the sum of all neighboring pixel values for averaging.
                total = 0

                # Loops over a square window centered around (x, y).
                # max(0, ...) ensures we don’t go outside the image boundary on the left/top.
                # min(..., xPixels - 1) ensures we don’t go beyond the right/bottom edge.
                # So this gets all pixels within the kernel range around the current pixel, safely.
                for x_i in range(max(0,x-neighbourRange),min(xPixels-1,x+neighbourRange)+1):
                    for y_i in range(max(0,y-neighbourRange),min(yPixels-1,y+neighbourRange)+1):
                        # Adds the value of each neighboring pixel (in the current channel c) to total.
                        total += image.array[x_i,y_i,c]
                
                # Takes the average of the neighboring pixels (including the current pixel).
                # kernel_size ** 2 is the total number of pixels in the kernel (e.g., 3x3 = 9).
                # This average becomes the new value for pixel (x, y) in the output image.
                newImg.array[x,y,c] = total / (kernel_size**2)

    # The function returns the blurred version of the original image.
    return newImg

# ------------------------------------------------------------------------------------------------------    


# Takes in an image (custom Image object with .array).
# Takes a kernel (usually a small 2D NumPy array like 3x3 or 5x5).
def applyKernel(image,kernel):

    # Extracts image dimensions:
    # xPixels = height
    # yPixels = width
    # numChannels = color channels (e.g. 3 for RGB)
    xPixels,yPixels,numChannels = image.array.shape

    #  Creates a new empty image to store the filtered output.
    newImg = Image(xPixels,yPixels,numChannels)

    # Gets the size of the kernel (assuming it's square, like 3x3 or 5x5).
    # For a 3x3 kernel → kernel_size = 3
    kernel_size = kernel.shape[0]

    #  Determines how many pixels around the center to consider:
    # For 3x3 → neighbourRange = 1
    # For 5x5 → neighbourRange = 2
    neighbourRange = kernel_size // 2

    # Loops through each pixel and each color channel (R, G, B).
    for x in range(xPixels):
        for y in range(yPixels):
            for c in range(numChannels):

                #  Prepares to sum all the weighted neighboring pixel values.
                total = 0

                #  Loops over each neighboring pixel within the kernel size:
                # Clipped to stay within the image boundaries.
                for x_i in range(max(0,x-neighbourRange),min(xPixels-1,x+neighbourRange)+1):
                    for y_i in range(max(0,y-neighbourRange),min(yPixels-1,y+neighbourRange)+1):

                        # Calculates the corresponding position in the kernel:
                        # This maps the pixel position (x_i, y_i) to the kernel position (x_k, y_k).
                        # This is necessary because:
                        # The kernel is centered at (x, y) in the image.
                        # Kernel coordinates go from 0 → kernel_size-1.
                        x_k = x_i + neighbourRange - x
                        y_k = y_i + neighbourRange -y

                        #  Fetches the kernel value at that position
                        kernel_val = kernel[x_k,y_k]

                        #  Applies the kernel:
                        #  Multiply image pixel by kernel value, and accumulate it into total.
                        total += image.array[x_i,y_i,c] * kernel_val
                
                # After going through all neighbors:
                # Sets the pixel value in the new image to the total (filtered result).
                newImg.array[x,y,c] = total

    # Returns the final filtered image
    return newImg
# ------------------------------------------------------------------------------------------------------


# this defines a function named combine_img that:
# Takes in two image objects, imgOne and imgTwo.
# Both images are expected to have the same size and number of color channels.
def combine_img(imgOne,imgTwo):

    # Extracts the image dimensions from imgOne:
    # xPixels: Height of the image.
    # yPixels: Width of the image.
    # numChannels: Number of color channels (e.g., 3 for RGB).
    # imgTwo is assumed to have the same shape as imgOne
    xPixels,yPixels,numChannels = imgOne.array.shape

    # Creates a new blank image object with the same dimensions, to store the combined result.
    newImg = Image(xPixels,yPixels,numChannels)

    # Loops through every pixel (x, y) and every color channel (c):
    # So it covers the entire image, channel by channel.
    for x in range(xPixels):
        for y in range(yPixels):
            for c in range(numChannels):

                # The core operation:
                # This line calculates the Euclidean distance (or magnitude) at each pixel position and channel, using this formula:

                # √(a² + b²)                
                # Where:
                # a = imgOne.array[x, y, c]
                # b = imgTwo.array[x, y, c]
                # This is often used to combine gradients from two directions (like Sobel X and Sobel Y) into one intensity map.
                # Example use case:
                # imgOne = horizontal edges
                # imgTwo = vertical edges
                # Result = overall edge strength
                newImg.array[x,y,c] = (imgOne.array[x,y,c]**2 + imgTwo.array[x,y,c]**2)**0.5

    # Finally, the new combined image is returned.
    return newImg







if __name__ == "__main__":
    lake  = Image(filename="lake.png")
    city = Image(filename="city.png")

    # brightened_img = adjust_brightness(lake,2.8)
    # brightened_img.write_image("brightned.png")

    # imgContrast = adjustContrast(lake,2,0.5)
    # imgContrast.write_image("inc_contrast.png")

    # imgBlur = blur(city,5)
    # imgBlur.write_image("blur_3.png")
    sobel_x_kernel = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    sobel_y_kernel = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    
    imgKernelX = applyKernel(city,sobel_x_kernel)
    # imgKernelX.write_image("kernel_x.png")

    imgKernelY = applyKernel(city,sobel_y_kernel)
    # imgKernelY.write_image("kernel_y.png")
    
    imgCombine = combine_img(imgKernelX,imgKernelY)
    imgCombine.write_image("combine_img.png")