from math import floor as floor

winner_found = False
draws = []
boards = []

class Board:    
    def __init__(self, arr):
        self.numbers = []
        self.drawn = []
        for line in arr:
            self.numbers.append([int(x) for x in line.split()])
            #fill a logical array with zeroes
            self.drawn.append([0]*len(self.numbers[0]))
            self.bingo = False
        
    def draw(self, n):
        if self.bingo:
            return True
        for i, line in enumerate(self.numbers):
            for j, number in enumerate(line):
                if number == n:
                    self.drawn[i][j] = 1
                    self.checkBingo(i, j)
        if self.bingo:
            self.calculateScore(n)
    
    
    def checkBingo(self, i, j):
        global winner_found
        #check row:
        if sum(self.drawn[i]) == len(self.drawn[i]):
            self.bingo = True
            winner_found = True
        #check column:
        s = len(self.drawn)
        for line in self.drawn:
            s -= line[j] 
        if s == 0:
            self.bingo = True
            winner_found = True
    
    
    def calculateScore(self, n):
        sum = 0
        for i, line in enumerate(self.numbers):
            for j, number in enumerate(line):
                if self.drawn[i][j] == 0:
                    sum += number
        print(sum*n)

with open("tag4.txt") as f:
    lines = [x.strip() for x in f.readlines()]
    draws = [int(x) for x in lines[0].split(",")]
    
    for i in range(floor((len(lines))/6)):
        arr = lines[i*6+2:i*6+7]
        boards.append(Board(arr))
    
    i = 0
    while True:
        for board in boards:
            board.draw(draws[i])
        i += 1
        if i > len(draws) - 1:
            break
    