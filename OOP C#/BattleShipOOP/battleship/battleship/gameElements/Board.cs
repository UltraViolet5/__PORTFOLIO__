using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using battleship.gameElements;


namespace battleship
{
    public class Board
        {
        //public int[,] ocean; // to powinna być dwu wymiarowa tablica obiektów typu field
        public List<List<Field>> ocean;

        public Board(int size ) // konsturktor tworzy ocean czyli listę dwuwymiarową wypełnioną obiktami typu field
        {

            ocean = new List<List<Field>> { };
        
            for(int y = 0; y <= size - 1 ; y ++)
            {
                ocean.Add(new List<Field> {  });
                for (int x = 0; x <= size - 1; x++)
                {
                    ocean[y].Add(new Field(enums.SateOfField.Free, false));

                }
                
            }

        }

        public void PlaceShip(List<Ship> ShipList)
        {
            List<Coordinates> shipCoordList;

            foreach (Ship ship in  ShipList)
            {
                shipCoordList = ship.GetShipCoordinates();
                foreach( Coordinates coord in shipCoordList)
                {
                    ocean[coord.y][coord.x].ContainShip = true;

                }


            }


        }

    }
}
