using System.Collections.Generic;
using System.Linq;
using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Items;
using Source.Actors.Characters;
using Source.Core.SavingManager;
using UnityEngine;
using UnityEngine.U2D;

namespace DungeonCrawl.Core
{
    /// <summary>
    ///     Main class for Actor management - spawning, destroying, detecting at positions, etc
    /// </summary>
    public class ActorManager : MonoBehaviour
    {
        /// <summary>
        ///     ActorManager singleton
        /// </summary>
        public static ActorManager Singleton { get; private set; }

        private List<Character> _allCharaacters;
        public List<Character> AllCharacters { get => _allCharaacters; private set => _allCharaacters = value; }
        private List<Item> _allItems;
        public List<Item> AllItems { get => _allItems; private set => _allItems = value; }
        private Player _player;
        public Player Player { get => _player; private set => _player = value; }

        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;

            AllCharacters = new List<Character>();
            AllItems = new List<Item>();

            Player = GameObject.FindWithTag("Player").GetComponent<Player>();
            foreach (Transform child in GameObject.FindWithTag("AllCharacters").transform)
            {
                if (child.CompareTag("Character"))
                {
                    AllCharacters.Add(child.GetComponent<Character>());
                }
            }

            foreach (Transform child in GameObject.FindWithTag("AllItems").transform)
            {
                AllItems.Add(child.GetComponent<Item>());
            }
        }
    }
}