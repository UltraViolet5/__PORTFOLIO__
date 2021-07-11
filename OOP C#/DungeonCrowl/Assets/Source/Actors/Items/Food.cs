using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Items;
using Source.Actors.Characters;
using UnityEngine;

namespace Source.Actors.Items
{
    public class Food : Item
    {
        [SerializeField] private int _healing;

        public int Healing
        {
            get => _healing;
            set => _healing = value;
        }

        public Food(string name, int healing) : base(name)
        {
            Healing = healing;
        }

        public override void Use()
        {
            Player player = GameObject.FindWithTag("Player").GetComponent<Player>();
            player.Heal(Healing);
            player.Inventory.RemoveItem(this);
        }

        public override string ToString()
        {
            return $"{Name}\nHealing {Healing}";
        }
    }
}