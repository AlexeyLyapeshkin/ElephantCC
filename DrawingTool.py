import numpy as np
import os


class DrawingTool:

    def create_canvas(self, x, y):
        self.MainArray = np.zeros((y, x), dtype=str)

        # self.MainArray[2][3] = 'x' # y, x

    def write_in_file(self):

        x_len = len(self.MainArray[0])
        y_len = len(self.MainArray)

        if os.stat('output.txt').st_size == 0:
            file_output = open('output.txt', 'w')
        else:
            file_output = open('output.txt', 'a')

        for i in range(y_len + 2):

            if i == 0 or i == y_len + 1:
                line = '-' + '-' * x_len + '-' + '\n'

            elif i != 0 and i != y_len + 1:
                line = '|'

                for j in range(x_len):

                    elem = self.MainArray[i - 1][j]
                    if elem != '':
                        line += self.MainArray[i - 1][j]
                    else:
                        line += ' '

                line += '|\n'

            file_output.write(line)

        file_output.close()

    def draw(self, mode, list_of_args):

        if mode.lower() == 'c':
            x, y = list_of_args

            self.create_canvas(x, y)
            self.write_in_file()

        if mode.lower() == 'l':

            x1, y1, x2, y2 = list_of_args

            if x1 == x2 and y1 != y2:
                for i in range(y1, y2):
                    self.MainArray[i][x1] = 'x'

            self.write_in_file()

        if mode.lower() == 'r':

            x1, y1, x2, y2 = list_of_args

            if x1 != x2 and y1 != y2:
                for i in range(x1, x2 + 1):
                    self.MainArray[y1][i] = 'x'
                    self.MainArray[y2][i] = 'x'
                for i in range(y1, y2 + 1):
                    self.MainArray[i][x1] = 'x'
                    self.MainArray[i][x2] = 'x'

            self.write_in_file()

        if mode.lower() == 'b':
            pass
