from tkinter import Canvas, Tk
from random import randint


class TicTacToe(Canvas):
    def __init__(self, window):
        """Переопределяем конструктор Canvas, определяем размеры окна, определяем статус клеток и статус нажатия."""

        self.window = window
        super().__init__(window, width=300, height=300, bg="seashell2")
        self.state = {(0,0):None, (1,0):None, (2,0):None, (0,1):None, (1,1):None, (2,1):None, (0,2):None, (1,2):None, (2,2):None}
        self.bind("<Button-1>", self.click)

    def get_winner(self):
        """Определяем победителя по комбинации символов(o или x)."""

        winner_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        list_cells = [val for val in self.state.values()]
        if ['x', 'x', 'x'] in winner_combo:
            winner = "x"
            game.show_winner(winner)
        elif ['o', 'o', 'o'] in winner_combo:
            winner = "o"
            game.show_winner(winner)
        elif None not in self.state.values():
            winner = "draw"
            game.show_winner(winner)
    

    def bot_move(self):
        """Отрисовка O в ответ на X."""

        if None in self.state.values():   
            while True:
                random_index = (randint(0, 2), randint(0, 2))
                if self.state[random_index] is None:
                    break
            self.state[random_index] = "o"

            self.add_o(random_index)



    def click(self, event):
        """Вычисляет координаты нажатия, вычисляет колонну, строку, индекс клетки по координатам."""
        pos_x = event.x // 100
        pos_y = event.y // 100
        index = (pos_x, pos_y)

        if self.state[index] is None:
            self.state[index] = "x"
            self.add_x(index)
            self.bot_move()
            self.get_winner()

    def draw_lines(self):
        """Рисует линии клеток."""

        for iteration in range(1, 3):
            self.create_line(100 * iteration, 0, 100 *
                             iteration, 300, fill='Grey')
            self.create_line(0, 100 * iteration, 300,
                             100 * iteration, fill='Grey')

    def add_x(self, index):
        """Рисует крестики."""

        self.create_line(index[0]*100+10, index[1]*100+10,
                         index[0]*100+90, index[1]*100+90, width=5)
        self.create_line(index[0]*100+90, index[1]*100+10,
                         index[0]*100+10, index[1]*100+90, width=5)

    def add_o(self, index):
        """Рисует нолики."""

        self.create_oval(
            index[0]*100+10,
            index[1]*100+10,
            index[0]*100+100-10,
            index[1]*100+100-10,
            width=5,
            outline="navajo white"
        )

    def show_winner(self, winner):
        """Выводит победителя на экран"""

        self.create_rectangle(0, 0, 310, 310, fill='seashell2')
        winner_banner = game.create_text(150, 100, text='', font=("Arial", 20))
        if winner == "x":
            game.itemconfig(winner_banner, text="Крестик победил")
        if winner == "o":
            game.itemconfig(winner_banner, text="Нолик победил")
        if winner == "draw":
            game.itemconfig(winner_banner, text="Ничья")       
            



if __name__ == "__main__":
    window = Tk()
    game = TicTacToe(window)
    game.pack()
    game.draw_lines()
    game.get_winner()
    window.mainloop()

