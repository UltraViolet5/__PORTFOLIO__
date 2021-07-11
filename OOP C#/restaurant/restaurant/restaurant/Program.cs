using System;
using System.Security.Cryptography.X509Certificates;
using restaurant.utils;
using restaurant.Controller;
using Action = restaurant.Controller.Action;


namespace restaurant
{
    class Program
    {
        static void Main(string[] args)
        {
            Action action = Action.GetInstance();
            action.StartRestaurant(2,6);


        }
            
        }
    }
}
