using System.Collections.Generic;

namespace CCOOPPA.Factory
{
    public static  class WorkplaceFactory
    {
        public static List<T> Factory<T>(int Loop) where T: IWorkPlace,new()
        {
            List<T>  listWorkPlaces = new List<T>();
            for (int i = 0; i < Loop; i++)
            {
                T workplace = new T();
                listWorkPlaces.Add(workplace);
            }

            return listWorkPlaces;
            
        }
    }
}