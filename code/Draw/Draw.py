import os
import random
import time
import tkinter as tk
from PIL import Image, ImageTk
import pygame

WA_G0_OneTime = True
WA_G1_OneTime = True
WA_G2_OneTime = True
WA_G3_OneTime = True
WA_G4_OneTime = True
WA_G5_OneTime = True
WA_G6_OneTime = True

Figure_Size = 450

filenameA = "RedTeam.log"
filenameB = "BlueTeam.log"

class ImagePickerApp:
    def __init__(self, root, image_folder_Boss, image_folder_G0, image_folder_G1, image_folder_G2, image_folder_G3, image_folder_G4, image_folder_G5, image_folder_G6, image_folder_Common):
        self.root = root
        w=1450  #width
        r=750  #height
        x=80  #與視窗左上x的距離
        y=120  #與視窗左上y的距離
        self.root.geometry('%dx%d+%d+%d' % (w,r,x,y))
        self.root.title("[Phison] Draw")
        self.bg = "#FFE5B5"
        self.root.configure(bg=self.bg)  # 可以直接打顏色名稱或是找色碼表的代號(https://www.wibibi.com/info.php?tid=372)

        # self.image_folder_Boss = image_folder_Boss
        self.image_folder_G0 = image_folder_G0
        self.image_folder_G1 = image_folder_G1
        self.image_folder_G2 = image_folder_G2
        self.image_folder_G3 = image_folder_G3
        self.image_folder_G4 = image_folder_G4
        self.image_folder_G5 = image_folder_G5
        self.image_folder_G6 = image_folder_G6
        self.image_folder_Common = image_folder_Common
        # self.image_list_Boss = self.get_image_list(image_folder_Boss)
        self.image_list_G0 = self.get_image_list(image_folder_G0)
        self.image_list_G1 = self.get_image_list(image_folder_G1)
        self.image_list_G2 = self.get_image_list(image_folder_G2)
        self.image_list_G3 = self.get_image_list(image_folder_G3)
        self.image_list_G4 = self.get_image_list(image_folder_G4)
        self.image_list_G5 = self.get_image_list(image_folder_G5)
        self.image_list_G6 = self.get_image_list(image_folder_G6)
        self.image_list_Common = self.get_image_list(image_folder_Common)

        # self.selected_images_Boss = set()
        self.selected_G_Idx = 0
        self.selected_images_G = set()
        self.selected_images_G0 = set()
        self.selected_images_G1 = set()
        self.selected_images_G2 = set()
        self.selected_images_G3 = set()
        self.selected_images_G4 = set()
        self.selected_images_G5 = set()
        self.selected_images_G6 = set()
        self.selected_images_Common = set()
        # self.already_selected_images_Boss = set()
        self.already_selected_images_G0 = set()
        self.already_selected_images_G1 = set()
        self.already_selected_images_G2 = set()
        self.already_selected_images_G3 = set()
        self.already_selected_images_G4 = set()
        self.already_selected_images_G5 = set()
        self.already_selected_images_G6 = set()
        self.already_selected_images_Common = set()

        ## print info
        # self.print_image_list(self.image_list_Boss)

        self.create_widgets()
        self.reset()
        self.display_image_phison()

        self.play_music()

    def reset(self):
        image_reset = "reset.PNG"
        # for i, image_card_label in enumerate(self.image_card_labels_2_Boss):
        #     if i < 2:
        #         image = Image.open(image_reset)
        #         image = image.resize((Figure_Size, Figure_Size))
        #         photo = ImageTk.PhotoImage(image)

        #         image_card_label.configure(image=photo)
        #         image_card_label.image = photo
        #     else:
        #         # If fewer than 2 images are available, clear the remaining labels
        #         image_card_label.configure(image=None)
        for i, image_card_label in enumerate(self.image_card_labels_2):
            if i < 2:
                image = Image.open(image_reset)
                image = image.resize((Figure_Size, Figure_Size))
                photo = ImageTk.PhotoImage(image)

                image_card_label.configure(image=photo)
                image_card_label.image = photo
            else:
                # If fewer than 2 images are available, clear the remaining labels
                image_card_label.configure(image=None)

    def print_image_list(self, image_list):
        for i in range(len(image_list)):
            print("{} ".format(image_list[i]))

    def create_widgets(self):
        self.image_card_labels_2_Boss = []
        self.image_card_labels_2 = []

        row_idx = 0
        column_idx = 0

        self.image_phison_label = tk.Label(self.root)
        self.image_phison_label.grid(row = row_idx, column = 0, columnspan = 2)

        title_label = tk.Label(root, text="群聯選秀大會", font=("Helvetica", 72), bg=self.bg)
        title_label.grid(row = row_idx, column = 2, columnspan = 2)
        row_idx = row_idx + 1

        # pick_button_Boss = tk.Button(self.root, text="Captain", font=("Helvetica", 20), command=self.pick_images_Boss)
        # pick_button_Boss.grid(row = row_idx, column = column_idx, ipady=5)
        # column_idx = column_idx + 1
        pick_button_G = tk.Button(self.root, text="第一輪選秀", font=("Helvetica", 20), command=self.pick_images_G)
        pick_button_G.grid(row = row_idx, column = column_idx, ipady=5)
        column_idx = column_idx + 1
        pick_button_Common = tk.Button(self.root, text="第二輪選秀", font=("Helvetica", 20), command=self.pick_images_Common)
        pick_button_Common.grid(row = row_idx, column = column_idx, ipady=5)
        column_idx = column_idx + 1
        one_label = tk.Label(root, text="Red Team", font=("Helvetica", 30), bg=self.bg)
        one_label.grid(row = row_idx, column = column_idx)
        column_idx = column_idx + 1
        two_label = tk.Label(root, text="Blue Team", font=("Helvetica", 30), bg=self.bg)
        two_label.grid(row = row_idx, column = column_idx)
        row_idx = row_idx + 1

        # board_label_Boss = tk.Label(root, text="Captain:", font=("Helvetica", 20), bg=self.bg)
        # board_label_Boss.grid(row = row_idx, column = column_idx-2)

        # for i in range(2):
        #     image_card_label_Boss = tk.Label(self.root)
        #     image_card_label_Boss.grid(row = row_idx, column = (column_idx-2)+i+1)
        #     self.image_card_labels_2_Boss.append(image_card_label_Boss)
        # row_idx = row_idx + 1

        pick_button_Print = tk.Button(self.root, text="PrintResult", font=("Helvetica", 20), command=self.PrintOutput)
        pick_button_Print.grid(row = row_idx, column = column_idx-3, ipady=5)

        board_label = tk.Label(root, text="Player:", font=("Helvetica", 20), bg=self.bg)
        board_label.grid(row = row_idx, column = column_idx-2)

        for i in range(2):
            image_card_label = tk.Label(self.root)
            image_card_label.grid(row = row_idx, column = (column_idx-2)+i+1)
            self.image_card_labels_2.append(image_card_label)

    def display_image_phison(self):
        image_phison = "phison.PNG"

        image = Image.open(image_phison)
        image = image.resize((500, 200))
        photo = ImageTk.PhotoImage(image)

        self.image_phison_label.configure(image=photo)
        self.image_phison_label.image = photo

    def get_image_list(self, image_folder):
        image_list = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        return image_list

    def pick_images_Boss(self):
        # Clear previously selected images
        self.selected_images_Boss.clear()

        # Pick 2 unique random images
        while len(self.selected_images_Boss) < 2:
            if len(self.image_list_Boss) == len(self.already_selected_images_Boss):
                break
            random_image = random.choice(self.image_list_Boss)
            if random_image not in self.already_selected_images_Boss:
                self.selected_images_Boss.add(random_image)
                self.already_selected_images_Boss.add(random_image)    

        # Display selected images
        self.display_images_Boss()

    def pick_images_G(self):
        # Clear previously selected images
        self.selected_images_G.clear()

        # Pick 2 unique random images
        while len(self.selected_images_G) < 2:
            if (self.selected_G_Idx == 0):
                if len(self.image_list_G0) == len(self.already_selected_images_G0):
                    if (WA_G0_OneTime == False):
                        self.selected_G_Idx = self.selected_G_Idx + 1
                    break
                random_image = random.choice(self.image_list_G0)
                if random_image not in self.already_selected_images_G0:
                    self.selected_images_G.add(random_image)
                    self.already_selected_images_G0.add(random_image)
            elif (self.selected_G_Idx == 1):
                if len(self.image_list_G1) == len(self.already_selected_images_G1):
                    if (WA_G1_OneTime == False):
                        self.selected_G_Idx = self.selected_G_Idx + 1
                    break
                random_image = random.choice(self.image_list_G1)
                if random_image not in self.already_selected_images_G1:
                    self.selected_images_G.add(random_image)
                    self.already_selected_images_G1.add(random_image)
            elif (self.selected_G_Idx == 2):
                if len(self.image_list_G2) == len(self.already_selected_images_G2):
                    if (WA_G2_OneTime == False):
                        self.selected_G_Idx = self.selected_G_Idx + 1
                    break
                random_image = random.choice(self.image_list_G2)
                if random_image not in self.already_selected_images_G2:
                    self.selected_images_G.add(random_image)
                    self.already_selected_images_G2.add(random_image)
            elif (self.selected_G_Idx == 3):
                if len(self.image_list_G3) == len(self.already_selected_images_G3):
                    if (WA_G3_OneTime == False):
                        self.selected_G_Idx = self.selected_G_Idx + 1
                    break
                random_image = random.choice(self.image_list_G3)
                if random_image not in self.already_selected_images_G3:
                    self.selected_images_G.add(random_image)
                    self.already_selected_images_G3.add(random_image)
            elif (self.selected_G_Idx == 4):
                if len(self.image_list_G4) == len(self.already_selected_images_G4):
                    if (WA_G4_OneTime == False):
                        self.selected_G_Idx = self.selected_G_Idx + 1
                    break
                random_image = random.choice(self.image_list_G4)
                if random_image not in self.already_selected_images_G4:
                    self.selected_images_G.add(random_image)
                    self.already_selected_images_G4.add(random_image)
            elif (self.selected_G_Idx == 5):
                if len(self.image_list_G5) == len(self.already_selected_images_G5):
                    self.selected_G_Idx = self.selected_G_Idx + 1
                    break
                random_image = random.choice(self.image_list_G5)
                if random_image not in self.already_selected_images_G5:
                    self.selected_images_G.add(random_image)
                    self.already_selected_images_G5.add(random_image)
            elif (self.selected_G_Idx == 6):
                if len(self.image_list_G6) == len(self.already_selected_images_G6):
                    self.selected_G_Idx = self.selected_G_Idx + 1
                    break
                random_image = random.choice(self.image_list_G6)
                if random_image not in self.already_selected_images_G6:
                    self.selected_images_G.add(random_image)
                    self.already_selected_images_G6.add(random_image)
            else:
                break

        # Display selected images
        self.reset()
        self.display_images_G()

    def pick_images_Common(self):
        # Clear previously selected images
        self.selected_images_Common.clear()

        # Pick 2 unique random images
        while len(self.selected_images_Common) < 2:
            if len(self.image_list_Common) == len(self.already_selected_images_Common):
                break
            random_image = random.choice(self.image_list_Common)
            if random_image not in self.already_selected_images_Common:
                self.selected_images_Common.add(random_image)
                self.already_selected_images_Common.add(random_image)    

        # Display selected images
        self.reset()
        self.display_images_Common()

    def display_images_Boss(self):
        for i, image_card_label in enumerate(self.image_card_labels_2_Boss):
            if i < 2: #len(self.selected_images_Boss)
                image_filename = os.path.join(self.image_folder_Boss, self.selected_images_Boss.pop())
                image = Image.open(image_filename)
                image = image.resize((Figure_Size, Figure_Size))
                photo = ImageTk.PhotoImage(image)

                # f.write("{}\t\t\t\t".format(image_filename))

                image_card_label.configure(image=photo)
                image_card_label.image = photo
            else:
                # If fewer than 5 images are available, clear the remaining labels
                image_card_label.configure(image=None)
        # f.write("\n")

    def display_images_G(self):
        if (self.selected_G_Idx == 0):
            for i, image_card_label in enumerate(self.image_card_labels_2):
                if i < 2: #len(self.selected_images_Boss)
                    image_filename = os.path.join(self.image_folder_G0, self.selected_images_G.pop())
                    image = Image.open(image_filename)
                    image = image.resize((Figure_Size, Figure_Size))
                    photo = ImageTk.PhotoImage(image)
                    if i == 0:
                        fA.write("{}\n".format(image_filename))
                    elif i == 1:
                        fB.write("{}\n".format(image_filename))

                    image_card_label.configure(image=photo)
                    image_card_label.image = photo
                else:
                    # If fewer than 5 images are available, clear the remaining labels
                    image_card_label.configure(image=None)
            if (WA_G0_OneTime == True):
                self.selected_G_Idx = self.selected_G_Idx + 1

        elif (self.selected_G_Idx == 1):
            for i, image_card_label in enumerate(self.image_card_labels_2):
                if i < 2: #len(self.selected_images_Boss)
                    image_filename = os.path.join(self.image_folder_G1, self.selected_images_G.pop())
                    image = Image.open(image_filename)
                    image = image.resize((Figure_Size, Figure_Size))
                    photo = ImageTk.PhotoImage(image)

                    if i == 0:
                        fA.write("{}\n".format(image_filename))
                    elif i == 1:
                        fB.write("{}\n".format(image_filename))

                    image_card_label.configure(image=photo)
                    image_card_label.image = photo
                else:
                    # If fewer than 5 images are available, clear the remaining labels
                    image_card_label.configure(image=None)
            if (WA_G1_OneTime == True):
                self.selected_G_Idx = self.selected_G_Idx + 1

        elif (self.selected_G_Idx == 2):
            for i, image_card_label in enumerate(self.image_card_labels_2):
                if i < 2: #len(self.selected_images_Boss)
                    image_filename = os.path.join(self.image_folder_G2, self.selected_images_G.pop())
                    image = Image.open(image_filename)
                    image = image.resize((Figure_Size, Figure_Size))
                    photo = ImageTk.PhotoImage(image)

                    if i == 0:
                        fA.write("{}\n".format(image_filename))
                    elif i == 1:
                        fB.write("{}\n".format(image_filename))

                    image_card_label.configure(image=photo)
                    image_card_label.image = photo
                else:
                    # If fewer than 5 images are available, clear the remaining labels
                    image_card_label.configure(image=None)
            if (WA_G2_OneTime == True):
                self.selected_G_Idx = self.selected_G_Idx + 1

        elif (self.selected_G_Idx == 3):
            for i, image_card_label in enumerate(self.image_card_labels_2):
                if i < 2: #len(self.selected_images_Boss)
                    image_filename = os.path.join(self.image_folder_G3, self.selected_images_G.pop())
                    image = Image.open(image_filename)
                    image = image.resize((Figure_Size, Figure_Size))
                    photo = ImageTk.PhotoImage(image)

                    if i == 0:
                        fA.write("{}\n".format(image_filename))
                    elif i == 1:
                        fB.write("{}\n".format(image_filename))

                    image_card_label.configure(image=photo)
                    image_card_label.image = photo
                else:
                    # If fewer than 5 images are available, clear the remaining labels
                    image_card_label.configure(image=None)
            if (WA_G3_OneTime == True):
                self.selected_G_Idx = self.selected_G_Idx + 1

        elif (self.selected_G_Idx == 4):
            for i, image_card_label in enumerate(self.image_card_labels_2):
                if i < 2: #len(self.selected_images_Boss)
                    image_filename = os.path.join(self.image_folder_G4, self.selected_images_G.pop())
                    image = Image.open(image_filename)
                    image = image.resize((Figure_Size, Figure_Size))
                    photo = ImageTk.PhotoImage(image)

                    if i == 0:
                        fA.write("{}\n".format(image_filename))
                    elif i == 1:
                        fB.write("{}\n".format(image_filename))

                    image_card_label.configure(image=photo)
                    image_card_label.image = photo
                else:
                    # If fewer than 5 images are available, clear the remaining labels
                    image_card_label.configure(image=None)
            if (WA_G4_OneTime == True):
                self.selected_G_Idx = self.selected_G_Idx + 1

        elif (self.selected_G_Idx == 5):
            for i, image_card_label in enumerate(self.image_card_labels_2):
                if i < 2: #len(self.selected_images_Boss)
                    image_filename = os.path.join(self.image_folder_G5, self.selected_images_G.pop())
                    image = Image.open(image_filename)
                    image = image.resize((Figure_Size, Figure_Size))
                    photo = ImageTk.PhotoImage(image)

                    if i == 0:
                        fA.write("{}\n".format(image_filename))
                    elif i == 1:
                        fB.write("{}\n".format(image_filename))

                    image_card_label.configure(image=photo)
                    image_card_label.image = photo
                else:
                    # If fewer than 5 images are available, clear the remaining labels
                    image_card_label.configure(image=None)
            if (WA_G5_OneTime == True):
                self.selected_G_Idx = self.selected_G_Idx + 1

        elif (self.selected_G_Idx == 6):
            for i, image_card_label in enumerate(self.image_card_labels_2):
                if i < 2: #len(self.selected_images_Boss)
                    image_filename = os.path.join(self.image_folder_G6, self.selected_images_G.pop())
                    image = Image.open(image_filename)
                    image = image.resize((Figure_Size, Figure_Size))
                    photo = ImageTk.PhotoImage(image)

                    if i == 0:
                        fA.write("{}\n".format(image_filename))
                    elif i == 1:
                        fB.write("{}\n".format(image_filename))

                    image_card_label.configure(image=photo)
                    image_card_label.image = photo
                else:
                    # If fewer than 5 images are available, clear the remaining labels
                    image_card_label.configure(image=None)
            if (WA_G6_OneTime == True):
                self.selected_G_Idx = self.selected_G_Idx + 1

        else:
            for image_card_label in enumerate(self.image_card_labels_2):
                image_card_label.configure(image=None)

    def display_images_Common(self):
        for i, image_card_label in enumerate(self.image_card_labels_2):
            if i < 2: #len(self.selected_images_Boss)
                image_filename = os.path.join(self.image_folder_Common, self.selected_images_Common.pop())
                image = Image.open(image_filename)
                image = image.resize((Figure_Size, Figure_Size))
                photo = ImageTk.PhotoImage(image)

                if i == 0:
                    fA.write("{}\n".format(image_filename))
                elif i == 1:
                    fB.write("{}\n".format(image_filename))

                image_card_label.configure(image=photo)
                image_card_label.image = photo
            else:
                # If fewer than 5 images are available, clear the remaining labels
                image_card_label.configure(image=None)

    def play_music(self):
        pygame.mixer.music.load(".\\backgroundmusic.wav")  # 替換成你的音樂文件的路徑
        pygame.mixer.music.play(-1)

    def PrintOutput(self):
        fA.close()
        fB.close()
        # 創建並顯示 Log Viewer 窗口
        log_viewer_root = tk.Toplevel(self.root)
        log_viewer = LogViewer(log_viewer_root, filenameA, filenameB)

class LogViewer:
    def __init__(self, root, filenameA, filenameB):
        self.root = root
        self.root.title("Team Viewer")
        self.root.geometry("600x900")

        # 配置 grid 的行列权重
        self.root.grid_rowconfigure(0, weight=1)  # 让第一行可扩展
        self.root.grid_columnconfigure(0, weight=1)  # 让第一列可扩展
        self.root.grid_columnconfigure(1, weight=1)  # 让第二列可扩展

        # 创建 A 的 Text
        self.text_area_A = tk.Text(self.root, wrap=tk.WORD, font=("Helvetica", 20))
        self.text_area_A.grid(row=0, column=0, sticky="nsew")  # 使其填满单元格

        # 创建 B 的 Text
        self.text_area_B = tk.Text(self.root, wrap=tk.WORD, font=("Helvetica", 20))
        self.text_area_B.grid(row=0, column=1, sticky="nsew")  # 使其填满单元格

        self.filenameA = filenameA
        self.filenameB = filenameB

        self.update_logs()

    def update_logs(self):

        if os.path.exists(self.filenameA):
            fileA = open(self.filenameA, "r")
            first = True
            try:
                for line in fileA:
                    if (first == True):
                        self.text_area_A.insert(tk.END, line)
                        first = False
                    else:
                        # 先按反斜杠分割，然后按点分割
                        nameA = line.split('\\')[-1].split('.')
                        resultA = nameA[0]
                        print(resultA)
                        self.text_area_A.insert(tk.END, resultA + '\n')
            finally:
                fileA.close()  # 确保文件在使用完后被关闭

        if os.path.exists(self.filenameB):
            fileB = open(self.filenameB, "r")
            first = True
            try:
                for line in fileB:
                    if (first == True):
                        self.text_area_B.insert(tk.END, line)
                        first = False
                    else:
                        # 先按反斜杠分割，然后按点分割
                        nameB = line.split('\\')[-1].split('.')
                        resultB = nameB[0]
                        print(resultB)
                        self.text_area_B.insert(tk.END, resultB + '\n')
            finally:
                fileB.close()  # 确保文件在使用完后被关闭

if __name__ == "__main__":

    fA = None
    fB = None
    if os.path.exists(filenameA) or os.path.exists(filenameB):
        print("File already exists, please check it")
        exit()
    else:
        fA = open(filenameA, "w")
        fB = open(filenameB, "w")
        fA.write("[Red Team]\n")
        fB.write("[Blue Team]\n")

    pygame.init()
    pygame.mixer.init()
    image_folder_path_Boss = ".\\Boss"
    image_folder_path_G0 = ".\\G0"
    image_folder_path_G1 = ".\\G1"
    image_folder_path_G2 = ".\\G2"
    image_folder_path_G3 = ".\\G3"
    image_folder_path_G4 = ".\\G4"
    image_folder_path_G5 = ".\\G5"
    image_folder_path_G6 = ".\\G6"
    image_folder_path_Common = ".\\Common"
    root = tk.Tk()
    app = ImagePickerApp(root, image_folder_path_Boss, image_folder_path_G0, image_folder_path_G1, image_folder_path_G2, image_folder_path_G3, image_folder_path_G4, image_folder_path_G5, image_folder_path_G6, image_folder_path_Common)

    root.mainloop()

    fA.close()
    fB.close()
