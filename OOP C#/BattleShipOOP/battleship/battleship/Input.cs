using System;
using battleship.gameElements;

namespace battleship
{
    public class Input // klasa była statyczna i powinna być statyczna
    {
        public int GetBoardSize()
        {
            System.Console.WriteLine("Podaj szerokość planszy : ");
            string input = System.Console.ReadLine();
            int to_return = Convert.ToInt32(input);

            return to_return;
        
        }


        public  Coordinates GetCoordinatesNew()
        {
            Coordinates userCoordinates = new Coordinates();
            bool InputCorrectX = false;
            bool InputCorrectY = false;
            while (InputCorrectX)
            {
                System.Console.WriteLine("Get X coordinates: ");
                string userInputXstring = Console.ReadLine();
                int userInputX;
                InputCorrectX = int.TryParse(userInputXstring, out userInputX);

                if (CantConvertToInt(userInputXstring) == true)
                {
                    userInputX = CharCoordinateToInt(userInputXstring);
                    userCoordinates.x = userInputX;
                    InputCorrectX = true;

                }
                else
                {
                    Console.WriteLine("Incorrect input !");
                    InputCorrectX = false;
                }
            }
            while (InputCorrectY)
            {
                System.Console.WriteLine("Get Y coordinates: ");
                string userInputYstring = Console.ReadLine();
                int userInputY;
                InputCorrectY = int.TryParse(userInputYstring, out userInputY);
                if (InputCorrectY == false)
                {
                    Console.WriteLine("Incorrect input !");
                    InputCorrectY = false;
                }
                else
                {
                    InputCorrectY = true;
                    userCoordinates.y = userInputY;
                }
            }

            return userCoordinates;
        }

        private static bool CantConvertToInt(string char_nr)
        {
            int UserInputChar;
            if (int.TryParse(char_nr, out UserInputChar))
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        
        public Coordinates GetCoordinates()
        {
            Display display = new Display();
            display.Write("Put coordinates eg \"A1\", \"C3\", \"C14\" : ");
            string str_coordinates =  Console.ReadLine();
            //Console.WriteLine("Długość koordynat");
            //Console.WriteLine(Convert.ToString( str_coordinates.Length ) );

            //str_coordinates[0]; //pierwsza koordynata Litera
            Coordinates coordinates = new Coordinates();
          
            coordinates.x = CharCoordinateToInt(Convert.ToString(str_coordinates[0] ));
            
            
                switch (str_coordinates.Length)
                {
                    case 2:
                        coordinates.y = Convert.ToInt16(str_coordinates.Substring(1, 1)) - 1 ;
                        break;
          
                    case 3:
                        coordinates.y = Convert.ToInt16(str_coordinates.Substring(1, 2)) - 1 ;
                        break;

                }

            
            
            return coordinates;
        }
        








        public enums.Position GetPosition()
        {
            Display display = new Display();
            display.Write("Put H to set ship horizontal, put V to set ship vertical :");
            string ReadedLine = Console.ReadLine();
            switch (ReadedLine)
            {
                case "h":
                    return enums.Position.Horizontal;
                case "H":
                    return enums.Position.Horizontal;
                case "v":
                    return enums.Position.Vertical;
                case "V":
                    return enums.Position.Vertical;
                default:
                    return enums.Position.Vertical; // jak niewiadomo jak to pionowo
                
            }

        }

        public int CharCoordinateToInt(string CoordinateChar)
        {
            switch (CoordinateChar)
            {
                case "a":
                    return 0;
                case "A":
                    return 0;
                
                case "b":
                    return 1;
                case "B":
                    return 1;

                case "c":
                    return 2;
                case "C":
                    return 2;

                case "d":
                    return 3;
                case "D":
                    return 3;

                case "e":
                    return 4;
                case "E":
                    return 4;

                case "f":
                    return 5;
                case "F":
                    return 5;

                case "g":
                    return 6;
                case "G":
                    return 6;

                case "h":
                    return 7;
                case "H":
                    return 7;

                case "i":
                    return 8;
                case "I":
                    return 8;

                case "j":
                    return 9;
                case "J":
                    return 9;

                case "k":
                    return 10;
                case "K":
                    return 10;

                case "l":
                    return 11;
                case "L":
                    return 11;

                case "m":
                    return 12;
                case "M":
                    return 12;

                case "n":
                    return 13;
                case "N":
                    return 13;

                case "o":
                    return 14;
                case "O":
                    return 14;

                case "p":
                    return 15;
                case "P":
                    return 15;

                case "r":
                    return 16;
                case "R":
                    return 16;

                case "s":
                    return 17;
                case "S":
                    return 17;

                case "t":
                    return 18;
                case "T":
                    return 18;

                case "u":
                    return 19;
                case "U":
                    return 19;

                case "w":
                    return 20;
                case "W":
                    return 20;

                case "x":
                    return 21;
                case "X":
                    return 21;

                case "y":
                    return 22;
                case "Y":
                    return 22;

                case "z":
                    return 23;
                case "Z":
                    return 23;
                default:
                    return 99;// jak 99 to koordynata nie znaleziona

            }
        }

        public int GetInt()
        {
            return Convert.ToInt32(Console.ReadLine()); //TODO: trzeba dodać odporność na błędy użytkownika jeżeli wprowadzi coś innego niż int
        }

        public string GetString()
        {
            return Console.ReadLine();
        }

        public void Pause()
        {
            Display display = new Display();
            display.Write("Push any button .. ");
            Console.ReadKey();
        }

    }
}