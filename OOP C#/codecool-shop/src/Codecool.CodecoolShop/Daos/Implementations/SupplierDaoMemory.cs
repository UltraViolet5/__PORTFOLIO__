using System.Collections.Generic;
using System.Linq;
using Codecool.CodecoolShop.Daos.Conte;
using Codecool.CodecoolShop.Models;

namespace Codecool.CodecoolShop.Daos.Implementations
{
    public class SupplierDaoMemory : ISupplierDao
    {
        private List<Supplier> data = new List<Supplier>();
        private static SupplierDaoMemory instance = null;


        private Context context { get; set; }


        public SupplierDaoMemory(Context context)
        {
            this.context = context;
        }
        //public static SupplierDaoMemory GetInstance()
        //{
        //    if (instance == null)
        //    {
        //        instance = new SupplierDaoMemory();
        //    }

        //    return instance;
        //}

        public void Add(Supplier item)
        {
            item.Id = context.Supplier.Count() + 1;
            context.Supplier.Add(item);
        }

        public void Remove(int id)
        {
            context.Supplier.Remove(this.Get(id));
        }

        public Supplier Get(int id)
        {
            return context.Supplier.Find(id);
        }

        public IEnumerable<Supplier> GetAll()
        {
            return context.Supplier.ToList();
        }
    }
}
