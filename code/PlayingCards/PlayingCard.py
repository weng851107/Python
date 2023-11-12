import os
import random
import tkinter as tk
from PIL import Image, ImageTk

class ImagePickerApp:
    def __init__(self, root, image_folder):
        self.root = root
        w=1440  #width
        r=480  #height
        x=200  #與視窗左上x的距離
        y=300  #與視窗左上y的距離
        self.root.geometry('%dx%d+%d+%d' % (w,r,x,y))
        self.root.title("[Phison] Random Playing Cards Picker")

        self.image_folder = image_folder
        self.image_list = self.get_image_list()

        self.selected_images = set()

        self.create_widgets()

    def create_widgets(self):
        self.image_labels = []

        for _ in range(5):
            image_label = tk.Label(self.root)
            image_label.pack(side=tk.LEFT, padx=5)
            self.image_labels.append(image_label)

        pick_button = tk.Button(self.root, text="Pick Images", command=self.pick_images)
        pick_button.pack(padx=10, pady=10, ipady=10)

    def get_image_list(self):
        image_list = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        return image_list

    def pick_images(self):
        # Clear previously selected images
        self.selected_images.clear()

        # Pick 5 unique random images
        while len(self.selected_images) < 10:
            random_image = random.choice(self.image_list)
            self.selected_images.add(random_image)

        # Display selected images
        self.display_images()

    def display_images(self):
        for i, image_label in enumerate(self.image_labels):
            if i < len(self.selected_images):
                image_filename = os.path.join(self.image_folder, self.selected_images.pop())
                image = Image.open(image_filename)
                image = image.resize((250, 250))
                photo = ImageTk.PhotoImage(image)

                image_label.configure(image=photo)
                image_label.image = photo
            else:
                # If fewer than 5 images are available, clear the remaining labels
                image_label.configure(image=None)

if __name__ == "__main__":
    image_folder_path = ".\\Figure"  # Replace with the actual path to your image folder
    root = tk.Tk()
    app = ImagePickerApp(root, image_folder_path)
    root.mainloop()
