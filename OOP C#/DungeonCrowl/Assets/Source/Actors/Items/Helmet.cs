using DungeonCrawl;
using Source.Actors.Characters;
using UnityEngine;

namespace Source.Actors.Items
{
    public class Helmet : Armor
    {
        public Helmet(string name, int protection) : base(name, protection)
        {
            this.Type = ItemType.Armor;
        }

        public override void Use()
        {
            Player player = GameObject.FindWithTag("Player").GetComponent<Player>();
            if (player.Equipment.Helmet == this)
            {
                player.Equipment.Helmet = null;
                player.Protection -= Protection;
            }
            else
            {
                player.Equipment.Helmet = this;
                player.Protection += Protection;
            }
        }
    }
}