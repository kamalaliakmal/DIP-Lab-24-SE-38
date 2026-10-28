import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# STEP 2: Load the image
image = cv.imread("Day 7 task.png")

if image is None:
    raise FileNotFoundError(
        "Image not found. Put your image in this folder and check its filename."
    )

print("\n--- STEP 2: IMAGE LOADING ---")
print("Image Shape (height, width, channels):", image.shape)
print("Image Data Type:", image.dtype)

# STEP 3: Inspect the image
height, width, channels = image.shape

print("\n--- STEP 3: IMAGE INSPECTION ---")
print("Height:", height)
print("Width:", width)
print("Number of Channels:", channels)
print("Top-left Pixel (BGR):", image[0, 0])

center_y = height // 2
center_x = width // 2
print("Center Pixel (BGR):", image[center_y, center_x])
print("Global Minimum:", image.min())
print("Global Maximum:", image.max())
print("Blue Channel Min/Max:",
      image[:, :, 0].min(), image[:, :, 0].max())
print("Green Channel Min/Max:",
      image[:, :, 1].min(), image[:, :, 1].max())
print("Red Channel Min/Max:",
      image[:, :, 2].min(), image[:, :, 2].max())

# STEP 4: Convert colors and separate channels
rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

red = rgb[:, :, 0]
green = rgb[:, :, 1]
blue = rgb[:, :, 2]

print("\n--- STEP 4: COLOR ANALYSIS ---")
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes[0, 0].imshow(rgb)
axes[0, 0].set_title("RGB Image")
axes[0, 1].imshow(red, cmap="gray")
axes[0, 1].set_title("Red Channel")
axes[0, 2].imshow(green, cmap="gray")
axes[0, 2].set_title("Green Channel")
axes[1, 0].imshow(blue, cmap="gray")
axes[1, 0].set_title("Blue Channel")
axes[1, 1].imshow(gray, cmap="gray")
axes[1, 1].set_title("Grayscale Image")
axes[1, 2].imshow(image)
axes[1, 2].set_title("Unconverted BGR Display")

for ax in axes.flat:
    ax.axis("off")
plt.tight_layout()
plt.show()

center_rgb = rgb[center_y, center_x]
hex_color = "#{:02X}{:02X}{:02X}".format(
    int(center_rgb[0]), int(center_rgb[1]), int(center_rgb[2])
)
print("Center Pixel RGB:", center_rgb)
print("Center Pixel HEX:", hex_color)

# STEP 5: Crop, resize, and save
print("\n--- STEP 5: CROP, RESIZE, AND SAVE ---")
# The assignment requires an image of at least 300 x 300 pixels.
y_start, x_start = 50, 50
crop = image[y_start:y_start + 100, x_start:x_start + 100]
print("Crop Shape:", crop.shape)

if crop.shape[:2] != (100, 100):
    raise ValueError("Crop is not 100 x 100. Check the input image dimensions.")

resized = cv.resize(crop, (200, 200))
print("Resized Image Shape:", resized.shape)

crop_rgb = cv.cvtColor(crop, cv.COLOR_BGR2RGB)
resized_rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(rgb)
axes[0].set_title("Original Image")
axes[1].imshow(crop_rgb)
axes[1].set_title("100 x 100 Crop")
axes[2].imshow(resized_rgb)
axes[2].set_title("200 x 200 Resized Crop")
for ax in axes:
    ax.axis("off")
plt.tight_layout()
plt.show()

resized_bgr = cv.cvtColor(resized_rgb, cv.COLOR_RGB2BGR)
saved = cv.imwrite("resized_crop.png", resized_bgr)
print("Was resized_crop.png saved successfully?", saved)

# STEP 6: Create a grayscale histogram
print("\n--- STEP 6: GRAYSCALE HISTOGRAM ---")
gray_flat = gray.ravel()
plt.figure(figsize=(8, 5))
plt.hist(gray_flat, bins=256, range=(0, 256))
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Intensity (0 = Black, 255 = White)")
plt.ylabel("Number of Pixels")
plt.tight_layout()
plt.savefig("grayscale_histogram.png")
plt.show()
print("Histogram saved as grayscale_histogram.png")
print("Report note: Inspect the histogram and explain whether the image")
print("is mainly dark, mainly bright, or has a broad/balanced distribution.")

# STEP 7: Demonstrate bit depth
print("\n--- STEP 7: BIT DEPTH ---")
gradient = np.arange(256, dtype=np.uint8).reshape(1, 256)

def quantize(image_array, bits):
    levels = 2 ** bits
    scaled = np.round(
        image_array.astype(np.float32) / 255 * (levels - 1)
    ) * (255 / (levels - 1))
    return scaled.astype(np.uint8)

gradient_1bit = quantize(gradient, 1)
gradient_2bit = quantize(gradient, 2)
gradient_4bit = quantize(gradient, 4)

fig, axes = plt.subplots(4, 1, figsize=(10, 5))
gradients = [
    (gradient, "Original 8-bit Gradient"),
    (gradient_1bit, "1-bit Gradient"),
    (gradient_2bit, "2-bit Gradient"),
    (gradient_4bit, "4-bit Gradient"),
]
for ax, (grad, title) in zip(axes, gradients):
    ax.imshow(grad, cmap="gray", vmin=0, vmax=255, aspect="auto")
    ax.set_title(title)
    ax.axis("off")
plt.tight_layout()
plt.show()

print("8-bit Unique Values:", len(np.unique(gradient)))
print("1-bit Unique Values:", len(np.unique(gradient_1bit)))
print("2-bit Unique Values:", len(np.unique(gradient_2bit)))
print("4-bit Unique Values:", len(np.unique(gradient_4bit)))

print("\n--- TASK COMPLETE ---")
print("Check that resized_crop.png and grayscale_histogram.png exist.")
print("Remember to capture screenshots and write your own report explanations.")
