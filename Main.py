from DrawingTool import DrawingTool


def main():

    file = open('output.txt', 'w')
    file.close()

    Canvas = DrawingTool()

    for i in Canvas.read_from_file():
        mode, *params = i
        Canvas.draw(mode, Canvas.convert(params))



if __name__ == '__main__':
    main()
