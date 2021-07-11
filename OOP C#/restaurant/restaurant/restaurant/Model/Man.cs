using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;

namespace restaurant.Model
{
    public abstract class Man
    {
        protected int Id { get; set; }
        public string Name { get; }

        private static int CounterId = 0;

        public Man(string name)
        {
            CounterId += 1;
            Id = CounterId;
            Name = name;
        }

        public abstract Order GetOrder(int Peoples, int Staff);
    }
}
