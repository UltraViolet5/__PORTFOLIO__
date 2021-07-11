using battleship.enums;
using battleship.gameElements;
using System.Collections.Generic;
using battleship.enums;
using System;

namespace battleship
{
    public class Game
    {
        
        public int BoardSize { get; set; }
        /*
        public Playground PlaygroundFirstPlayer { get; set; }
        public Playground PlaygroundSecondPlayer { get; set; }
        */

        public Board boardPlayerA ;
        public Board boardPlayerB ;

        public List<Ship> shipPlayerA;
        public List<Ship> shipPlayerB;


        public Game()
        {
            /*
            this.BoardSize = boardSize;
            CreatePlaygrounds();
            */
            Display display = new Display();
            Input input = new Input();

            display.Clear();
            display.Menu(DisplayText.BoardSizeInput);  
            
            BoardSize = input.GetBoardSize();

            this.boardPlayerA  = new Board(BoardSize);
            this.boardPlayerB = new Board(BoardSize);

            shipPlayerA = ShipPlacement(this.boardPlayerA, enums.Players.FirstPlayer); // pierwszym graczem jest gracz A
            shipPlayerB = ShipPlacement(this.boardPlayerB, enums.Players.SecondPlayer); // drugim graczem jest gracz B

            // rozpoczynamy bitwę !
            this.Battleship();
            // trzeba dodać funkcję sprawdzającą czy statek jest zatopiony
            
            // bitwa ma się zakończyć wygraną jednego z graczy






        }
        /*
        public void CreatePlaygrounds()
        {
            this.PlaygroundFirstPlayer = new Playground(this.BoardSize, Players.FirstPlayer);
            this.PlaygroundSecondPlayer = new Playground(this.BoardSize, Players.SecondPlayer);
            PlaygroundFirstPlayer.CreateBoard();
            PlaygroundSecondPlayer.CreateBoard();

        }
        */

        public List<Ship> ShipPlacement(Board boardPlayer, battleship.enums.Players player  )
        {
            Display display = new Display();
            
            switch (player)
            {
                case Players.FirstPlayer:
                    display.Clear();
                    display.Write("Seting ship of player A");
                    break;
                case Players.SecondPlayer:
                    display.Clear();
                    display.Write("Seting ship of player B");
                    break;
            }

            Board board = new Board(this.BoardSize);
            List<Ship> PlayerShips = new List<Ship> { };
            
            board.PlaceShip(PlayerShips);

            Input input = new Input();
            // wyświetl pustą planszę bez statków
            display.Board(this.PutShipsOnBoard(boardPlayer, PlayerShips));// było boardPlayerA

            Coordinates cordinates_ship;
            enums.Position position_ship;
            Ship ship;

            
            for(int iterate = 1; iterate <= 3; iterate++)
            {
                //Poproś o koordynaty statku
                cordinates_ship = input.GetCoordinates();
                //Poproś o pozycję czy statek ma być pionowo czy poziomo
                position_ship = input.GetPosition();

                ship = new Ship(iterate, enums.Players.FirstPlayer, cordinates_ship, position_ship);

                PlayerShips.Add(ship);
                // wyczyść ekran
                display.Clear();
                // wyświetl planszę ze statkami
                display.Board(this.PutShipsOnBoard(boardPlayer, PlayerShips));
                if (iterate == 3)
                {
                    input.Pause();
                }

            }
            return PlayerShips;
        }

        //poniższa funkcja jest potrzebna do wyświetlania statków w metodzie display.board
        public Board PutShipsOnBoard(Board boardPlayer, List<Ship> shipList)
        {
            List<Coordinates> shipCoodrinatesList;
            foreach(Ship ship in shipList)
            {
                shipCoodrinatesList = ship.GetShipCoordinates();
                foreach(Coordinates coord in shipCoodrinatesList)
                {
                    boardPlayer.ocean[coord.y][coord.x].ContainShip = true;
                }
            }
            return boardPlayer;
        }


        public void Battleship()
        {
            Display display = new Display();
            Input input = new Input();

            // Wyświetl ekran rozpoczęcia bitwy 
            display.Menu(DisplayText.BattleshipBegin);
            
            // Wyświetl pole bitwy - ocean
            display.Ocean(this.boardPlayerA, this.boardPlayerB);

            bool is_running = true;
            while (is_running)
            {
                Round(Players.FirstPlayer);
                display.Clear();
                CheckShips(enums.Players.SecondPlayer); // wprowadz zmiany w statkach na planszy gracza B
                is_running = !IsWiner(enums.Players.FirstPlayer); // sprawdź czy gracz A jest zwycięzcą
                if (!is_running)
                {
                    display.Menu(DisplayText.PlayerA_Win);
                    input.Pause();
                    break;
                }
                
                
                display.Ocean(boardPlayerA, boardPlayerB);

                Round(Players.SecondPlayer);
                display.Clear();
                CheckShips(enums.Players.FirstPlayer); // wprowadz zmiany w statkach na planszy gracza A
                is_running = !IsWiner(enums.Players.SecondPlayer); // sprawdź czy gracz B jest zwycięzcą
                if (!is_running)
                {
                    display.Menu(DisplayText.PlayerB_Win);
                    input.Pause();
                    break;
                }

                display.Ocean(boardPlayerA, boardPlayerB);

            }
        }

        public void Round(enums.Players player)
        {
            Input input = new Input();
            Coordinates coord;
            Display display = new Display();
            
            if (player == Players.FirstPlayer)
            {
                display.Write("Player A is shooting");
            }
            else 
            {
                display.Write("Player B is shooting");
            }

            coord = input.GetCoordinates();
            
            if (player == Players.FirstPlayer)
            {
                Shot(coord, this.boardPlayerB, player);
            }
            else
            {
                Shot(coord, this.boardPlayerA, player);
            }


        }

        public void Shot(Coordinates coord, Board boardPlayer, enums.Players shooter)
        {
            Display display = new Display();
            // jak jest runda firstplayera to strzelamy do tarczy gracza b
            // jak jest runda secondplayera to strzelamy do tarczy gracza a
            
            switch (boardPlayer.ocean[coord.y][coord.x].State)
            {
                /*            
                Fired,// ostrzelane pole bez statku N
                Free,// wolne pole F
                Hit,// uderzony H
                HitSunk // trafiony zatopiony S
                */

                // jeżeli wolne pole 
                case SateOfField.Free:
                    if (boardPlayer.ocean[coord.y][coord.x].ContainShip == true)
                    {
                        boardPlayer.ocean[coord.y][coord.x].State = SateOfField.Hit;
                    }
                    else
                    {
                        // jeżeli strzelamy a niema statku to oznaczamy pole jako ostrzelane
                        boardPlayer.ocean[coord.y][coord.x].State = SateOfField.Fired;
                    }

                    break;
                    // jeżeli ostrzelane pole bez statku
                    case SateOfField.Fired:
                    // jeżeli gracz strzelił w ostrzelane pole to:
                    display.Clear();
                    display.Write("This field was shoted before!");
                    break;
                    // jeżeli statek został ostrzelany
                    case SateOfField.Hit:
                    display.Clear();
                    display.Write("This field was shoted before!");

                    break;
                    // jeżeli statek został zatopiony
                    case SateOfField.HitSunk:
                    display.Clear();
                    display.Write("This field was shoted before!");

                    break;

            }

            if (shooter == Players.FirstPlayer)
            {
                this.boardPlayerB = boardPlayer;
            }
            else
            {
                this.boardPlayerA = boardPlayer;
            }

        }

        public void CheckShips(enums.Players shotedPlayer )
        {
            /*
            Fired,// ostrzelane pole bez statku
            Free,// wolne pole
            Hit,// uderzony
            HitSunk // trafiony zatopiony
            */
            bool is_sunk;

            if (shotedPlayer == Players.SecondPlayer)
            {
                // jeżeli była ostrzelana plansza gracza B
                foreach ( Ship ship in shipPlayerB)
                {
                    is_sunk = true;
                    foreach(Coordinates coord in ship.GetShipCoordinates() )
                    {
                        if(boardPlayerB.ocean[coord.y][coord.x].State == SateOfField.Free)
                        {
                            is_sunk = false;
                        }
                    }
                    //jeżeli statek ma zatopione wszystkie maszty to zmień jego stan na zatopiony
                    if(is_sunk == true)
                    {
                        foreach (Coordinates coord in ship.GetShipCoordinates())
                        {
                            boardPlayerB.ocean[coord.y][coord.x].State = SateOfField.HitSunk;
                        }
                    }
                }
            }
            else
            {
                // jeżeli była ostrzelana plansza gracza A
                foreach (Ship ship in shipPlayerA)
                {
                    is_sunk = true;
                    foreach (Coordinates coord in ship.GetShipCoordinates())
                    {
                        if (boardPlayerA.ocean[coord.y][coord.x].State == SateOfField.Free)
                        {
                            is_sunk = false;
                        }
                    }
                    //jeżeli statek ma zatopione wszystkie maszty to zmień jego stan na zatopiony
                    if (is_sunk == true)
                    {
                        foreach (Coordinates coord in ship.GetShipCoordinates())
                        {
                            boardPlayerA.ocean[coord.y][coord.x].State = SateOfField.HitSunk;
                        }
                    }
                }
            }

        }

        public bool IsWiner(enums.Players shoterPlayer)
        {
            bool all_ship_sunk;
            all_ship_sunk = true;

            if (shoterPlayer == Players.SecondPlayer)
            {
                // jeżeli strzela gracz B
                foreach (Ship ship in shipPlayerA)
                {
                    foreach (Coordinates coord in ship.GetShipCoordinates())
                    {
                        if (boardPlayerA.ocean[coord.y][coord.x].State != SateOfField.HitSunk)
                        {
                            all_ship_sunk = false;
                        }
                    }
                }
            }
            else
            {
                // jeżeli strzela gracz A
                foreach (Ship ship in shipPlayerB)
                {
                    foreach (Coordinates coord in ship.GetShipCoordinates())
                    {
                        if (boardPlayerB.ocean[coord.y][coord.x].State != SateOfField.HitSunk)
                        {
                            all_ship_sunk = false;
                        }
                    }
                }
            }
            return all_ship_sunk;
        }
    }
}