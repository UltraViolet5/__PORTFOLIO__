using DungeonCrawl.Actors.Characters;
using Source.Core;
using Source.UI;

namespace Source.Actors.Items
{
    public class Equipment
    {
        /// <summary>
        /// Character witch have equipment instance.
        /// </summary>
        private Character _character;

        public Equipment(Character character)
        {
            _character = character;
        }

        private Armor _armor;

        public Armor Armor
        {
            get => _armor;
            set
            {
                if (value != null)
                {
                    if (_armor == null)
                    {
                        _character.Protection += value.Protection;
                    }
                    else
                    {
                        _character.Protection -= _armor.Protection;
                        _character.Protection += value.Protection;
                    }
                }
                else
                {
                    _character.Protection -= _armor.Protection;
                }

                _armor = value;
                InventoryManager.Singleton.DisplayEquipment();
            }
        }

        private Helmet _helmet;

        public Helmet Helmet
        {
            get => _helmet;
            set
            {
                if (value != null)
                {
                    if (_helmet == null)
                    {
                        _character.Protection += value.Protection;
                    }
                    else
                    {
                        _character.Protection -= _helmet.Protection;
                        _character.Protection += value.Protection;
                    }
                }
                else
                {
                    _character.Protection -= _helmet.Protection;
                }
                
                _helmet = value;
                InventoryManager.Singleton.DisplayEquipment();
            }
        }

        private Weapon _weapon;

        public Weapon Weapon
        {
            get => _weapon;
            set
            {
                if (value != null)
                {
                    if (_weapon == null)
                    {
                        _character.Attack += value.Damages;
                    }
                    else
                    {
                        _character.Attack -= _weapon.Damages;
                        _character.Attack += value.Damages;
                    }
                }
                else
                {
                    _character.Attack -= _weapon.Damages;
                }
                
                _weapon = value;
                InventoryManager.Singleton.DisplayEquipment();
            }
        }
    }
}