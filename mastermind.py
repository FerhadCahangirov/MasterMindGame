import tkinter as tk
from tkinter import messagebox as mb
import random 

class App(tk.Tk):
    def __init__(self, rn_array):
        super().__init__()

        self.rn_array = rn_array

        self.frame_canvas = tk.Frame(self)
        self.frame_button = tk.Frame(self)
        self.frame_canvas.grid(row = 1)
        self.frame_button.grid(row = 2)
        self.game_status = 0

        self.allowed_number_of_turns = 12
        self.used_number_of_turns = 0
        self.colors = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        self.random_colors_array = [self.colors[self.rn_array[0]], self.colors[self.rn_array[1]], self.colors[self.rn_array[2]], self.colors[self.rn_array[3]]]
        self.coord_of_circle = (5, 5, 40, 40)
        self.click_counter = 0
        self.widget_array = [ [0]*50 for i in range(50)]
        
        self.circles_of_compared_data_template = list()

        for i in range (8):
            self.random_color_selections = tk.Canvas(self.frame_canvas, bg = "gray" , width=40, height = 40)
            self.random_color_selections.bind("<Button-1>", lambda event, color = self.colors[i]:self.get_colors(color, event=event))
            self.random_color_selections.grid(row = 0, column = i, padx=5, pady=5)
            self.random_color_selection_circle = self.random_color_selections.create_oval(self.coord_of_circle,fill=self.colors[i])


        for i in range (1, 12):
            for j in range (2, 6):
                self.approximatable_template = tk.Canvas(self.frame_canvas, bg = "grey", width=40, height = 40)
                self.widget_array[i][j] = self.approximatable_template
                self.widget_array[i][j].grid(row = i, column = j, padx = 5, pady = 5)

        for i in range (12, 13):
            for j in range(2, 6):
                self.approximated_data_template = tk.Canvas(self.frame_canvas, bg = "grey", width=40, height = 40)
                self.widget_array[i][j] = self.approximated_data_template
                self.widget_array[i][j].grid(row = i, column = j, padx = 5, pady = 5)

        for i in range(1, 12):
            self.compared_data_template = tk.Canvas(self.frame_canvas, bg = "grey", width=80, height = 50)
            self.widget_array[i][0] = self.compared_data_template
            for j in range(4):
                if j == 0:
                    self.circles_of_compared_data_template.append(self.widget_array[i][0].create_oval((20, 10, 30, 20), fill = "grey", outline="black"))
                elif j == 1:
                    self.circles_of_compared_data_template.append(self.widget_array[i][0].create_oval((50, 10, 60, 20), fill = "grey", outline="black"))
                elif j == 2:
                    self.circles_of_compared_data_template.append(self.widget_array[i][0].create_oval((20, 30, 30, 40), fill = "grey", outline="black"))
                elif j == 3:
                    self.circles_of_compared_data_template.append(self.widget_array[i][0].create_oval((50, 30, 60, 40), fill = "grey", outline="black"))
                

            self.widget_array[i][0].grid(row = i, column = 0, columnspan = 2)

        set_btn = tk.Button(self.frame_button,text="set", width=10, height=2)
        set_btn.bind("<Button-1>", self.compare_with_system)
        set_btn.grid(column=0, row=0)
        clear_btn = tk.Button(self.frame_button,text="clear", width=10, height=2)
        clear_btn.bind("<Button-1>", self.clear_data)
        clear_btn.grid(column=1, row=0)

    def get_colors(self, color, event):
        if(self.click_counter >= 4 ):
            self.click_counter = 0
        
        get_obj = self.widget_array[12][self.click_counter + 2]
        if(get_obj != 0):
            get_obj.configure(bg = color)
            self.click_counter += 1
        else: 
            print("There is no widget")
            print(get_obj)
    
    def compare_with_system(self, event):
        if(self.used_number_of_turns >= 10):
            mb.showinfo(title=None, message="Game Over")
            exit(0)

        for i in range(2, 6):
            if self.widget_array[12][i]["background"] == "grey":
                mb.showwarning("showwarning", "Fill all the columns!!")
                self.used_number_of_turns -= 1
                break
            
            if self.widget_array[12][i]["background"] == self.random_colors_array[i-2]:
                self.widget_array[self.used_number_of_turns + 1][0].itemconfig(self.circles_of_compared_data_template[i-2], fill="white")
                self.game_status += 1
            elif self.widget_array[12][i]["background"] in self.random_colors_array:
                self.widget_array[self.used_number_of_turns + 1][0].itemconfig(self.circles_of_compared_data_template[i-2], fill="black")
                
        if (self.game_status == 4):
            mb.showinfo(title=None, message="Congratulations you won")
            exit(0)
        else: self.game_status = 0
        self.used_number_of_turns += 1
        print(self.allowed_number_of_turns - self.used_number_of_turns)

    def clear_data(self, event):
        self.click_counter = 0
        for i in range(2, 6):
            get_obj = self.widget_array[12][i].configure(bg = "grey")
            

if __name__ == "__main__":

    r_n1 = random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(0, 1), 2), 3),4) ,5), 6), 7)
    r_n2 = random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(0, 1), 2), 3),4) ,5), 6), 7)
    r_n3 = random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(0, 1), 2), 3),4) ,5), 6), 7)
    r_n4 = random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(random.randint(0, 1), 2), 3),4) ,5), 6), 7)

    rn_array = [r_n1,r_n2, r_n3, r_n4]

    app = App(rn_array)
    app.mainloop()