namespace CCOOPPA.Resource
{
    public struct Uranium 
    {
        public int uranium;

        public Uranium (int uranium)
        {
            this.uranium = uranium;
        }

        public int getInSI()
        {
            /// in KG
            return uranium * 100;
        }
    }
}