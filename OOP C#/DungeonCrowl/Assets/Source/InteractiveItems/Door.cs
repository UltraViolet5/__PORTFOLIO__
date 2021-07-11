using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Characters;
using Source.Actors.Characters;
using Source.Actors.Items;
using Source.Core;
using UnityEngine;

// ReSharper disable All

namespace Source.InteractiveItems
{
    public class Door : MonoBehaviour, ISelectable
    {
        [SerializeField] private Sprite _closeSprite;

        public Sprite CloseSprite
        {
            get => _closeSprite;
            set => _closeSprite = value;
        }

        [SerializeField] private Sprite _openSprite;

        public Sprite OpenSprite
        {
            get => _openSprite;
            set => _openSprite = value;
        }

        private SpriteRenderer _spriteRenderer;
        private AudioSource _audioSource;

        private void Awake()
        {
            _spriteRenderer = GetComponent<SpriteRenderer>();
            _spriteRenderer.sprite = CloseSprite;

            _audioSource = GetComponent<AudioSource>();

            Key = GetComponent<Door>().KeyGameObject.GetComponent<Key>();
        }

        [SerializeField] private bool _isLock = false;

        public bool IsLock
        {
            get => _isLock;
            set => _isLock = value;
        }

        private bool _isOpen = false;

        public bool IsOpen
        {
            get => _isOpen;
            set => _isOpen = value;
        }

        public GameObject KeyGameObject;
        
        private Key _key;

        private Key Key
        {
            get => _key;
            set => _key = value;
        }

        public void Open()
        {
            IsOpen = true;
            _spriteRenderer.sprite = OpenSprite;
            GetComponent<Collider2D>().isTrigger = true;
            // Play sound.
            _audioSource.Play();
        }

        public void Close()
        {
            IsOpen = false;
            _spriteRenderer.sprite = CloseSprite;
            GetComponent<Collider2D>().isTrigger = false;
            // Play sound.
            _audioSource.Play();
        }

        public void Unlock()
        {
            GameObject player = GameObject.FindWithTag("Player");
            Player p = player.GetComponent<Player>();
            if (p.CheckIfOwnKey(this.Key))
            {
                MessageBox.Singleton.DisplayMessage("Correct key!");
                IsLock = false;
                Open();
                // Play sound
                _audioSource.Play();
            }
            else
            {
                MessageBox.Singleton.DisplayMessage("I need a key!");
            }
        }

        public void Activate(GameObject owner)
        {
            if (IsLock)
                Unlock();
            else
            {
                if (IsOpen)
                    Close();
                else
                    Open();
            }
        }

        public override string ToString()
        {
            return "Door";
        }
    }
}