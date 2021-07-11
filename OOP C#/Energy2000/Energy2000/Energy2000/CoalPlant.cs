using System;
using System.Collections.Generic;
using System.Text;

namespace Energy2000
{
    public class CoalPlant: IPlant
    {
        private ResourceStorage _resource;


        public int production()
        {
            IPlant.Resource.coal -= 100;
            return IPlant.Resource.energy += 7;
        }
    }

}
