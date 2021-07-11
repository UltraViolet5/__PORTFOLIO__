using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Items;
using Source.Actors.Items;
using Source.Core;
using UnityEngine;

namespace Source.Actors.Characters
{
    public class Player : Character
    {
        private Rigidbody2D _rb;

        public override int CurrentHealth
        {
            get => _currentHealth;
            set
            {
                _currentHealth = value;
                StatisticsUpdater.Singleton.Display();
            }
        }

        public override int MaxHealth
        {
            get => _maxHealth;
            set
            {
                _maxHealth = value;
                StatisticsUpdater.Singleton.Display();
            }
        }

        public override int Attack
        {
            get => _attack;
            set
            {
                _attack = value;
                StatisticsUpdater.Singleton.Display();
            }
        }

        public override int Protection
        {
            get => _protection;
            set
            {
                _protection = value;
                StatisticsUpdater.Singleton.Display();
            }
        }

        private Transform Hand { get; set; }
        private AudioSource _audioSource;

        protected override void OnAwake()
        {
            base.OnAwake();
            _rb = GetComponent<Rigidbody2D>();
            _audioSource = GetComponent<AudioSource>();
            Hand = transform.GetChild(0);
        }

        protected override void OnUpdate(float deltaTime)
        {
            Move();
            ActivateSelected();
            AttackOpponent();
        }

        private void AttackOpponent()
        {
            if (Equipment.Weapon != null)
                Hand.localRotation = Input.GetKey(KeyCode.E)
                    ? Quaternion.Euler(0, 0, -30)
                    : Quaternion.Euler(0, 0, 0);

            // If we have equipped weapon and character (With component Character) is selected.
            if (Equipment.Weapon != null &&
                GetComponent<ItemDetector>().SelectedItem?.GetComponent<ISelectable>() is Enemy)
            {
                if (Input.GetKeyDown(KeyCode.E))
                {
                    // Play music
                    _audioSource.clip = GetComponent<PlayerInteractionAudios>().fight;
                    _audioSource.Play();
                }
            }
        }

        private void ActivateSelected()
        {
            if (Input.GetKeyDown(KeyCode.E) || Input.GetKeyDown(KeyCode.Return))
            {
                GetComponent<ItemDetector>().Activate();
            }
        }

        public override void Move()
        {
            Vector2 movement = new Vector2();

            if (Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow))
            {
                // Move up
                movement.y = 1;
            }

            if (Input.GetKey(KeyCode.S) || Input.GetKey(KeyCode.DownArrow))
            {
                // Move down
                movement.y = -1;
            }

            if (Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow))
            {
                // Move left
                movement.x = -1;
            }

            if (Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow))
            {
                // Move right
                movement.x = 1;
            }

            movement = movement.normalized;
            _rb.MovePosition(_rb.position + movement * Speed * Time.deltaTime);
        }

        protected override void OnDeath()
        {
            Debug.Log("Oh no, I'm dead!");
        }

        public override string DefaultName => "Player";

        public bool CheckIfOwnKey(Key key)
        {
            foreach (Item item in this.Inventory.GetItems())
            {
                if (item is Key && item == key)
                {
                    return true;
                }
            }

            return false;
        }
    }
}