import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyPaint")
        self.root.geometry("800x600")

        self.brush_color = "black"
        self.brush_size = 5

        # Canvas oluştur
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(pady=20)
        self.canvas.bind("<B1-Motion>", self.paint)

        # Kontrol paneli oluştur
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        # Fırça rengi seçme düğmesi
        color_button = tk.Button(control_frame, text="Renk Seç", command=self.choose_color)
        color_button.grid(row=0, column=0, padx=5)

        # Fırça boyutu seçme kaydırıcısı
        size_slider = tk.Scale(control_frame, from_=1, to=20, orient=tk.HORIZONTAL, command=self.change_brush_size)
        size_slider.set(self.brush_size)
        size_slider.grid(row=0, column=1, padx=5)

        # Temizleme düğmesi
        clear_button = tk.Button(control_frame, text="Temizle", command=self.clear_canvas)
        clear_button.grid(row=0, column=2, padx=5)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def choose_color(self):
        self.brush_color = colorchooser.askcolor(color=self.brush_color)[1]

    def change_brush_size(self, new_size):
        self.brush_size = int(new_size)

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
