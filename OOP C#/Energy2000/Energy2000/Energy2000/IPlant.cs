namespace Energy2000
{
    public interface IPlant
    {
        protected static ResourceStorage Resource => ResourceStorage.GetInstance();
    }
}