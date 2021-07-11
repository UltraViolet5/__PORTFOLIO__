using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Codecool.CodecoolShop.Daos.Conte;
using Codecool.CodecoolShop.Models;

namespace Codecool.CodecoolShop.Daos.Implementations
{
    public class ProductDaoMemory : IProductDao
    {
        private List<Product> data = new List<Product>();
        private static ProductDaoMemory instance = null;

        private Context context { get; set; }
        

        public ProductDaoMemory(Context context)
        {
            this.context = context;
        }

        //public static ProductDaoMemory GetInstance()
        //{
        //    if (instance == null)
        //    {
        //        instance = new ProductDaoMemory();
        //    }

        //    return instance;
        //}

        public void Add(Product item)
        {
            item.Id = context.Products.Count() + 1;
            context.Products.Add(item);
        }

        public void Remove(int id)
        {
            context.Products.Remove(this.Get(id));
        }

        public Product Get(int id)
        {
            return context.Products.Find(id);
        }

        public IEnumerable<Product> GetAll()
        {
            return context.Products.ToList();
        }

        public IEnumerable<Product> GetBy(Supplier supplier)
        {
            return context.Products.Where(x => x.Supplier.Id == supplier.Id);
        }

        public IEnumerable<Product> GetBy(ProductCategory productCategory)
        {
            return context.Products.Where(x => x.ProductCategory.Id == productCategory.Id);
        }
    }
}
