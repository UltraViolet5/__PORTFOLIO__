using System;
using System.Collections.Generic;
using System.Text;
using restaurant.Model;
using restaurant.Peoples;

namespace restaurant.Controller
{
    public class Action
    {
        public List<Order> Orders = new List<Order>();
        public List<Waiters> ListWaiters = new List<Waiters>();
        private static Action _instance = null;
        public int Waiters { get; set; }
        public int Guests { get; set; }
        public Chef chef { get; set; }
        private Action()
        {

        }
        public static Action GetInstance()
        {
            if (_instance == null)
            {
                _instance = new Action();
            }

            return _instance;
        }


        public void StartRestaurant(int InputWaiters, int InputGuests)
        {
            Waiters = InputWaiters;
            Guests = InputGuests;
            chef = new Chef("Kucharek");
            for (int i = 1; i < Waiters; i++)
            {
                Waiters waiter = new Waiters($"John{i}");
                ListWaiters.Add(waiter);
            }
            for (int i = 1; i < Guests; i++)
            {
                Guest guest = new Guest($"John + {i}");
                Orders.Add(guest.order);
            }
        }

        public Order InteracionTime()
        {
            int Staff = Waiters + 1;
            int Peoples = Waiters + Guests + 1;
            foreach (var waiter in ListWaiters)
            { 
                waiter.GetOrder(Peoples, Staff);
            }
            
        }
        public Order CheedInteraction
    }

}
