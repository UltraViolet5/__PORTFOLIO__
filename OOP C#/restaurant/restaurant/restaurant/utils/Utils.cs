using System;
using System.Collections.Generic;
using System.Text;

namespace restaurant.utils
{
    static class Utils
    {
        public static int GetRandom(int min, int max)
        {
            Random random = new Random();
            var number =random.Next(min, max);
            return number;
        }
    }
}
