using System;
using System.Dynamic;
using battleship.enums;

namespace battleship.gameElements
{
    public class Field
    {
        public SateOfField State { get; set; }
        public bool ContainShip { get; set; }
        public string Symbol
        {

            /*
            get
            {
                
                return this.State switch // myślę że funkcja powinna zwracać jedno znakowego stringa albo chara
                {
                    SateOfField.Free => "N",//"█",
                    SateOfField.Fired => "X",
                    SateOfField.Hit => "◙",
                    SateOfField.HitSunk => "☼",
                    _ => "█"
                };
            }
            */

            get{
                //string to_return = "";

                switch (State)
                {
                    case enums.SateOfField.Free:
                        return "F";
                        
                    case enums.SateOfField.Fired:
                        return "N";
                        
                    case enums.SateOfField.Hit:
                        return "H";
                        
                    case enums.SateOfField.HitSunk:
                        return "S"; 
                     
                    default:
                        return "W";
                }
            }
        }
  
        public Field( SateOfField state = enums.SateOfField.Free, bool containShip = false)
        {
            this.State = state;
            this.ContainShip = containShip;
        }
    }
}


