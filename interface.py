import tkinter as tk

class MouseInteraction:
    def __init__(self, root):
        self.root = root
        self.width = 500
        self.height = 500
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_move)
        self.canvas.bind("<Motion>", self.on_hover)
        self.pixels = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.draw_pixels()

    def on_click(self, event):
        x, y = event.x, event.y
        self.pixels[y][x] = 1 - self.pixels[y][x]
        self.draw_pixels()

    def on_move(self, event):
        x, y = event.x, event.y
        print(f"Moving at: {x}, {y}")

    def on_hover(self, event):
        x, y = event.x, event.y
        self.pixels[y][x] = 1
        self.draw_pixels()

    def draw_pixels(self):
        for y in range(self.height):
            for x in range(self.width):
                color = "blue" if self.pixels[y][x] == 1 else "white"
                self.canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline="")

root = tk.Tk()
mouse_interaction = MouseInteraction(root)
root.mainloop()