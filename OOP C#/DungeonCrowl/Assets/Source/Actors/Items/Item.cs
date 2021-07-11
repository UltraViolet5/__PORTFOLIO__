using UnityEngine;
using DungeonCrawl.Actors.Characters;
using Source.Actors.Items;
using Source.Core;
using Source.UI;

// ReSharper disable All

namespace DungeonCrawl.Actors.Items
{
    public class Item : MonoBehaviour, ISelectable, IUsable
    {
        [UniqueIdentifier] public string Id;
        [SerializeField] private string _name;
        public string Name
        {
            get => _name;
            set => _name = value;
        }

        public ItemType Type { get; set; }

        [SerializeField] private int _value = 1;

        public int Value
        {
            get => _value;
            set => _value = value;
        }

        [SerializeField] private int _amount = 1;

        public int Amount
        {
            get => _amount;
            set => _amount = value;
        }

        public Sprite Sprite { get; private set; }

        public Item(string name)
        {
            this.Name = name;
            this.Type = ItemType.Other;
        }

        private void Awake()
        {
            this.Sprite = GetComponent<SpriteRenderer>().sprite;
            OnAwake();
        }
        public void Activate(GameObject owner)
        {
            PickUp(owner);
        }
        public void PickUp(GameObject inventoryOwner)
        {
            if (!IncrementAmoutIfExistInInventory(inventoryOwner))
            {
                inventoryOwner.GetComponent<Character>().Inventory.AddItem(this);
            }

            this.gameObject.SetActive(false);

            InventoryManager.Singleton.Display();
            MessageBox.Singleton.DisplayMessage($"I picked up {Amount}x {Name}! :)");
        }

        /// <summary>
        /// Increment amout of item if exist in inventory.
        /// </summary>
        /// <param name="owner">Inventory owner.</param>
        /// <returns>If found the same item in inventory return true, else false.</returns>
        private bool IncrementAmoutIfExistInInventory(GameObject owner)
        {
            Inventory inventory = owner.GetComponent<Character>().Inventory;
            foreach (Item item in inventory.GetItems())
            {
                if (item.Name == this.Name)
                {
                    item.Amount += this.Amount;
                    return true;
                }
            }

            return false;
        }

        protected virtual void OnAwake()
        {
        }

        public virtual void Use()
        {
            Debug.Log("Item used...");
        }

        public override string ToString()
        {
            return Name;
        }
    }
}