using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Items;
using Source.Actors.Characters;
using UnityEngine;

namespace Source.Actors.Items
{
    public class Weapon : Item
    {
        [SerializeField] private int _damages = 1;

        public int Damages
        {
            get => _damages;
            set => _damages = value;
        }

        public Weapon(string name, int damages) : base(name)
        {
            Damages = damages;
        }

        public override void Use()
        {
            Player player = GameObject.FindWithTag("Player").GetComponent<Player>();
            if (player.Equipment.Weapon == this)
            {
                player.Equipment.Weapon = null;
                Unequip(player.gameObject);
            }
            else
            {
                player.Equipment.Weapon = this;
            }
        }

        /// <summary>
        /// Remove weapon representation from player object.
        /// </summary>
        /// <param name="player">Player game object.</param>
        private void Unequip(GameObject player)
        {
            Transform hand = player.transform.GetChild(0);
            foreach (Transform child in hand)
            {
                Destroy(child.gameObject);
            }
        }

        // TODO Remove this, moved this to 
        // /// <summary>
        // /// Display weapon.
        // /// </summary>
        // /// <param name="player">Player game object</param>
        // public void Equip(GameObject player)
        // {
        //     Transform hand = player.transform.GetChild(0);
        //     foreach (Transform child in hand)
        //     {
        //         Destroy(child.gameObject);
        //     }
        //
        //     GameObject weapon = CreateWeaponInstance(hand);
        //
        //     weapon.transform.SetParent(hand, false);
        //     weapon.transform.localPosition = new Vector3(0.25f, 0.25f, 0f);
        // }
        //
        // private GameObject CreateWeaponInstance(Transform parent)
        // {
        //     GameObject weaponInstance = new GameObject();
        //
        //     SpriteRenderer sr = weaponInstance.AddComponent<SpriteRenderer>();
        //     sr.sprite = Sprite;
        //     sr.sortingOrder = 4;
        //
        //     return weaponInstance;
        // }

        public override string ToString()
        {
            return $"{Name}\nDamage: {Damages.ToString()}";
        }
    }
}