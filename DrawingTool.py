import numpy as np
import os

CWARN = '\033[93m'
CRED = '\033[91m'
CEND = '\033[0m'


class DrawingTool:
    """
    Class is using to draw a simple figures in text file on "canvas".

    :Usage: In the file input.txt, enter the data in the following format:

        - Line :: L x1 y1 x2 y2 (horizontal or vertical) ((x1,y1) - top left point; (x2,y2) - lower right point)
        - Rectangle :: R x1 y1 x2 y2 ((x1,y1) - top left point; (x2,y2) - lower right point)
        - Bucket Fill :: B x y char ((x,y) - start point, char - char, that will be painted over)
        - Canvas :: width, height.
        - You can only draw if a canvas has been created.
        - Shapes are drawn using the draw method.
        - Read comments.
        - Result in file 'output.txt'.

    """

    def __in_range(self, x1, y1, x2=-1, y2=-1):
        """
        Checks for coordinates on canvas.
        :param x1: top left x coord
        :param y1: top left y coord
        :param x2: lower right x coord or -1, if undefined
        :param y2: lower right y coord or -1, if undefined
        :return: True, if the point(s) is on canvas, else False.
        """

        if x2 == -1 and y2 == -1:

            if x1 in self.pull_x and y1 in self.pull_y:
                return True
            else:
                return False

        elif x2 != -1 and y2 != -1:

            if x1 in self.pull_x and y1 in self.pull_y and x2 in self.pull_x and y2 in self.pull_y:
                return True
            else:
                return False

    def __format_args(self, x1, y1, x2=-1, y2=-1):
        """
        Formats parameters according to the rules of working with arrays.
        :param x1: top left x coord / x cord of point
        :param y1: top left y coord / y coord of point
        :param x2: lower right x coord
        :param y2: lower right y coord
        :return: Normalized parameters. (x,y) / (x1,y1,x2,y2)
        """

        if x2 == -1 and y2 == -1:
            if self.__in_range(x1, y1):
                return x1 - 1, y1 - 1

        elif x2 != -1 and y2 != -1:
            if self.__in_range(x1, y1, x2, y2):
                return x1 - 1, y1 - 1, x2 - 1, y2 - 1

    def __create_canvas(self, x, y):
        """
        Create canvas to draw.
        :param   x:  width
        :param   y:  height
        :return: nothing
        """
        self.MainArray = np.zeros((y, x), dtype=str)  # "Canvas" on which figures will be drawn

        # Width and height of real array.
        self.width = len(self.MainArray[0])
        self.height = len(self.MainArray)

        # Generating sets of X's and Y's.
        self.pull_y = frozenset([y for y in range(self.height + 1)])
        self.pull_x = frozenset([x for x in range(self.width + 1)])

    def __is_createrd_canvas(self):
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

    def __parse_line(self, list_of_lines):
        """
        Split the inputs line of args to divided args.
        :param list_of_lines: list of params from file
        :return: parsed list of params
        """

        list = []

        for i in range(len(list_of_lines)):

            line = list_of_lines[i]
            ind = line.find('#')
            if ind != -1:
                line = line[:ind]
            line = line.split()

            if line != []:
                list.append(line)

        return list

    def read_from_file(self):
        """
        Get args from file.
        :return: generator of params
        """

        file_input = open('input.txt', 'r')
        list_of_lines = file_input.readlines()

        for i in self.__parse_line(list_of_lines):
            yield i

    def __write_in_file(self):
        """
        Wrap output of array/canvas in file.
        :return: nothing
        """

        if os.stat('output.txt').st_size == 0:
            file_output = open('output.txt', 'w')
        else:
            file_output = open('output.txt', 'a')

        for i in range(self.height + 2):

            if i == 0 or i == self.height + 1:
                line = '-' + '-' * self.width + '-' + '\n'

            elif i != 0 and i != self.height + 1:
                line = '|'

                for j in range(self.width):

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
        :return: 1 if all is OK, else -1
        """

        # Drawing Canvas
        if mode.lower() == 'c':
            x, y = list_of_args
            try:
                if x > 0 and y > 0:
                    self.__create_canvas(x, y)
                    self.__write_in_file()

                    return 1
                else:
                    return -1
            except TypeError:
                print(CWARN + 'Bad args! Mode:{0} Args:{1}.'.format(mode.upper(), [x, y]) + CEND)
                return -1

        if self.__is_createrd_canvas():

            # Drawing line.
            if mode.lower() == 'l':

                x1, y1, x2, y2 = list_of_args

                if self.__in_range(x1, y1, x2, y2):

                    x1, y1, x2, y2 = self.__format_args(x1, y1, x2, y2)

                    if x1 == x2 and y1 != y2:
                        for i in range(y1, y2 + 1):
                            self.MainArray[i][x1] = 'x'

                    elif y1 == y2 and x1 != x2:
                        for i in range(x1, x2 + 1):
                            self.MainArray[y1][i] = 'x'

                    self.__write_in_file()
                    return 1

                else:
                    print(CWARN + 'Bad args! Mode:{0} Args:{1}.'.format(mode.upper(), [x1, y1, x2, y2]) + CEND)
                    return -1
            # Drawing rectangle.
            if mode.lower() == 'r':

                x1, y1, x2, y2 = list_of_args

                if self.__in_range(x1, y1, x2, y2):

                    x1, y1, x2, y2 = self.__format_args(x1, y1, x2, y2)

                    if x1 != x2 and y1 != y2:

                        for i in range(x1, x2 + 1):
                            self.MainArray[y1][i] = 'x'
                            self.MainArray[y2][i] = 'x'

                        for i in range(y1, y2 + 1):
                            self.MainArray[i][x1] = 'x'
                            self.MainArray[i][x2] = 'x'

                    self.__write_in_file()
                    return 1

                else:
                    print(CWARN + 'Bad args! Mode:{0} Args:{1}.'.format(mode.upper(), [x1, y1, x2, y2]) + CEND)
                    return -1

            # Flood filling area.
            if mode.lower() == 'b':

                x, y, color = list_of_args

                if self.__in_range(x, y):
                    x, y = self.__format_args(x, y)

                    if len(color) == 1:
                        self.__floodfill(x, y, color)

                    self.__write_in_file()

                else:
                    print(CWARN + 'Bad args! Mode:{0} Args:{1}.'.format(mode.upper(), [x, y]) + CEND)
        else:
            print(CRED + 'Canvas does not created! Impossible to draw a shape.' + CEND)

    def __floodfill(self, x, y, color):
        """
        Non-recursive fill algorithm (using the "stack").
        :param x: x coord of start point
        :param y: y coord of start point
        :param color: the character with which the field will be painted. (len == 1 !)
        :return: nothing
        """

        self.Stack = [(x, y)]

        while len(self.Stack) > 0:

            x, y = self.Stack.pop()

            if self.MainArray[y][x] != '':
                continue

            self.MainArray[y][x] = color

            if x < self.width - 1:
                self.Stack.append((x + 1, y))  # right

            if x > 0:
                self.Stack.append((x - 1, y))  # left

            if y < self.height - 1:
                self.Stack.append((x, y + 1))  # down

            if y > 0:
                self.Stack.append((x, y - 1))  # up
