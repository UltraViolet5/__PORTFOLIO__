namespace CCOOPPA.Mines
{
    public class CoalMine : IWorkPlace
    {
        private int _get1 = 0;
        private int _produce1 = 40;

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
            IWorkPlace.Resource.coal += _produce1;
        }
    }
}