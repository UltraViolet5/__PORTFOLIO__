using System.Collections.Generic;
using Codecool.CodecoolShop.Daos;

using Codecool.CodecoolShop.Models;

namespace Codecool.CodecoolShop.Services
{
    public class ProductService
    {
        public readonly IProductDao productDao;
        public readonly IProductCategoryDao productCategoryDao;
        public readonly ISupplierDao supplierDao;


        public ProductService(IProductDao productDao, IProductCategoryDao productCategoryDao, ISupplierDao supplierDao)
        {
            this.productDao = productDao;
            this.productCategoryDao = productCategoryDao;
            this.supplierDao = supplierDao;
        }

        public ProductCategory GetProductCategory(int categoryId)
        {
            return this.productCategoryDao.Get(categoryId);
        }

        public Supplier GetProductSupplier(int categoryId)
        {
            return this.supplierDao.Get(categoryId);
        }

        public IEnumerable<Product> GetProductsForCategory(int categoryId)
        {
            ProductCategory category = this.productCategoryDao.Get(categoryId);
            return this.productDao.GetBy(category);
        }
        public IEnumerable<ProductCategory> GetAllProductCategory()
        {
            return this.productCategoryDao.GetAll();
        }
        public IEnumerable<Product> GetProductsForSupplier(int supplierId)
        {
            Supplier supplier = this.supplierDao.Get(supplierId);
            return this.productDao.GetBy(supplier);
        }

        public Product GetProduct(int id)
        {
           return this.productDao.Get(id);
        }


        public IEnumerable<Supplier> GetAllSuppliers()
        {
            return this.supplierDao.GetAll();
        }
        /*      public List<Supplier> GetListOfSuplliers()
              {
                  List<Supplier> listOfSuppliers = new List<Supplier>();
                  var listOfProduct = Daos.Implementations.ProductDaoMemory.GetInstance().GetAll();
                  foreach (var product in listOfProduct)
                  { 
                      listOfSuppliers.Add(product.Supplier);
                  }
                  //List<string> listOfSuppliersString = new List<string>();
                  //foreach (var supplier in listOfSuppliers)
                  //{
                  //    if (!listOfSuppliersString.Contains(supplier.Name))
                  //    {
                  //        listOfSuppliersString.Add(supplier.Name);
                  //    }
                  //}
                  return listOfSuppliers;
              }*/

        public void AddProduct(Product product)
        {
            productDao.Add(product);

        }

    }



}
