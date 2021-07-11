using Codecool.CodecoolShop.Models;
using Microsoft.EntityFrameworkCore;
using DbContext = Microsoft.EntityFrameworkCore.DbContext;

namespace Codecool.CodecoolShop.Daos.Conte
{
    public class Context: DbContext
    {
        public Microsoft.EntityFrameworkCore.DbSet<Product> Products { get; set; }
        public Microsoft.EntityFrameworkCore.DbSet<ProductCategory> ProductCategory { get; set; }
        public Microsoft.EntityFrameworkCore.DbSet<Supplier> Supplier { get; set; }
        public Context(DbContextOptions<Context>opt) : base(opt)
        {

        }
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Product>().Property(e => e.DefaultPrice).HasPrecision(38, 18);
        }
    }
}