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
    public class Chef: Man
    {
        public List<Order> ChefOrder { get; set; }

        public Chef(string name) : base(name)
        {

        }

        public override Order GetOrder(int Peoples, int Staff)
        {
            
            Action action = Action.GetInstance();
             
            foreach (var waiter in action.ListWaiters)
            {
                action.chef.ChefOrder.Add(waiter.order);
            }


        }
    }
}
