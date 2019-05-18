from DrawingTool import DrawingTool

CWARN = '\033[93m'
CRED = '\033[91m'
CEND = '\033[0m'


def main():

    file = open('output.txt', 'w')
    file.close()

    DT = DrawingTool()

    line = 1

    for params in DT.read_from_file():

        try:

            mode, *params = params
            DT.draw(mode, DT.convert(params))

        except ValueError:
            print(CWARN + 'Error of convertation params in line {} in file \'input.txt\'.'.format(line) + CEND)

        line += 1


if __name__ == '__main__':
    main()
