from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from process import convert_to_grayscale


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

        if not self.loaded_image:
            messagebox.showwarning("Input Error", "Please load a image.")
            return

        with open(self.loaded_image, 'rb') as file:
            file.readline()
            dimensions = file.readline().decode('ascii').strip()
            width, height = map(int, dimensions.split())
            file.readline()
            pixel_data = list(file.read())


if __name__ == '__main__':
    root = Tk()
    app = ImageProcess(root)
    root.mainloop()
