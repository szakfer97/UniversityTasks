from tkinter import *
from PIL import ImageTk, Image

def forward(img_no):
	global label, button_forward, button_back, button_exit
	label.grid_forget()
	label = Label(image=List_images[img_no-1])
	label.grid(row=1, column=0, columnspan=3)
	button_for = Button(root, text="forward",
						command=lambda: forward(img_no+1))
	if img_no == 4:
		button_forward = Button(root, text="Forward",
								state=DISABLED)
	button_back = Button(root, text="Back",
						command=lambda: back(img_no-1))
	if img_no == 1:
		button_back = Button(root, Text="Back", state=DISABLED)
	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)
	button_for.grid(row=5, column=2)

def back(img_no):
	global label, button_forward, button_back, button_exit
	label.grid_forget()
	label = Label(image=List_images[img_no - 1])
	label.grid(row=1, column=0, columnspan=3)
	button_forward = Button(root, text="forward",
							command=lambda: forward(img_no + 1))
	button_back = Button(root, text="Back",
						command=lambda: back(img_no - 1))
	if img_no == 1:
		button_back = Button(root, Text="Back", state=DISABLED)
	label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=5, column=0)
	button_exit.grid(row=5, column=1)

root = Tk()
root.title("Image Viewer")
root.geometry("700x700")
image_no_1 = ImageTk.PhotoImage(Image.open(r"C:\Users\Hp\Downloads\JavaScript_screenshot.png"))
image_no_2 = ImageTk.PhotoImage(Image.open(r"C:\Users\Hp\Downloads\Christmas_image.jpg"))
image_no_3 = ImageTk.PhotoImage(Image.open(r"C:\Users\Hp\Downloads\Spring_picture.jpg"))
List_images = [image_no_1, image_no_2, image_no_3]
label = Label(image=image_no_1)
label.grid(row=1, column=0, columnspan=3)
button_back = Button(root, text="Back", command=back,
					state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text="Forward",
						command=lambda: forward(1))
button_back.grid(row=5, column=0)
button_exit.grid(row=5, column=1)
button_forward.grid(row=5, column=2)
root.mainloop()

