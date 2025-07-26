
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import threading

import qrcode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image

class app:
    QR = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # GUI
    def __init__(self):
        root = tk.Tk()
        root.title("QR Code Generator")
        root.geometry("400x250")

        self.INFO = tk.StringVar()
        self.OUTPUT_NAME = tk.StringVar()

        tk.Label(root, text="Enter QR Info:").pack(pady=(20, 5))
        qr_info_entry = tk.Entry(root, width=50, textvariable= self.INFO)
        qr_info_entry.pack()

        self.include_picture_var = tk.BooleanVar()
        include_picture_check = tk.Checkbutton(root, text="Include Picture", variable=self.include_picture_var)
        include_picture_check.pack(pady=10)

        tk.Label(root, text="Output File Name:").pack(pady=(10, 5))
        output_name_entry = tk.Entry(root, width=50, textvariable= self.OUTPUT_NAME)
        output_name_entry.pack()

        generate_button = ttk.Button(root, text="Generate QR Code", command=self.generate_QR)
        generate_button.pack(pady=20)

        root.mainloop()

    def generate_QR(self):
        self.QR.add_data(self.INFO.get())

        if self.include_picture_var.get():
            img = self.QR.make_image(image_factory=StyledPilImage, embeded_image_path=askopenfilename())
        else:
            img = self.QR.make_image(image_factory=StyledPilImage)

        img.save(f"{self.OUTPUT_NAME.get()}.png")

        self.INFO.set("")
        self.OUTPUT_NAME.set("")
        self.include_picture_var.set(False)

        threading.Thread(target=lambda: img.show()).start()
        messagebox.showinfo("Info", "QR Code generated successfully!")

app()
