namespace CCOOPPA.Plants
{
    public class SolarPlant : IWorkPlace
    {
        private int _get1=0;
        private int _produce1 = 2;

        int IWorkPlace._get
        {
            get => _get1;
            set => _get1 = value;
        }

        int IWorkPlace._produce
        {
            get => _produce1;
            set => _produce1 = value;
        }

        public void Production()
        {
            IWorkPlace.Resource.energy += _produce1;
        }
    }
}