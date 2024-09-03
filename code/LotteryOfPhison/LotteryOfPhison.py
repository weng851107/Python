import os
import random
import time
import tkinter as tk
from PIL import Image, ImageTk
import pygame

class ImagePickerApp:
    def __init__(self, root, image_folder):
        self.root = root
        w=1400  #width
        r=600  #height
        x=200  #與視窗左上x的距離
        y=300  #與視窗左上y的距離
        self.root.geometry('%dx%d+%d+%d' % (w,r,x,y))
        self.root.title("[Phison] Lottery")
        self.bg = "#FFE5B5"
        self.root.configure(bg=self.bg)  # 可以直接打顏色名稱或是找色碼表的代號(https://www.wibibi.com/info.php?tid=372)

        self.image_folder = image_folder
        self.image_list = self.get_image_list()

        self.selected_images = set()
        self.already_selected_images = set()

        self.create_widgets()
        self.reset()
        self.display_image_phison()

        #self.play_music()

    def reset(self):
        image_reset = "reset.PNG"
        for i, image_card_label in enumerate(self.image_card_labels_5):
            if i < 5:
                image = Image.open(image_reset)
                image = image.resize((220, 220))
                photo = ImageTk.PhotoImage(image)

                image_card_label.configure(image=photo)
                image_card_label.image = photo
            else:
                # If fewer than 2 images are available, clear the remaining labels
                image_card_label.configure(image=None)

    def create_widgets(self):
        self.image_card_labels_5 = []

        row_idx = 0

        self.image_phison_label = tk.Label(self.root)
        self.image_phison_label.grid(row = row_idx, column = 0, columnspan = 3)

        title_label = tk.Label(root, text="群聯大樂透", font=("Helvetica", 72), bg=self.bg)
        title_label.grid(row = row_idx, column = 3, columnspan = 3)
        row_idx = row_idx + 1

        pick_button = tk.Button(self.root, text="抽獎", font=("Helvetica", 20), command=self.pick_images_5card)
        pick_button.grid(row = row_idx, column = 0, ipady=5)
        one_label = tk.Label(root, text="第一順位", font=("Helvetica", 30), bg=self.bg)
        one_label.grid(row = row_idx, column = 1)
        two_label = tk.Label(root, text="第二順位", font=("Helvetica", 30), bg=self.bg)
        two_label.grid(row = row_idx, column = 2)
        three_label = tk.Label(root, text="第三順位", font=("Helvetica", 30), bg=self.bg)
        three_label.grid(row = row_idx, column = 3)
        four_label = tk.Label(root, text="第四順位", font=("Helvetica", 30), bg=self.bg)
        four_label.grid(row = row_idx, column = 4)
        five_label = tk.Label(root, text="第五順位", font=("Helvetica", 30), bg=self.bg)
        five_label.grid(row = row_idx, column = 5)
        row_idx = row_idx + 1

        board_label = tk.Label(root, text="Number:", font=("Helvetica", 20), bg=self.bg)
        board_label.grid(row = row_idx, column = 0)

        for i in range(5):
            image_card_label = tk.Label(self.root)
            image_card_label.grid(row = row_idx, column = i+1)
            self.image_card_labels_5.append(image_card_label)

    def display_image_phison(self):
        image_phison = "phison.PNG"

        image = Image.open(image_phison)
        image = image.resize((550, 225))
        photo = ImageTk.PhotoImage(image)

        self.image_phison_label.configure(image=photo)
        self.image_phison_label.image = photo

    def get_image_list(self):
        image_list = [f for f in os.listdir(self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        return image_list

    def pick_images_5card(self):
        # Clear previously selected images
        self.selected_images.clear()

        # Pick 5 unique random images
        while len(self.selected_images) < 5:
            if len(self.image_list) == len(self.already_selected_images):
                break
            random_image = random.choice(self.image_list)
            if random_image not in self.already_selected_images:
                self.selected_images.add(random_image)
                self.already_selected_images.add(random_image)    

        # Display selected images
        self.reset()
        self.display_images_5card()

    def display_images_5card(self):
        for i, image_card_label in enumerate(self.image_card_labels_5):
            if i < 5: #len(self.selected_images)
                image_filename = os.path.join(self.image_folder, self.selected_images.pop())
                image = Image.open(image_filename)
                image = image.resize((220, 220))
                photo = ImageTk.PhotoImage(image)

                image_card_label.configure(image=photo)
                image_card_label.image = photo
            else:
                # If fewer than 5 images are available, clear the remaining labels
                image_card_label.configure(image=None)

    def play_music(self):
        pygame.mixer.music.load(".\\disney.wav")  # 替換成你的音樂文件的路徑
        pygame.mixer.music.play()

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    image_folder_path = ".\\Figure"  # Replace with the actual path to your image folder
    root = tk.Tk()
    app = ImagePickerApp(root, image_folder_path)
    root.mainloop()
