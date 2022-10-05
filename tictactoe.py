from tkinter import Canvas, Tk
from random import randint


class TicTacToe(Canvas):
    def __init__(self, window):
        """Переопределяем конструктор Canvas, определяем размеры окна, определяем статус клеток и статус нажатия."""

        self.window = window
        super().__init__(window, width=300, height=300)
        self.state = [None, None, None, None, None, None, None, None, None]
        self.bind("<Button-1>", self.click)

    def get_winner(self):
        """Определяем победителя по комбинации символов(o или x)."""

        winner_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        combo_list = []
        i = 0
        while i < 8:
            listok = []
            for el in winner_combo[i]:
                listok.append(self.state[el])
            combo_list.append(listok)
            i += 1
        if ['x', 'x', 'x'] in combo_list:
            print("x_win")
            self.window.quit()
        elif ['o', 'o', 'o'] in combo_list:
            print("o_win")
            self.window.quit()
        elif None not in self.state:
            print("draw")
            self.window.quit()

    def bot_move(self):
        """Отрисовка O в ответ на X."""

        if None in self.state:   
            while True:
                random_index = randint(0, 8)
                if self.state[random_index] is None:
                    break
            self.state[random_index] = "o"

            cell_coordinates = ((0, 0), (1, 0), (2, 0), (0, 1),
                                (1, 1), (2, 1), (0, 2), (1, 2), (2, 2))
            self.add_o(cell_coordinates[random_index][0],
                    cell_coordinates[random_index][1])



    def click(self, event):
        """Вычисляет координаты нажатия, вычисляет колонну, строку, индекс клетки по координатам."""
        if event.y < 100:
            if event.x < 100:
                column = 0
                row = 0
                index = 0
            elif event.x > 100 and event.x < 200:
                column = 1
                row = 0
                index = 1
            elif event.x > 200 and event.x < 300:
                column = 2
                row = 0
                index = 2
        if event.y > 100 and event.y < 200:
            if event.x < 100:
                column = 0
                row = 1
                index = 3
            elif event.x > 100 and event.x < 200:
                column = 1
                row = 1
                index = 4
            elif event.x > 200 and event.x < 300:
                column = 2
                row = 1
                index = 5
        if event.y > 200:
            if event.x < 100:
                column = 0
                row = 2
                index = 6
            elif event.x > 100 and event.x < 200:
                column = 1
                row = 2
                index = 7
            elif event.x > 200 and event.x < 300:
                column = 2
                row = 2
                index = 8

        if self.state[index] is None:
            self.state[index] = "x"
            self.add_x(column, row)
            self.bot_move()
            self.get_winner()

    def draw_lines(self):
        """Рисует линии клеток."""

        for iteration in range(1, 3):
            self.create_line(100 * iteration, 0, 100 *
                             iteration, 300, fill='Grey')
            self.create_line(0, 100 * iteration, 300,
                             100 * iteration, fill='Grey')

    def add_x(self, column, row):
        """Рисует крестики."""

        self.create_line(column*100+10, row*100+10,
                         column*100+90, row*100+90, width=5)
        self.create_line(column*100+90, row*100+10,
                         column*100+10, row*100+90, width=5)

    def add_o(self, column, row):
        """Рисует нолики."""

        self.create_oval(
            column*100+10,
            row*100+10,
            column*100+100-10,
            row*100+100-10,
            width=5,
            outline="brown2"
        )


if __name__ == "__main__":
    window = Tk()
    game = TicTacToe(window)
    game.pack()
    game.draw_lines()
    game.get_winner()
    window.mainloop()

