


namespace CCOOPPA.Plants
{
    public class NuclearPlant : IWorkPlace
    {
        private int _get1 = 1;
        private int _produce1 = 10000;

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
            IWorkPlace.Resource.uranium -= _get1;
            IWorkPlace.Resource.energy += _produce1;
        }
    }
}