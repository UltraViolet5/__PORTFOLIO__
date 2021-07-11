using System;
using DungeonCrawl.Actors;
using Source.Actors;
using UnityEngine;

namespace Source.InteractiveItems
{
    public class Chest : MonoBehaviour, ISelectable
    {
        public Sprite openedChest;
        public Sprite closedChest;
        
        private bool _isOpened;

        private bool isOpened
        {
            get => _isOpened;
            set
            {
                _isOpened = value;
                UpdateSprite();
            }
        }

        public void Activate(GameObject owner)
        {
            GetComponent<GiveItemOnFirstMeet>()?.GivItem();
            isOpened = true;
        }

        private void Start()
        {
            UpdateSprite();
        }

        private void UpdateSprite()
        {
            GetComponent<SpriteRenderer>().sprite = _isOpened ? openedChest : closedChest;
        }

        public override string ToString()
        {
            return "Chest";
        }
    }
}