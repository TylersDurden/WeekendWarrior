from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from skimage import data
from math import sqrt
import sys

if 'ex' in sys.argv:
    image = data.hubble_deep_field()[0:500, 0:500]
elif len(sys.argv) > 1:
    image = plt.imread(sys.argv[1])
image_gray = rgb2gray(image)
# Laplacian of Gaussian
blobs_log = blob_log(image_gray, max_sigma=30, num_sigma=10, threshold=.1)
# Compute radii in the 3rd column
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
# Diff of Gaussian
blobs_dog = blob_dog(image_gray, max_sigma=30, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
# Diff of Hessian
blobs_doh = blob_doh(image_gray, max_sigma=30, threshold=.01)
# Organize Blob types
blobs_list = [blobs_log, blobs_dog, blobs_doh]
colors = ['yellow', 'lime', 'red']
titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
          'Determinant of Hessian']
sequence = zip(blobs_list, colors, titles)

''' Create Figure '''
fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()
for idx, (blobs, color, title) in enumerate(sequence):
    ax[idx].set_title(title)
    ax[idx].imshow(image, interpolation='nearest')
    print title + ': '+str(len(blobs))
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        ax[idx].add_patch(c)
    ax[idx].set_axis_off()
plt.tight_layout()
plt.show()
