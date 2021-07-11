namespace CCOOPPA
{
    public interface IWorkPlace 
    {
        protected static ResourceStorage Resource => ResourceStorage.GetInstance();
        
        protected int _get { get; set; }
        protected int _produce { get; set; }

        public  abstract  void Production();
    }
}