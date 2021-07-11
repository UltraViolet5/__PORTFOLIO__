using System;
using DungeonCrawl.Actors.Characters;
using Source.Actors.Characters;
using TMPro;
using UnityEngine;

namespace Source.Core
{
    public class StatisticsUpdater : MonoBehaviour
    {
        /// <summary>
        ///     ActorManager singleton
        /// </summary>
        public static StatisticsUpdater Singleton { get; private set; }

        private Player Player { get; set; }
        
        
        private GameObject HealthText { get; set; }
        private GameObject AttackText { get; set; }
        private GameObject ProtectionText { get; set; }
        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;
            
            HealthText = GameObject.FindWithTag("HealthStatText");
            AttackText = GameObject.FindWithTag("AttackStatText");
            ProtectionText = GameObject.FindWithTag("ProtectionStatText");
            this.Player = GameObject.FindWithTag("Player").GetComponent<Player>();
        }

        private void Start()
        {
            Display();
        }
        
        public void Display()
        {
            HealthText.GetComponent<TextMeshProUGUI>().text = $"Health: {Player.CurrentHealth}/{Player.MaxHealth}";
            AttackText.GetComponent<TextMeshProUGUI>().text = $"Attack: {Player.Attack}";
            ProtectionText.GetComponent<TextMeshProUGUI>().text = $"Protection: {Player.Protection}";
        }
    }
}