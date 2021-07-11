using System;
using Source.Actors;
using Source.Actors.Characters;
using Source.Core;
using UnityEngine;

namespace DungeonCrawl.Actors.Characters
{
    public class NPC : Character, ISelectable
    {
        // Inspector configuration
        public String message = "Some message...";
        public bool playSound = true;

        public override string DefaultName { get; } = "NPC_";

        private AudioSource _audioSource;
        private ItemQuest _quest;
        protected override void OnDeath()
        {
            throw new System.NotImplementedException();
        }

        public void Activate(GameObject owner)
        {
            _quest.Complete(owner.GetComponent<Player>());
            MessageBox.Singleton.DisplayMessage(message);
            if (playSound)
                _audioSource.Play();
            GetComponent<GiveItemOnFirstMeet>()?.GivItem();
        }

        protected override void OnAwake()
        {
            base.OnAwake();
            _audioSource = GetComponent<AudioSource>();
            _quest = GetComponent<ItemQuest>();
        }

        public override string ToString()
        {
            return $"{Name}";
        }
    }
}