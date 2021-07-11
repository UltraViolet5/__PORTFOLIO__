using battleship.enums;

namespace battleship.gameElements
{
    public class Playground //co ma robić klasę playground?? czy może być zastąpiona przez klasę board?
    {
        public Field[,] Board { get; set; }

        public Players Player { get; set; }

        public Playground(int boardSize, Players player)
        {
            Board = new Field[boardSize, boardSize];
            this.Player = player;
            CreateBoard();
        }


        public void CreateBoard()
        {
            for (int y = 0; y < this.Board.Length; y++)
            {
                for (int x = 0; x < this.Board.Length; x++)
                {
                    this.Board[y, x] = new Field();
                }
            }
        }
    }
}