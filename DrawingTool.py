import numpy as np
import os


class DrawingTool:
    """

    Class is using to draw a simple figures in text file on canvas.

    """

    def create_canvas(self, x, y):
        """
        Create canvas to draw.
        :param   x: x-coord - width
        :param   y: y-coord = height
        :return: nothing
        """
        self.MainArray = np.zeros((y, x), dtype=str)

    def is_createrd_canvas(self):
        """
        Checks existing of MainArray.
        :return: True, if exis; False, if not exist.
        """
        if hasattr(self, 'MainArray'):
            return True
        else:
            return False

    def convert(self, list_):
        """
        Converts numeric values ​​from string to number.
        :param list_: list of params
        :return: converted list
        """
        i = 0
        while i < len(list_):
            if list_[i].isdigit():
                list_[i] = int(list_[i])
            i += 1
        return list_

    def parse_line(self, list_of_lines):
        """
        Split the inputs line of args to divided args.
        :param list_of_lines: list of params from file
        :return: parsed list of params
        """

        list = []

        for i in range(len(list_of_lines)):
            line = list_of_lines[i]
            line = line.split()

            list.append(line)
        return list

    def read_from_file(self):
        """
        Get args from file
        :return: generator of params
        """

        file_input = open('input.txt', 'r')
        list_of_lines = file_input.readlines()

        for i in self.parse_line(list_of_lines):
            yield i

    def write_in_file(self):
        """
        Wrap output of array/canvas in file.
        :return: nothing
        """

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
        """
        Draw figures in canvas.
        :param mode: mode of drawing [C, L, R, B]
        :param list_of_args: list of args
        :return:nothing
        """

        if mode.lower() == 'c':
            x, y = list_of_args

            self.create_canvas(x, y)
            self.write_in_file()

        if self.is_createrd_canvas():

            if mode.lower() == 'l':

                x1, y1, x2, y2 = list_of_args

                if x1 == x2 and y1 != y2:
                    for i in range(y1, y2):
                        self.MainArray[i][x1] = 'x'

                elif y1 == y2 and x1 != x2:
                    for i in range(x1, x2):
                        self.MainArray[y1][i] = 'x'

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

                x, y, color = list_of_args

                if x != y:
                    self.floodfill(x, y, color)

                self.write_in_file()
        else:
            print('Canvas does not created!')

    def floodfill(self, x, y, color):

        arrayWidth = len(self.MainArray[0])
        arrayHeight = len(self.MainArray)

        self.theStack = [(x, y)]

        while len(self.theStack) > 0:

            x, y = self.theStack.pop()

            if self.MainArray[y][x] != '':
                continue

            self.MainArray[y][x] = color

            if x < arrayWidth - 1:
                self.theStack.append((x + 1, y))  # right

            if x > 0:
                self.theStack.append((x - 1, y))  # left

            if y < arrayHeight - 1:
                self.theStack.append((x, y + 1))  # down

            if y > 0:
                self.theStack.append((x, y - 1))  # up
