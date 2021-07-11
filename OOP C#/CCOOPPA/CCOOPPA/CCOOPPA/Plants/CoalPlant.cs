
using CCOOPPA.Resource;

namespace CCOOPPA.Plants
{
    public class CoalPlant : IWorkPlace
    {
        private int _get1 = 100;
        private int _produce1 = 7;

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
            IWorkPlace.Resource.coal -= _get1;
            IWorkPlace.Resource.energy += _produce1;
        }
    }

}