import os
import random
import tkinter as tk
from PIL import Image, ImageTk

class ImagePickerApp:
    def __init__(self, root, image_folder):
        self.root = root
        w=1400  #width
        r=600  #height
        x=200  #與視窗左上x的距離
        y=300  #與視窗左上y的距離
        self.root.geometry('%dx%d+%d+%d' % (w,r,x,y))
        self.root.title("[Phison] Random Playing Cards Picker")
        self.root.configure(bg="#BABABA")  # 可以直接打顏色名稱或是找色碼表的代號(https://www.wibibi.com/info.php?tid=372)

        self.image_folder = image_folder
        self.image_list = self.get_image_list()

        self.selected_images = set()
        self.selected_images_board = set()

        self.create_widgets()

    def reset(self):
        image_reset = "reset.PNG"
        for i, image_label in enumerate(self.image_labels_5):
            if i < 5:
                image = Image.open(image_reset)
                image = image.resize((250, 250))
                photo = ImageTk.PhotoImage(image)

                image_label.configure(image=photo)
                image_label.image = photo
            else:
                # If fewer than 2 images are available, clear the remaining labels
                image_label.configure(image=None)

        for i, image_label in enumerate(self.image_labels_2):
            if i < 2:
                image = Image.open(image_reset)
                image = image.resize((250, 250))
                photo = ImageTk.PhotoImage(image)

                image_label.configure(image=photo)
                image_label.image = photo
            else:
                # If fewer than 2 images are available, clear the remaining labels
                image_label.configure(image=None)

    def create_widgets(self):
        self.image_labels_5 = []
        self.image_labels_2 = []

        for i in range(5):
            image_label = tk.Label(self.root)
            image_label.grid(row = 1, column = i+1)
            self.image_labels_5.append(image_label)

        board_label = tk.Label(root, text="Board:", font=("Helvetica", 20))
        board_label.grid(row = 1, column = 0)

        for i in range(2):
            image_label = tk.Label(self.root)
            image_label.grid(row = 2, column = i+1)
            self.image_labels_2.append(image_label)

        host_label = tk.Label(root, text="Host:", font=("Helvetica", 20))
        host_label.grid(row = 2, column = 0)

        pick_button = tk.Button(self.root, text="Get Board Cards", font=("Helvetica", 12), command=self.pick_images_5)
        pick_button.grid(row = 0, column = 0, ipady=5)

        host_button = tk.Button(self.root, text="Get Host Cards", font=("Helvetica", 12), command=self.pick_images_2)
        host_button.grid(row = 0, column = 1, ipady=5)

        reset_button = tk.Button(self.root, text="Reset", font=("Helvetica", 12), command=self.reset)
        reset_button.grid(row = 0, column = 2, ipady=5)

    def get_image_list(self):
        image_list = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        return image_list

    def pick_images_5(self):
        # Clear previously selected images
        self.selected_images.clear()
        self.selected_images_board.clear()

        # Pick 5 unique random images
        while len(self.selected_images) < 5:
            random_image = random.choice(self.image_list)
            self.selected_images.add(random_image)
            self.selected_images_board.add(random_image)

        # Display selected images
        self.display_images_5()

    def pick_images_2(self):
        # Clear previously selected images
        self.selected_images.clear()

        # Pick 2 unique random images
        while len(self.selected_images) < 2:
            random_image = random.choice(self.image_list)
            if random_image not in self.selected_images_board:
                self.selected_images.add(random_image)

        # Display selected images
        self.display_images_2()

    def display_images_5(self):
        for i, image_label in enumerate(self.image_labels_5):
            if i < 5: #len(self.selected_images)
                image_filename = os.path.join(self.image_folder, self.selected_images.pop())
                image = Image.open(image_filename)
                image = image.resize((250, 250))
                photo = ImageTk.PhotoImage(image)

                image_label.configure(image=photo)
                image_label.image = photo
            else:
                # If fewer than 5 images are available, clear the remaining labels
                image_label.configure(image=None)

    def display_images_2(self):
        for i, image_label in enumerate(self.image_labels_2):
            if i < 2:
                image_filename = os.path.join(self.image_folder, self.selected_images.pop())
                image = Image.open(image_filename)
                image = image.resize((250, 250))
                photo = ImageTk.PhotoImage(image)

                image_label.configure(image=photo)
                image_label.image = photo
            else:
                # If fewer than 2 images are available, clear the remaining labels
                image_label.configure(image=None)

if __name__ == "__main__":
    image_folder_path = ".\\Figure"  # Replace with the actual path to your image folder
    root = tk.Tk()
    app = ImagePickerApp(root, image_folder_path)
    root.mainloop()
