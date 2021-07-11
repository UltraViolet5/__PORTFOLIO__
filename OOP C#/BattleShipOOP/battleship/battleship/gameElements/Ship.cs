using System.Collections.Generic;
using System.Linq;
using battleship.enums;


namespace battleship.gameElements
{
    public class Ship
    {
        private int QuantityOfMast { get; set; }

        public Players Player { get; set; }

        public Coordinates Place { get; set; } 

        private Position Position { get; set; }

        


        public Ship(int quantityOfMast, Players player, Coordinates place, Position position)
        {
            this.QuantityOfMast = quantityOfMast;
            this.Player = player;
            this.Place = place;
            this.Position = position;
        }

        public List<Coordinates> GetShipCoordinates()
        {
            List<Coordinates> coordinates = new List<Coordinates> {this.Place};
            
            switch (Position)
            {
                case Position.Horizontal:

                    for (int i = 1; i < this.QuantityOfMast; i++)
                    {
                        Coordinates newCoordinates = Place;
                        newCoordinates.x += i ;
                        coordinates.Add(newCoordinates);
                    }

                    return coordinates;

                case Position.Vertical:
                    for (int i = 1; i < this.QuantityOfMast; i++)
                    {
                        Coordinates newCoordinates = Place;
                        newCoordinates.y += i ;
                        coordinates.Add(newCoordinates);
                    }

                    return coordinates;
                default:
                    return coordinates;
            }
        }
    }
}