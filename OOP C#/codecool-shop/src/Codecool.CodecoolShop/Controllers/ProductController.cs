using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Codecool.CodecoolShop.Daos;
using Codecool.CodecoolShop.Daos.Conte;
using Codecool.CodecoolShop.Daos.Implementations;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Codecool.CodecoolShop.Models;
using Codecool.CodecoolShop.Services;
using Codecool.CodecoolShop.Helpers;
using Newtonsoft;
using Newtonsoft.Json;

namespace Codecool.CodecoolShop.Controllers
{
    public class ProductController : Controller
    {
        private readonly ILogger<ProductController> _logger;
        public ProductService ProductService { get; set; }

        public ProductController(ILogger<ProductController> logger, Context context)
        {
            _logger = logger;
            ProductService = new ProductService(
                new ProductDaoMemory(context),
                new ProductCategoryDaoMemory(context),
                new SupplierDaoMemory(context));


        }

        
        
        
        public IActionResult Index(int categoryNumber = 1)
        {
            
            var products = ProductService.GetProductsForCategory(categoryNumber);

            //product category
            var list = ProductService.GetAllProductCategory().ToList<ProductCategory>();
            ViewData["ListCategory"] = list;
            
            // product suppliers
            var listOfSuppliers = ProductService.GetAllSuppliers().ToList<Supplier>();
            ViewData["listOfSuppliers"] = listOfSuppliers;
            if (SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart") != null)
            {
                var cart = SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart");
                ViewBag.cart = cart;
                ViewBag.total = cart.Sum(item => item.product.DefaultPrice * item.Quantity);
                ViewBag.Quantity = cart.Sum(item => item.Quantity);
            }
            else
            {
                ViewBag.cart = null;
                ViewBag.total = 0;
                ViewBag.Quantity = 0;
            }

            return View(products.ToList());
        }
  
        [HttpGet]
        public IActionResult Index(string supplier, string category = "1")
        {
            
            var CategoryNr = int.Parse(category);
            //product category
            var list = ProductService.GetAllProductCategory().ToList();
            ViewData["ListCategory"] = list;
            // product suppliers
            var listOfSuppliers = ProductService.GetAllSuppliers().ToList();
            ViewData["listOfSuppliers"] = listOfSuppliers;
            if (SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart") != null)
            {
                var cart = SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart");
                ViewBag.cart = cart;
                ViewBag.total = cart.Sum(item => item.product.DefaultPrice * item.Quantity);
                ViewBag.Quantity = cart.Sum(item => item.Quantity);
            }
            else
            {
                ViewBag.cart = null;
                ViewBag.total = 0;
                ViewBag.Quantity = 0;
            }
            if (supplier != null)
            {
                var SupplierNr = int.Parse(supplier);
                var products = ProductService.GetProductsForSupplier(SupplierNr);
                return View(products);
            }
            else
            {
                var products = ProductService.GetProductsForCategory(CategoryNr);
               /* List<Product> entitylist = new List<Product>(products);
                var  nowalista = entitylist.ToList();*/
                return View(products.ToList());
            }
            
        }

        [HttpPost]
        public IActionResult AddProduct([FromBody] string product)
        {

            var values = product;
            var productjson = JsonConvert.DeserializeObject<Product>(product);


          /*  product.Supplier = ProductService.GetProductSupplier(1);
            product.ProductCategory = ProductService.GetProductCategory(1);

            ProductService.AddProduct(product);*/


            return Json(new { Status = "success" });
            }

        /*[HttpPost]
        public IActionResult AddProduct(Product product)
        {
            Console.WriteLine(product);
            product.Supplier = ProductService.GetProductSupplier(1);
            product.ProductCategory = ProductService.GetProductCategory(1);

            *//*ProductService.AddProduct(product);*//*
           
            Console.WriteLine(product.Name);


            return Json(product);
        }*/

        public IActionResult AddP()
        {
            return View("AddP");
        }
        
        public IActionResult Buy(int id)
        {
            //var id = int.Parse(stringid);
            if (SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart") == null)
            {
                List<LineItem> cart = new List<LineItem>();
                cart.Add(new LineItem { product = ProductService.GetProduct(id), Quantity = 1 });
                SessionHelper.SetObjectAsJson(HttpContext.Session, "cart", cart);
            }
            else
            {
                List<LineItem> cart = SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart");
                int index = isExist(id);
                if (index != -1)
                {
                    cart[index].Quantity++;
                }
                else
                {
                    cart.Add(new LineItem { product = ProductService.GetProduct(id), Quantity = 1 });
                }
                SessionHelper.SetObjectAsJson(HttpContext.Session, "cart", cart);
            }
            return RedirectToAction("Index");
        }

        [Route("cart")]
        public IActionResult Cart()
        {
            var cart = SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart");
            ViewBag.cart = cart;
            ViewBag.total = cart.Sum(item => item.product.DefaultPrice * item.Quantity);
            ViewBag.Quantity = cart.Sum(item => item.Quantity);
            return View("cart");
        }

        public IActionResult Quantity()
        {
            var cart = SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart");
            var stringValues = Request.Form;
            var count1 = cart.Count;
            var count2 = stringValues["q"].Count;
            List<LineItem> ClearedCart = new List<LineItem>();
            for (int i = 0; i < count1; i++)
            {
                var intValues = Int16.Parse(stringValues["q"][i]);
                cart[i].Quantity = intValues;
                if (cart[i].Quantity != 0)
                {
                    ClearedCart.Add(cart[i]);
                }
            }
            SessionHelper.SetObjectAsJson(HttpContext.Session, "cart", ClearedCart);
            var Checkout = new Checkout();
            //ViewBag.q = cart;
            return View("Checkout", Checkout);
        }


        private int isExist(int id)
        {
            List<LineItem> cart = SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart");
            for (int i = 0; i < cart.Count; i++)
            {
                if (cart[i].product.Id.Equals(id))
                {
                    return i;
                }
            }
            return -1;
        }

        
        public IActionResult Privacy()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Payment(Checkout checkout)
        {
            SessionHelper.SetObjectAsJson(HttpContext.Session, "checkout", checkout);
            List<LineItem> cart = SessionHelper.GetObjectFromJson<List<LineItem>>(HttpContext.Session, "cart");
            ViewBag.total = cart.Sum(item => item.product.DefaultPrice * item.Quantity);
            return View("Payment");
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
