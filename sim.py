import tkinter as tk
from path import Planner

class Arm:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 2
        self.id = canvas.create_oval(self.x-self.size, self.y-self.size,
                                     self.x+self.size, self.y+self.size,
                                     fill="black")

    def move_to(self, new_x, new_y):
        old_x, old_y = self.x, self.y
        self.x, self.y = new_x, new_y
        self.canvas.create_line(old_x, old_y, new_x, new_y, fill="red")
        self.canvas.move(self.id, new_x-old_x, new_y-old_y)

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()
    arm = Arm(canvas, 50, 50)

    # Example usage of move_to method
    # arm.move_to(0, 0)
    # arm.move_to(10, 10)
    # arm.move_to(14, 40)
    a = Planner('sample_gcode/setup.gcode')
    while True:
        arm.move_to(a.generate().x, a.generate().y)

    root.mainloop()
    
if __name__ == '__main__':
    main()
