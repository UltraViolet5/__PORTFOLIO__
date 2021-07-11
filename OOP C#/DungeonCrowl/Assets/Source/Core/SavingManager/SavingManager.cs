using System.Collections.Generic;
using System.IO;
using System.Linq;
using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Items;
using DungeonCrawl.Core;
using Source.Actors.Characters;
using UnityEngine;
using Source.Actors.Items;
using Source.Core.EnemyStateMachine;
using Source.UI;
using UnityEngine.SceneManagement;

namespace Source.Core.SavingManager
{
    public class SavingManager : MonoBehaviour
    {
        private string _fileName = "SaveData.json";
        private string _savingPath;
        public static SavingManager Singleton { get; private set; }

        public bool HasSaveDataToLoad => LoadSaveFromFile() != null;

        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;
            _savingPath = Application.dataPath + "\\save";
            if (!Directory.Exists(_savingPath))
            {
                Directory.CreateDirectory(_savingPath);
            }
        }

        public void SaveGame()
        {
            WriteSaveToFile();
        }

        public void LoadGame()
        {
            SceneManager.sceneLoaded += OnSceneLoaded;
            SceneManager.LoadScene("Level1");
        }

        private void LoadSaveData()
        {
            Save save = LoadSaveFromFile();

            var dictOfItems = GenerateDictOfItemById();
            var player = ActorManager.Singleton.Player;

            // Player
            LoadPlayerAttributes(save, player);

            //Player Inventory
            LoadPlayerInventory(save, player, dictOfItems);

            // Player Equipment
            LoadPlayerEquipment(save, player, dictOfItems);

            //Characters
            LoadCharacters(save);

            //Items
            LoadItems(save, dictOfItems);

            // Camera
            Camera.main.transform.position = save.cameraPosition;

            // Refresh Inventory UI 
            InventoryManager.Singleton.Display();
            InventoryManager.Singleton.DisplayEquipment();
        }

        private void OnSceneLoaded(Scene scene, LoadSceneMode mode)
        {
            Debug.Log("OnSceneLoaded");
            LoadSaveData();
            MessageBox.Singleton.DisplayMessage("Game Loaded.");
            Debug.Log("Game loaded.");
            SceneManager.sceneLoaded -= OnSceneLoaded;
        }

        /// <summary>
        /// Read game state and return save object.
        /// </summary>
        /// <returns>State of the game.</returns>
        private Save GenerateSave()
        {
            Save save = new Save();
            // Save player data
            save.player = GeneratePlayerSaveData();

            // Save characters states
            save.characters = GenerateCharactersSaveData();

            // Save items states
            save.items = GenerateItemsSaveData();

            save.cameraPosition = Camera.main.transform.position;

            return save;
        }

        private List<CharactersSaveData> GenerateCharactersSaveData()
        {
            // Get items in scene and fill list by CharacterSaveData objects
            List<CharactersSaveData> charactersSaveDataList = new List<CharactersSaveData>();

            var characters = ActorManager.Singleton.AllCharacters;
            foreach (var character in characters)
            {
                CharactersSaveData characterSaveData = new CharactersSaveData(character);
                charactersSaveDataList.Add(characterSaveData);
            }

            return charactersSaveDataList;
        }

        private List<ItemsSaveData> GenerateItemsSaveData()
        {
            // Get items in scene and fill list by ItemSaveData objects

            var items = ActorManager.Singleton.AllItems;
            List<ItemsSaveData> itemsSaveDatas = new List<ItemsSaveData>();

            foreach (var item in items)
            {
                ItemsSaveData itemsSaveData = new ItemsSaveData(item);
                itemsSaveDatas.Add(itemsSaveData);
            }

            return itemsSaveDatas;
        }

        private PlayerSaveData GeneratePlayerSaveData()
        {
            var playerGameObject = GameObject.FindGameObjectWithTag("Player");
            Player player = playerGameObject.GetComponent<Player>();
            PlayerSaveData playerData = new PlayerSaveData(player);
            return playerData;
        }

        private Save LoadSaveFromFile()
        {
            string path = Path.Combine(_savingPath, _fileName);

            if (File.Exists(path))
            {
                string json = File.ReadAllText(path);
                Save save = JsonUtility.FromJson<Save>(json);
                return save;
            }

            Debug.LogError("Could not Open the file " + _fileName + "to read");
            return null;
        }

        private void WriteSaveToFile()
        {
            var json = JsonUtility.ToJson(GenerateSave());
            string path = Path.Combine(_savingPath, _fileName);

            File.WriteAllText(path, json);
        }

        private static void LoadItems(Save save, Dictionary<string, Item> dictOfItems)
        {
            foreach (var itemsSaveData in save.items)
            {
                var item = dictOfItems[itemsSaveData.id];
                item.Amount = itemsSaveData.amount;
                item.gameObject.SetActive(itemsSaveData.enabled);
            }
        }

        private void LoadCharacters(Save save)
        {
            var dictOfCharacter = GenerateDictOfCharacterById();
            foreach (var saveCharacter in save.characters)
            {
                var character = dictOfCharacter[saveCharacter.id];
                character.gameObject.SetActive(saveCharacter.enabled);
                character.Position = saveCharacter.position;
                character.CurrentHealth = saveCharacter.currentHealth;
            }
        }

        private static void LoadPlayerAttributes(Save save, Player player)
        {
            player.Position = save.player.position;
            player.CurrentHealth = save.player.currentHealth;
            player.MaxHealth = save.player.maxHealth;
        }

        private static void LoadPlayerInventory(Save save, Player player, Dictionary<string, Item> dictOfItems)
        {
            var inventoryObject = player.Inventory;

            foreach (var id in save.player.inventory)
            {
                inventoryObject.AddItem(dictOfItems[id]);
            }
        }

        private static void LoadPlayerEquipment(Save save, Player player, Dictionary<string, Item> dictOfItems)
        {
            if (!string.IsNullOrEmpty(save.player.equipment.armor))
                player.Equipment.Armor = dictOfItems[save.player.equipment.armor] as Armor;
            if (!string.IsNullOrEmpty(save.player.equipment.helmet))
                player.Equipment.Helmet = dictOfItems[save.player.equipment.helmet] as Helmet;
            if (!string.IsNullOrEmpty(save.player.equipment.weapon))
                player.Equipment.Weapon = dictOfItems[save.player.equipment.weapon] as Weapon;
        }

        public Dictionary<string, Item> GenerateDictOfItemById()
        {
            var items = ActorManager.Singleton.AllItems;
            Dictionary<string, Item> dict = new Dictionary<string, Item>();
            foreach (var item in items)
            {
                dict.Add(item.Id, item);
            }

            return dict;
        }

        public Dictionary<string, Character> GenerateDictOfCharacterById()
        {
            var characters = ActorManager.Singleton.AllCharacters;
            Dictionary<string, Character> dict = new Dictionary<string, Character>();

            foreach (var character in characters)
            {
                dict.Add(character.Id, character);
            }

            return dict;
        }
    }
}