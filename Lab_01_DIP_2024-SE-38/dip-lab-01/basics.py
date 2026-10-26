# Exercise 1: Variables and Data Types
width = 640
height = 480
image_name = "sample.png"
is_color = True

print("Width:", width, "| Type:", type(width))
print("Height:", height, "| Type:", type(height))
print("Image name:", image_name, "| Type:", type(image_name))
print("Is color:", is_color, "| Type:", type(is_color))
print("Total pixels:", width * height,"\n")


# Exercise 2: if, elif, and else
intensities = [-1, 0, 127, 128, 255, 256]

for intensity in intensities:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"

    print(f"Intensity {intensity}: {label}")


# Exercise 3: for and while loops
print("\nFor loop:")

for pixel in [20, 130, 255]:
    if pixel >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"

    print(f"{pixel}: {label}")

print("\nWhile loop:")

counter = 0
while counter < 3:
    print(counter)
    counter += 1


# Exercise 4: Functions
def is_bright(pixel, threshold=128):
    return pixel >= threshold

print("\nFunction results:")
print(is_bright(127))
print(is_bright(128))
print(is_bright(200, 210))


# Exercise 5: Lists and Tuples
pixels = [0, 128, 255]

print("\nFirst pixel:", pixels[0])

pixels[1] = 150
pixels.append(64)

print("Updated pixels:", pixels)
print("List length:", len(pixels))

size = (640, 480)
width, height = size

print("Width:", width)
print("Height:", height)

# A list is mutable, so its items can be changed.
# A tuple is immutable, so its items cannot be reassigned.


# Exercise 6: Dictionaries and Sets
image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print("\nImage width:", image["width"])
print("Image mode:", image["mode"])

labels = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels)

print("Unique labels:", unique_labels)
print("Number of unique labels:", len(unique_labels))



