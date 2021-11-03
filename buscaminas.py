
class Buscaminas():
    def __init__(self,buscaminas,board,show):
        self.board = [[' ', '1', 'B', 'B', '1', ' ', '1', 'B'],
                      ['1', '2', '2', '2', '1', ' ', '1', '1'],
                      ['B', '3', '2', '1', ' ', ' ', '1', '1'],
                      ['2', 'B', 'B', '2', ' ', ' ', '1', 'B'],
                      ['2', '4', 'B', '2', ' ', ' ', '1', '1'],
                      ['1', 'B', '3', '2', ' ', ' ', ' ', ' '],
                      ['1', '2', 'B', '1', ' ', ' ', ' ', ' '],
                      [' ', '1', '1', '1', ' ', ' ', ' ', ' ']]
        self.show = show
        self.buscaminas = buscaminas

    def win(self):
        while True:
            buscaminas = False
            for x in range(8):
                for y in range(8):
                    if buscaminas == 0:
                        return True
                    else:
                        return False
    
    def lose(self):
        while True:
            buscaminas = False
            for x in range(8):
                for y in range(8):
                    if buscaminas >= 0:
                        return True
                    else:
                        return False



    def question(self, mov):
        while True:
            mov =['flag', 'uncover'] 
            mov = input ('1. flag \n \n 2.uncover')
            if mov not in mov:
                raise Exception()
            else:
                break
        
        while True:
            row = input ('ingresa el numero de fila')
            if row in row:
                row = int(row)
            else:
                raise Exception()
            break
        
        while True:
            
            col = input ('ingresa el numero de columna')
            if col in col:
                col = int(col)
            else:
                raise Exception()
            break

        return [mov, row, col]

        
    def play(self, mov, col, row):
        while True:
            mov = 0
            row = 0
            col = 0
            flag = True
            pass
