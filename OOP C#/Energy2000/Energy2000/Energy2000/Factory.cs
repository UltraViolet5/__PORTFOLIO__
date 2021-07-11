using System;
using System.Runtime.InteropServices.ComTypes;

namespace Energy2000
{
    public class Factory 

    {
        public static T GenerateFacility<T>() where T : IPlant, new()
        {
            return new T();
        }

        public int? GetEnum(Enum1 par)
        {
            switch (par)
            {
                case Enum1.kot:
                    return 1;
                case Enum1.pies:
                    return null;
                case Enum1.czlowiek:
                    return null;
                default:
                    throw new ArgumentOutOfRangeException(nameof(par), par, null);
            }
        }
    }

}