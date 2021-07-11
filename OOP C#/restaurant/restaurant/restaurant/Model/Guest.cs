using System;
using System.Collections.Generic;
using System.Text;
using static restaurant.utils.Utils;

namespace restaurant.Model
{
    class Guest: Man
    {
        public Order order { get; set; }

        public Guest(string name):base(name)
        {
            order = new Order(this.Id);
        }

        //public override Order GetOrder(int Peoples, int Staff)
        //{
        //    int GuestId = GetRandom(Staff + 1, Peoples+1);

        //    return order;

        //}
        G
    }
}
