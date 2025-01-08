import time
import keyboard
import os


class Game:
    def __init__(self, stagesize):
        self.stagesize = stagesize
        self.stage = [[0 for _ in range(self.stagesize)] for _ in range(self.stagesize)]
        self.selected = [int(self.stagesize / 2), int(self.stagesize / 2)]
        self.judge_move_list = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
        self.player = 1
        self.isfinished = False

        keyboard.add_hotkey("up", lambda:self.move_cursor("up"))
        keyboard.add_hotkey("down", lambda:self.move_cursor("down"))
        keyboard.add_hotkey("right", lambda:self.move_cursor("right"))
        keyboard.add_hotkey("left", lambda:self.move_cursor("left"))
        keyboard.add_hotkey("space", self.put)
        self.display()
    
    def move_cursor(self, dir):
        match dir:
            case "up":
                if self.selected[1] > 0:
                    self.selected[1] -= 1
            case "down":
                if self.selected[1] < self.stagesize - 1:
                    self.selected[1] += 1
            case "right":
                if self.selected[0] < self.stagesize - 1:
                    self.selected[0] += 1
            case "left":
                if self.selected[0] > 0:
                    self.selected[0] -= 1
        self.display()
    
    def put(self):
        self.stage[self.selected[1]][self.selected[0]] = self.player
        self.display()
        self.judge()
        self.player = -1 * (self.player - 3)
        
    
    def judge(self):
        count = 1
        for move in self.judge_move_list:
            for i in range(1, 5):
                if -1 < self.selected[0] + move[0] * i < self.stagesize and -1 < self.selected[1] + move[1] * i < self.stagesize:
                    if self.stage[self.selected[1] + move[1] * i][self.selected[0] + move[0] * i] == self.player:
                        count += 1
                    else:
                        break
            for i in range(-1, -5, -1):
                if -1 < self.selected[0] + move[0] * i < self.stagesize and -1 < self.selected[1] + move[1] * i < self.stagesize:
                    if self.stage[self.selected[1] + move[1] * i][self.selected[0] + move[0] * i] == self.player:
                        count += 1
                    else:
                        break
            if count > 4:
                if self.player == 1:
                    print("黒の勝ち!")
                else:
                    print("白の勝ち!")
                self.isfinished = True
                break
            count = 1
    
    def display(self):
        os.system("cls")
        disp = ""
        for i, li in enumerate(self.stage):
            for j, el in enumerate(li):
                if i == self.selected[1] and j == self.selected[0]:
                    disp += " ■"
                else:
                    match el:
                        case 0:
                            disp += "  "
                        case 1:
                            disp += " ○"
                        case 2:
                            disp += " ●"
            disp += "\n"
        print(disp)


if __name__ == "__main__":
    while 1:
        game = Game(31)
        while not game.isfinished:
            time.sleep(0.1)
        time.sleep( 3) 