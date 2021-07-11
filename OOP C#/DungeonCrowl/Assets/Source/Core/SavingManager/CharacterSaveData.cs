using DungeonCrawl.Actors.Characters;
using UnityEngine;

namespace Source.Core.SavingManager
{
    [System.Serializable]
    public class CharactersSaveData
    {
        public string id;
        public bool enabled;
        public Vector3 position;
        public int currentHealth;
        
        public CharactersSaveData(Character character)
        {
            id = character.Id;
            enabled = character.gameObject.activeSelf;
            position = character.Position;
            currentHealth = character.CurrentHealth;
        }
    }
}