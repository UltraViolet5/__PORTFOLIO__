using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Items;
using Source.Actors.Characters;
using Source.Core;
using Source.UI;
using UnityEngine;

namespace Source.Actors
{
    [RequireComponent(typeof(NPC))]
    public class ItemQuest : MonoBehaviour
    {
        public bool Completed { get; private set; }
        public GameObject itemToBring;
        public GameObject prize;
        public string newMessage;
        
        private Item _itemToBring;
        private NPC _self;

        private void Awake()
        {
            _itemToBring = itemToBring.GetComponent<Item>();
            _self = GetComponent<NPC>();
        }
        
        /// <summary>
        /// Complete a quest.
        /// </summary>
        /// <param name="player"></param>
        public void Complete(Player player)
        {
            if (!Completed && player.Inventory.HaveItem(_itemToBring.Id))
            {
                player.Inventory.RemoveItem(_itemToBring.Id);
                InventoryManager.Singleton.Display();
                Completed = true;
                _self.message = newMessage;
                GivePrize();
                _self.playSound = false;
            }
        }

        private void GivePrize()
        {
            prize.SetActive(true);
        }
    }
}
