using System;

namespace battleship
{
    class Program
    {
        static void Main(string[] args)
        {
            Display display = new Display();
            Input input = new Input();

            while(true) 
            {
                display.Clear();
                display.Menu(enums.DisplayText.WelcomeGraphic);
                display.Menu(enums.DisplayText.WelcomeMenu);
            
                switch(input.GetInt())
                {
                    case 1:
                        Game game = new Game();
                        break;
                    case 2:
                        display.Write("Function not available"); //Start singleplayer game win AI 
                        input.Pause();
                        break;
                    case 3:
                        display.Clear();
                        display.Menu(enums.DisplayText.InfoAboutGame);
                        input.Pause();
                        break;
                    case 4:
                        System.Environment.Exit(0);
                        break;
                }
            }
        }
    }
}