using System;
using battleship.enums;
using battleship.gameElements;
using System.Collections.Generic;

namespace battleship
{
    public class Display
    {
        
        private string alphabet_char(int char_nr)
        {
            switch (char_nr)
            {
                case 1:
                    return "A";
                case 2:
                    return "B";
                case 3:
                    return "C";
                case 4:
                    return "D";
                case 5:
                    return "E";
                case 6:
                    return "F";
                case 7:
                    return "G";
                case 8:
                    return "H";
                case 9:
                    return "I";
                case 10:
                    return "J";
                case 11:
                    return "K";
                case 12:
                    return "L";
                case 13:
                    return "M";
                case 14:
                    return "N";
                case 15:
                    return "O";
                case 16:
                    return "P";
                case 17:
                    return "R";
                case 18:
                    return "S";
                case 19:
                    return "T";
                case 20:
                    return "U";
                case 21:
                    return "W";
                case 22:
                    return "X";
                case 23:
                    return "Y";
                case 24:
                    return "Z";

                default:
                    return " ";

            }
        }
        
        public void Board(Board Ocean_player)
        {
            /*
            PLAYER A     
              A B C D E F  
            1 O O O O O O 1
            2 O O O O O O 2
            3 O O O O O O 3
            4 O O O O O O 4
            5 O O O O O O 5
              A B C D E F 
            */
            //Console.Clear();
            int row = Ocean_player.ocean[0].Count; // pobiera z planszy playera a szerokość planszy szerokości muszą być takie same

            // ma być 7 spacji dla 5 znakowej planszy
            //jeżeli plansza jest większa od 5 np x 5+x to spacji ma być 2*x

            //Druga linia
            Console.Write("   "); //najpierw trzy spacje 

            for (int i = 0; i < row; i++)
            {
                //Potem ma być duża litera alfabetu w pętli w zależności od row A, B, C, D,E,F,G,H,I,J,K,L,M
                Console.Write(alphabet_char(i + 1)); // są drukowane kolejne litery alfabetu 
                //potem spacja
                Console.Write(" ");
            }

            Console.Write("\n");

            // trzecia linia i kolejne
            for (int y = 0; y < row; y++)
            {
                if (y + 1 < 10)//jeżeli liczba jest jedno znakowa to przed liczbą ma być jedna spacja
                {
                    Console.Write(" ");
                }
                Console.Write(Convert.ToString(y + 1)); // w pierwszej lini to będzie 1
                Console.Write(" ");
                for (int x = 0; x < row; x++)
                {
                    if (Ocean_player.ocean[y][x].ContainShip == true)
                    {
                        Console.Write("#"); //jak jest statek

                    }
                    else
                    {
                        Console.Write("O"); //jak niema statku
                    }

                    Console.Write(" "); // spacja oddzielająca kolumny
                }
                Console.Write(Convert.ToString(y + 1));
                Console.Write("\n");
            }

            // Ostatnia linia jest taka sama jak druga

            Console.Write("   "); //najpierw trzy spacje 

            for (int i = 0; i < row; i++)
            {
                //Potem ma być duża litera alfabetu w pętli w zależności od row A, B, C, D,E,F,G,H,I,J,K,L,M
                Console.Write(alphabet_char(i + 1)); // są drukowane kolejne litery alfabetu 
                //potem spacja
                Console.Write(" ");
            }

            Console.Write("\n");

        }


        public void Ocean(Board Ocean_player_A, Board Ocean_player_B)
        {
            /*
            PLAYER A       PLAYER B
              A B C D E F  A B C D E F  
            1 O O O O O O  O O O O O O 1
            2 O O O O O O  O O O O O O 2
            3 O O O O O O  O O O O O O 3
            4 O O O O O O  O O O O O O 4
            5 O O O O O O  O O O O O O 5
              A B C D E F  A B C D E F  
            */
            int row = Ocean_player_A.ocean[0].Count; // pobiera z planszy playera a szerokość planszy szerokości muszą być takie same

            // Pierwsza linia
            Console.Write("PLAYER A     ");
            // ma być 7 spacji dla 5 znakowej planszy
            //jeżeli plansza jest większa od 5 np x 5+x to spacji ma być 2*x
            for (int i = 5; i < row; i++)
            {
                Console.Write("  ");
            }

            Console.Write("PLAYER B\n");

            //Druga linia
            Console.Write("   "); //najpierw trzy spacje 

            for (int i = 0; i < row; i++)
            {
                //Potem ma być duża litera alfabetu w pętli w zależności od row A, B, C, D,E,F,G,H,I,J,K,L,M
                Console.Write(alphabet_char(i + 1)); // są drukowane kolejne litery alfabetu 
                //potem spacja
                Console.Write(" ");
            }

            Console.Write(" ");
            for (int i = 0; i < row; i++)
            {
                //Potem ma być duża litera alfabetu w pętli w zależności od row A, B, C, D,E,F,G,H,I,J,K,L,M
                Console.Write(alphabet_char(i + 1)); // są drukowane kolejne litery alfabetu
                //potem spacja
                Console.Write(" ");
            }
            Console.Write("\n");

            for (int y = 0; y < row; y++)
            {
                if (y + 1 < 10)//jeżeli liczba jest jedno znakowa to przed liczbą ma być jedna spacja
                {
                    Console.Write(" ");
                }
                Console.Write(Convert.ToString(y + 1)); // w pierwszej lini to będzie 1
                Console.Write(" ");
                for (int x = 0; x < row; x++)
                {
                    Console.Write(Ocean_player_A.ocean[y][x].Symbol);
                    Console.Write(" ");
                }
                Console.Write(" ");
                for (int x = 0; x < row; x++)
                {
                    Console.Write(Ocean_player_B.ocean[y][x].Symbol);
                    Console.Write(" ");
                }
                Console.Write(Convert.ToString(y + 1));
                Console.Write("\n");
            }

            // Ostatnia linia jest taka sama jak druga
            Console.Write("   "); //najpierw trzy spacje 

            for (int i = 0; i < row; i++)
            {
                //Potem ma być duża litera alfabetu w pętli w zależności od row A, B, C, D,E,F,G,H,I,J,K,L,M
                Console.Write(alphabet_char(i + 1)); // są drukowane kolejne litery alfabetu 
                //potem spacja
                Console.Write(" ");
            }

            Console.Write(" ");
            for (int i = 0; i < row; i++)
            {
                //Potem ma być duża litera alfabetu w pętli w zależności od row A, B, C, D,E,F,G,H,I,J,K,L,M
                Console.Write(alphabet_char(i + 1)); // są drukowane kolejne litery alfabetu
                //potem spacja
                Console.Write(" ");
            }
            Console.Write("\n");

        }

        public void Menu(DisplayText version)
        {
            
            //version 0 Welcome text
            switch (version)
            {
                case DisplayText.WelcomeGraphic:

                    Console.WriteLine(" _    _      _                                 ");
                    Console.WriteLine("| |  | |    | |                                ");
                    Console.WriteLine("| |  | | ___| | ___ ___  _ __ ___   ___        ");
                    Console.WriteLine("| |/\\| |/ _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\       ");
                    Console.WriteLine("\\  /\\  /  __/ | (_| (_) | | | | | |  __/       ");
                    Console.WriteLine(" \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___|       ");
                    Console.WriteLine("                                               ");
                    Console.WriteLine("                                               ");
                    Console.WriteLine("                _                              ");
                    Console.WriteLine("               (_)                             ");
                    Console.WriteLine("                _ _ __                         ");
                    Console.WriteLine("               | | '_ \\                        ");
                    Console.WriteLine("               | | | | |                       ");
                    Console.WriteLine("               |_|_| |_|                       ");
                    Console.WriteLine("                                               ");
                    Console.WriteLine("                                               ");
                    Console.WriteLine(" _           _   _   _           _     _       ");
                    Console.WriteLine("| |         | | | | | |         | |   (_)      ");
                    Console.WriteLine("| |__   __ _| |_| |_| | ___  ___| |__  _ _ __  ");
                    Console.WriteLine("| '_ \\ / _` | __| __| |/ _ \\/ __| '_ \\| | '_ \\ ");
                    Console.WriteLine("| |_) | (_| | |_| |_| |  __/\\__ \\ | | | | |_) |");
                    Console.WriteLine("|_.__/ \\__,_|\\__|\\__|_|\\___||___/_| |_|_| .__/ ");
                    Console.WriteLine("                                        | |    ");
                    Console.WriteLine("                                        |_|   ");


                    break;

                case DisplayText.WelcomeMenu: // Welcome menu

                    Console.WriteLine("*********************************************");
                    Console.WriteLine("*                                           *");
                    Console.WriteLine("* 1 - Start multiplayer game                *");
                    Console.WriteLine("* 2 - Start singleplayer game win AI        *");
                    Console.WriteLine("* 3 - Info about game                       *");
                    Console.WriteLine("* 4 - to exit game                          *");
                    Console.WriteLine("*                                           *");
                    Console.WriteLine("*********************************************");


                    break;
                case DisplayText.InfoAboutGame: // info about game
                    Console.WriteLine("****************************************************************************");
                    Console.WriteLine("*                                                                          *");
                    Console.WriteLine("* Battleship (also Battleships or Sea Battle[1]) is a strategy type        *");
                    Console.WriteLine("* guessing game for two players. It is played on ruled grids               *");
                    Console.WriteLine("* (paper or board) on which each player's fleet of ships                   *");
                    Console.WriteLine("* (including battleships) are marked.                                      *");
                    Console.WriteLine("* The locations of the fleets are concealed from the other player. Players *");
                    Console.WriteLine("* alternate turns calling \"shots\" at the other player's ships, and the     *");
                    Console.WriteLine("* objective of the game is to destroy the opposing player's fleet.         *");
                    Console.WriteLine("* Battleship is known worldwide as a pencil and paper game which dates     *");
                    Console.WriteLine("* from World War I. It was published by various companies as a             *");
                    Console.WriteLine("* pad-and-pencil g0ame in the 1930s, and was released as a plastic board   *");
                    Console.WriteLine("* game by Milton Bradley in 1967. The game has spawned electronic          *");
                    Console.WriteLine("* versions, video games, smart device apps and a film.                     *");
                    Console.WriteLine("*                                                                          *");
                    Console.WriteLine("****************************************************************************");
                    break;

                case DisplayText.BoardSizeInput: // input board size

                    Console.WriteLine("*********************************************");
                    Console.WriteLine("*                                           *");
                    Console.WriteLine("*    Put board size (5 - 15)                *");
                    Console.WriteLine("*                                           *");
                    Console.WriteLine("*********************************************");

                    break;
                case DisplayText.BattleshipBegin:
                    Console.Clear();

                    Console.WriteLine("______  ___ _____ _____ _      _____ _____ _   _ ___________ ");
                    Console.WriteLine("| ___ \\/ _ \\_   _|_   _| |    |  ___/  ___| | | |_   _| ___ \\");
                    Console.WriteLine("| |_/ / /_\\ \\| |   | | | |    | |__ \\ `--.| |_| | | | | |_/ /");
                    Console.WriteLine("| ___ \\  _  || |   | | | |    |  __| `--. \\  _  | | | |  __/ ");
                    Console.WriteLine("| |_/ / | | || |   | | | |____| |___/\\__/ / | | |_| |_| |    ");
                    Console.WriteLine("\\____/\\_| |_/\\_/   \\_/ \\_____/\\____/\\____/\\_| |_/\\___/\\_|    ");
                    Console.WriteLine("                                                             ");
                    Console.WriteLine("                                                             ");
                    Console.WriteLine("______ _____ _____ _____ _   _                               ");
                    Console.WriteLine("| ___ \\  ___|  __ \\_   _| \\ | |                              ");
                    Console.WriteLine("| |_/ / |__ | |  \\/ | | |  \\| |                              ");
                    Console.WriteLine("| ___ \\  __|| | __  | | | . ` |                              ");
                    Console.WriteLine("| |_/ / |___| |_\\ \\_| |_| |\\  |                              ");
                    Console.WriteLine("\\____/\\____/ \\____/\\___/\\_| \\_/                              ");
                    Console.WriteLine("");
                    Console.WriteLine("");
                    break;

                case DisplayText.PlayerA_Win:
                    Console.WriteLine("");
                    Console.WriteLine("  _____  _                                  ");
                    Console.WriteLine(" |  __ \\| |                           /\\    ");
                    Console.WriteLine(" | |__) | | __ _ _   _  ___ _ __     /  \\   ");
                    Console.WriteLine(" |  ___/| |/ _` | | | |/ _ \\ '__|   / /\\ \\  ");
                    Console.WriteLine(" | |    | | (_| | |_| |  __/ |     / ____ \\ ");
                    Console.WriteLine(" |_|    |_|\\__,_|\\__, |\\___|_|    /_/    \\_\\");
                    Console.WriteLine(" (_)              __/ |                     ");
                    Console.WriteLine("  _ ___          |___/                      ");
                    Console.WriteLine(" | / __|                                    ");
                    Console.WriteLine(" | \\__ \\                                    ");
                    Console.WriteLine(" |_|___/     ___                            ");
                    Console.WriteLine(" \\ \\        / (_)                           ");
                    Console.WriteLine("  \\ \\  /\\  / / _ _ __  _ __   ___ _ __      ");
                    Console.WriteLine("   \\ \\/  \\/ / | | '_ \\| '_ \\ / _ \\ '__|     ");
                    Console.WriteLine("    \\  /\\  /  | | | | | | | |  __/ |        ");
                    Console.WriteLine("     \\/  \\/   |_|_| |_|_| |_|\\___|_|   ");
                    Console.WriteLine("");

                    break;
                case DisplayText.PlayerB_Win:
                    Console.WriteLine("");
                    Console.WriteLine("  _____  _                         ____  ");
                    Console.WriteLine(" |  __ \\| |                       |  _ \\ ");
                    Console.WriteLine(" | |__) | | __ _ _   _  ___ _ __  | |_) |");
                    Console.WriteLine(" |  ___/| |/ _` | | | |/ _ \\ '__| |  _ < ");
                    Console.WriteLine(" | |    | | (_| | |_| |  __/ |    | |_) |");
                    Console.WriteLine(" |_|    |_|\\__,_|\\__, |\\___|_|    |____/ ");
                    Console.WriteLine(" (_)              __/ |                  ");
                    Console.WriteLine("  _ ___          |___/                   ");
                    Console.WriteLine(" | / __|                                 ");
                    Console.WriteLine(" | \\__ \\                                 ");
                    Console.WriteLine(" |_|___/     ___                         ");
                    Console.WriteLine(" \\ \\        / (_)                        ");
                    Console.WriteLine("  \\ \\  /\\  / / _ _ __  _ __   ___ _ __   ");
                    Console.WriteLine("   \\ \\/  \\/ / | | '_ \\| '_ \\ / _ \\ '__|  ");
                    Console.WriteLine("    \\  /\\  /  | | | | | | | |  __/ |     ");
                    Console.WriteLine("     \\/  \\/   |_|_| |_|_| |_|\\___|_|   ");
                    Console.WriteLine("");

                    break;



            }
        }

        public void Clear()
        {
            Console.Clear();
        }

        public void Write(string text)
        {
            Console.WriteLine(text);
        }
    }
}