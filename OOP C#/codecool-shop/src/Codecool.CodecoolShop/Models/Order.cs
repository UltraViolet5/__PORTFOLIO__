using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Codecool.CodecoolShop.Models
{
    public class Order
    {
        public Checkout checkout { get; set; }

        public List<LineItem> Cart { get; set; }

    }
}
