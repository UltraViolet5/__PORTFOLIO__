using System.Runtime.InteropServices.ComTypes;

namespace Codecool.CodecoolShop.Models
{
    public class LineItem
    {
        public int Quantity { get; set; }
        public Product product { get; set; }

    }
}