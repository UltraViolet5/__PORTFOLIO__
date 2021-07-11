using System;
using System.Collections.Generic;
using System.Text;

namespace Energy2000
{
    public class ResourceStorage
    {
        public int energy { get; set; }
        public int coal = 200;
        public int uranium { get; set; }
        public int hellium { get; set; }
        public int antimatter { get; set; }
        private static ResourceStorage _instance = null;
        public static ResourceStorage GetInstance()
        {
            if (_instance == null)
            {
                _instance = new ResourceStorage();
            }

            return _instance;
        }
    }
}
