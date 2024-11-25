from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from process import convert_to_grayscale, show_images, save_pgm_image, binarize_image

class ImageProcess:
    def __init__(self, root):
        self.root = root
        self.root.title('BairesDev Image Process')
        self.root.config(padx=50, pady=50)
        self.root.eval('tk::PlaceWindow . center')
        self.loaded_image = None

        load_button = Button(root, text='Load Image', command=self.open_image)
        load_button.pack()

        process_button = Button(root, text='Process Image', command=self.generate_image)
        process_button.pack()

        self.image_label = Label(root)
        self.image_label.pack()

    def open_image(self):
        """Load the image"""
        file_path = filedialog.askopenfilename(
            title='Open Image',
            filetypes=[("PPM Image Files", "*.ppm")]
        )

        if file_path:
            self.loaded_image = file_path

            img = Image.open(file_path)
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk

    def generate_image(self):
        """Convert image to grayscale and binary color."""
        if not self.loaded_image:
            messagebox.showwarning("Input Error", "Please load an image.")
            return

        with open(self.loaded_image, 'rb') as file:
            file.readline()  # Skip the magic number
            dimensions = file.readline().decode('ascii').strip()
            while dimensions.startswith('#'):
                dimensions = file.readline().decode('ascii').strip()
            width, height = map(int, dimensions.split())
            file.readline()  # Skip the max color value
            pixel_data = list(file.read())

        grayscale_data = convert_to_grayscale(width, height, pixel_data)
        grayscale_path = 'grayscale.pgm'
        save_pgm_image(grayscale_path, width, height, grayscale_data)

        binary_data = binarize_image(grayscale_data)
        binary_path = 'binary.pgm'
        save_pgm_image(binary_path, width, height, binary_data)

        show_images(self.loaded_image, grayscale_path, binary_path)

if __name__ == '__main__':
    root = Tk()
    app = ImageProcess(root)
    root.mainloop()
