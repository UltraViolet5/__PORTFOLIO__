using System;
using System.Collections.Generic;
using System.Text;
using restaurant.Model;
using static restaurant.utils.Utils;
using restaurant.Controller;
using Action = restaurant.Controller.Action;
using System.Linq;

namespace restaurant.Model
{
    public class Waiters: Man
    {
        public Order order { get; set; }

        public Waiters(string name) : base(name)
        {
            
        }

        public override Order GetOrder(int Peoples, int Staff)
        {
            int GuestId = GetRandom(Staff + 1, Peoples + 1);
            Action action = Action.GetInstance();
            order = action.Orders.Find(x => x.GuestId == GuestId);
            return action.Orders.Find(x => x.GuestId == GuestId);

        }
    }
}
