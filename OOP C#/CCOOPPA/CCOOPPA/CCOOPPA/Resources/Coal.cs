using System.Threading;

namespace CCOOPPA.Resources
{
    public struct Coal
    {
        public int coal;

        public Coal(int coal)
        {
            this.coal = coal;
        }

        public int getInSI()
        {
            /// in Tons
            return coal* 1000;
        }
    }
}