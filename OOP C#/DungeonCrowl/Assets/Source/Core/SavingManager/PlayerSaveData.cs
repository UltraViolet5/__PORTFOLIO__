using System.Collections.Generic;
using DungeonCrawl.Actors.Items;
using Source.Actors.Characters;
using UnityEngine;


namespace Source.Core.SavingManager
{
    [System.Serializable]
    public class PlayerSaveData
    {
        public Vector3 position;
        public int currentHealth;
        public int maxHealth;

        /// <summary>
        /// Id's of the items
        /// </summary>
        public List<string> inventory;

        /// <summary>
        /// Id's of the items
        /// </summary>
        public EquipmentSaveData equipment;

        public PlayerSaveData(Player player)
        {
            position = player.Position;
            currentHealth = player.CurrentHealth;
            maxHealth = player.MaxHealth;
            inventory = new List<string>();
            foreach (Item item in player.Inventory.GetItems())
            {
                inventory.Add(item.Id);
            }

            equipment = new EquipmentSaveData(
                player.Equipment.Helmet == null ? "" : player.Equipment.Helmet.Id,
                player.Equipment.Armor == null ? "" : player.Equipment.Armor.Id,
                player.Equipment.Weapon == null ? "" : player.Equipment.Weapon.Id
            );
        }
    }
}