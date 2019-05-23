import unittest

from DrawingTool import DrawingTool


class test_DrawingTool(unittest.TestCase):

    def test_borders(self):

        file = open('output.txt', 'w')
        file.close()

        DT = DrawingTool()
        DT.draw('c', [4, 4])

        # Line tests
        self.assertEqual(DT.draw('l', [100, 100, 100, 200]), -1, 'Should be -1')
        self.assertEqual(DT.draw('l', [1, 1, 1, 3]), 1, 'Should be 1')

        # Canvas tests
        self.assertEqual(DT.draw('c', [0, 0]), -1, 'Should be -1')
        self.assertEqual(DT.draw('c', ['h', 'w']), -1, 'Should be -1')

        # Rectangle tests
        self.assertEqual(DT.draw('r', [1, 1, 3, 3]), 1, 'Should be 1')
        self.assertEqual(DT.draw('r', [1, 1, 30, 30]), -1, 'Should be -1')




if __name__ == '__main__':
    unittest.main()
