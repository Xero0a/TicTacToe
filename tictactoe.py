from tkinter import Canvas, Tk
from random import randint


class TicTacToe(Canvas):
    def __init__(self, window):
        """Переопределяем конструктор Canvas, определяем размеры окна, определяем статус клеток и статус нажатия."""

        self.window = window
        super().__init__(window, width=300, height=300, bg="seashell2")
        self.state = {(0, 0):None, (1, 0):None, (2, 0):None, (0, 1):None, (1, 1):None,
                      (2, 1):None, (0, 2):None, (1, 2):None, (2, 2):None}
        self.bind("<Button-1>", self.click)

    def get_winner(self):
        """Получаем победителя по комбинации символов(o или x) и выводим его на экран."""

        cells = [val for val in self.state.values()]
        win_combo = [
            cells[0:3], cells[3:6], cells[6:9], cells[0:7:3], cells[1:8:3],
            cells[2:9:3], cells[0:9:4], cells[2:7:2]
        ]
        if ['x', 'x', 'x'] in win_combo:
            winner = "x"
            game.show_winner(winner)
        elif ['o', 'o', 'o'] in win_combo:
            winner = "o"
            game.show_winner(winner)
        elif None not in self.state.values():
            winner = "draw"
            game.show_winner(winner)
    

    def bot_move(self):
        """Отрисовка нолика в ответ на ход игрока."""

        if None in self.state.values():   
            while True:
                random_key = (randint(0, 2), randint(0, 2))
                if self.state[random_key] is None:
                    break

            self.draw_o(random_key)
            self.state[random_key] = "o"



    def click(self, event):
        """Вычисляет координаты нажатия, вычисляет колонну, строку, ключ клетки по координатам."""
        
        pos_x = event.x // 100
        pos_y = event.y // 100
        key = (pos_x, pos_y)

        if self.state[key] is None:
            self.state[key] = "x"
            self.draw_x(key)
            self.bot_move()
            self.get_winner()

    def draw_lines(self):
        """Рисует линии клеток."""

        for iteration in range(1, 3):
            self.create_line(100 * iteration, 0, 100 *
                             iteration, 300, fill='Grey')
            self.create_line(0, 100 * iteration, 300,
                             100 * iteration, fill='Grey')

    def draw_x(self, key):
        """Рисует крестик."""

        self.create_line(key[0]*100+10, key[1]*100+10,
                         key[0]*100+90, key[1]*100+90, width=5)
        self.create_line(key[0]*100+90, key[1]*100+10,
                         key[0]*100+10, key[1]*100+90, width=5)

    def draw_o(self, key):
        """Рисует нолик."""

        self.create_oval(
            key[0]*100+10,
            key[1]*100+10,
            key[0]*100+100-10,
            key[1]*100+100-10,
            width=5,
            outline="navajo white"
        )

    def show_winner(self, winner):
        """Выводит победителя на экран."""

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

