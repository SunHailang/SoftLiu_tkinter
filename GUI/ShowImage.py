
import tkinter
from PIL import Image

if __name__ == "__main__":
    app_width = 450
    app_height = 300
    tk = tkinter.Tk()
    tk.title('登录')
    screen_width = tk.winfo_screenwidth()
    screen_height = tk.winfo_screenheight()
    x_coord = (screen_width/2) - (app_width/2)
    y_coord = (screen_height/2) - (app_height/2)
    tk.geometry("%dx%d+%d+%d" % (app_width,
                                 app_height, x_coord, y_coord))
    # 阻止Python GUI的大小调整
    tk.resizable(0, 0)
    canvas = tkinter.Canvas(tk, bg='green', height=190, width=293)
    # 带图button，image
    print(Image.open('1.gif'))
    button_img_gif = tkinter.PhotoImage(file='1.gif')
    print(button_img_gif)
    button_img = canvas.create_image(295/2,193/2, image=button_img_gif)
    canvas.pack()
    tk.mainloop()
