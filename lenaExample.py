from scipy import misc
import matplotlib.pyplot as plt

# loads an 8bit grayscale image of Lena (classic image processing example) into l
l = misc.lena()

# saves image of lena into a png file
misc.imsave('lena.png', l)

# displays the image of lena
plt.imshow(l)
plt.show()

# creates numpy array from an image file
lena = misc.imread('lena.png')
