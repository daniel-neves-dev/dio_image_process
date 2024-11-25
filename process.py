import matplotlib.pyplot as plt
import numpy as np

def convert_to_grayscale(width, height, pixel_data):
    """Convert RGB image data to grayscale."""
    grayscale_data = []
    for i in range(0, len(pixel_data), 3):
        r, g, b = pixel_data[i], pixel_data[i + 1], pixel_data[i + 2]
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)
        grayscale_data.append(gray)
    return grayscale_data

def binarize_image(grayscale_data, threshold=128):
    """Binarize grayscale image data."""
    return [255 if pixel > threshold else 0 for pixel in grayscale_data]

def save_pgm_image(filepath, width, height, data):
    """Save a grayscale or binary image in PGM (P5) format."""
    with open(filepath, 'wb') as f:
        f.write(f'P5\n{width} {height}\n255\n'.encode('ascii'))
        f.write(bytearray(data))

def show_images(original_file, grayscale_file, binary_file):
    """Show images side by side"""
    with open(original_file, 'rb') as file:
        file.readline()
        dimensions = file.readline().decode('ascii').strip()
        while dimensions.startswith('#'):
            dimensions = file.readline().decode('ascii').strip()
        width, height = map(int, dimensions.split())
        file.readline()
        original_data = file.read()

    # Read the grayscale image (PGM format)
    with open(grayscale_file, 'rb') as file:
        file.readline()
        dimensions = file.readline().decode('ascii').strip()
        while dimensions.startswith('#'):
            dimensions = file.readline().decode('ascii').strip()
        width_g, height_g = map(int, dimensions.split())
        file.readline()
        grayscale_data = file.read()

    with open(binary_file, 'rb') as file:
        file.readline()
        dimensions = file.readline().decode('ascii').strip()
        while dimensions.startswith('#'):
            dimensions = file.readline().decode('ascii').strip()
        width_g, height_g = map(int, dimensions.split())
        file.readline()
        binary_data = file.read()

    original = np.frombuffer(original_data, dtype=np.uint8).reshape((height, width, 3))
    grayscale = np.frombuffer(grayscale_data, dtype=np.uint8).reshape((height_g, width_g))
    binary = np.frombuffer(binary_data, dtype=np.uint8).reshape((height_g, width_g))

    # Plot the images side by side
    plt.figure(figsize=(12, 4))

    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    # Grayscale image
    plt.subplot(1, 3, 2)
    plt.imshow(grayscale, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    # Binary image
    plt.subplot(1, 3, 3)
    plt.imshow(binary, cmap="gray")
    plt.title("Binary Image")
    plt.axis("off")

    # Show the images
    plt.tight_layout()
    plt.show()


