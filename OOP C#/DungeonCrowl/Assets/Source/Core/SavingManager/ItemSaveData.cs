using DungeonCrawl.Actors.Items;

namespace Source.Core.SavingManager
{
    [System.Serializable]
    public class ItemsSaveData
    {
        public string id;
        public bool enabled;
        public int amount;

        public ItemsSaveData(Item item)
        {
            this.id = item.Id;
            this.enabled = item.gameObject.activeSelf;
            this.amount = item.Amount;
        }
    }
}