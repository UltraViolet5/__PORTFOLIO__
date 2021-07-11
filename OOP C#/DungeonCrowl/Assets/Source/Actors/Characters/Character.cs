using DungeonCrawl.Actors.Items;
using DungeonCrawl.Core;
using Source.Actors.Items;
using UnityEngine;

namespace DungeonCrawl.Actors.Characters
{
    public abstract class Character : Actor
    {
        public Inventory Inventory { get; private set; }
        public Equipment Equipment { get; private set; }

        [Header("Attributes")] [SerializeField]
        protected int _currentHealth;

        public virtual int CurrentHealth
        {
            get => _currentHealth;
            set => _currentHealth = value;
        }

        [SerializeField] protected int _maxHealth = 100;

        public virtual int MaxHealth
        {
            get => _maxHealth;
            set => _maxHealth = value;
        }

        [SerializeField] protected int _attack = 5;

        public virtual int Attack
        {
            get => _attack;
            set => _attack = value;
        }

        [SerializeField] protected int _protection = 5;

        public virtual int Protection
        {
            get => _protection;
            set => _protection = value;
        }

        private Sprite _idleSprite;

        public Sprite IdleSprite
        {
            get => _idleSprite;
            private set => _idleSprite = value;
        }

        protected Character()
        {
            Inventory = new Inventory();
        }

        public void ApplyDamage(int damage)
        {
            if (damage > this.Protection)
            {
                CurrentHealth -= damage - this.Protection;

                if (CurrentHealth <= 0)
                {
                    // Die
                    OnDeath();
                }
            }
        }

        public void Heal(int value)
        {
            CurrentHealth += value;
            CurrentHealth = Mathf.Clamp(_currentHealth, 0, _maxHealth);
        }


        protected abstract void OnDeath();

        /// <summary>
        ///     All characters are drawn "above" floor etc
        /// </summary>
        public override int Z => -1;

        protected override void OnAwake()
        {
            base.OnAwake();
            Equipment = new Equipment(this);
            _currentHealth = MaxHealth;
            IdleSprite = GetComponent<SpriteRenderer>().sprite;
        }
    }
}