'''
fIRST VERSION
BY
VICTOR DANIEL GAUNA CSE-210 SPRING 2022
'''
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-"]
def main():
    display_board()


def play():
    print("Start the Game")

    for i in range(4):
        print("Turn PLayer 1 with a 'X'")
        val="X"
        game(valor)
        for j in range(3):
            print("Turn PLayer 2 with a 'O'")
            val="="
            game(valor)
def game(valor):
    position= int(input("Choose a position from 1 at 9"))





def display_board():
    print("\n")
    print(board[0] ,"|",board[1],"|",board[2], "1|2|3" )
    print(board[3] ,"|",board[4],"|",board[5], "4|5|6" )
    print(board[6] ,"|",board[7],"|",board[8], "7|8|9" )

if __name__ == "__main__":
    main()    


