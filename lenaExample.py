from scipy import misc

# loads an 8bit grayscale image of Lena (classic image processing example) into l
l = misc.lena()

# saves image of lena into a png file
misc.imsave('lena.png', l)
