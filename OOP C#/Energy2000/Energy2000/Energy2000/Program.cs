using System;
namespace Energy2000
{
    class Program
    {
        static void Main(string[] args)
        {
            CoalPlant plant = new CoalPlant();
            for (int i = 0; i < 15; i++)
            {
                plant.production();
                Console.WriteLine(ResourceStorage.GetInstance().energy);
                Console.WriteLine(ResourceStorage.GetInstance().coal);
            }
            
            
        }
    }
}
