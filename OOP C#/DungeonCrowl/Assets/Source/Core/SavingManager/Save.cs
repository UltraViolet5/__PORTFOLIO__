using System.Collections.Generic;
using UnityEngine;

namespace Source.Core.SavingManager
{
    [System.Serializable]
    public class Save
    {
        public PlayerSaveData player;
        public List<CharactersSaveData> characters;
        public List<ItemsSaveData> items;
        public Vector3 cameraPosition;
    }
}