from DrawingTool import DrawingTool

def main():

    file = open('input.txt','w')
    file.close()
    file = open('output.txt','w')
    file.close()

    Canvas = DrawingTool()
    Canvas.draw('c',[200,40])
    Canvas.draw('l',[0,0,0,3])
    Canvas.draw('r', [0, 0, 3, 3])


if __name__ == '__main__':
    main()


