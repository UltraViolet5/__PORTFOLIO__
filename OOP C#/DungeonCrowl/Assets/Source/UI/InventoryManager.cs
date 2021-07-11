using System;
using System.Collections.Generic;
using DungeonCrawl.Actors.Items;
using DungeonCrawl.Core;
using Source.Actors.Characters;
using Source.Actors.Items;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

namespace Source.UI
{
    public class InventoryManager : MonoBehaviour
    {
        /// <summary>
        /// Item Prefab to spawn items representations in inventory.
        /// </summary>
        public GameObject UIItemPrefab;

        /// <summary>
        /// Item Prefab to spawn items representations in inventory. Contain item amount text value.
        /// </summary>
        public GameObject UIItemWithAmountPrefab;

        public static InventoryManager Singleton { get; private set; }
        private Inventory Inventory { get; set; }
        private List<GameObject> InventorySlots { get; set; }
        private GameObject HelmetSlot { get; set; }
        private GameObject ArmorSlot { get; set; }
        private GameObject WeaponSlot { get; set; }
        private GameObject LeftRoll { get; set; }
        private GameObject RightRoll { get; set; }

        /// <summary>
        /// True if we opened inventory, else false
        /// </summary>
        public bool Activated { get; private set; }

        private int SlotsCount { get; set; }


        /// <summary>
        /// Index of selected slot in inventory.
        /// </summary>
        private int SelectedSlot { get; set; }

        public Item SelectedItem
        {
            get
            {
                try
                {
                    return GetItem(SelectedSlot + _itemsOffset);
                }
                catch (Exception e)
                {
                    return null;
                }
            }
        }

        /// <summary>
        /// Slot frame size
        /// </summary>
        private float _slotSize;

        /// <summary>
        /// Slot frame size after selection.
        /// </summary>
        private const float SelectedSlotSize = 1;

        private GameObject _player;

        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;


            HelmetSlot = GameObject.FindWithTag("HelmetSlot");
            ArmorSlot = GameObject.FindWithTag("ArmorSlot");
            WeaponSlot = GameObject.FindWithTag("WeaponSlot");
            LeftRoll = GameObject.Find("LeftRoll");
            RightRoll = GameObject.Find("RightRoll");
            InventorySlots = new List<GameObject>();

            foreach (Transform child in GameObject.FindWithTag("InventorySlots").transform)
            {
                InventorySlots.Add(child.gameObject);
            }

            SlotsCount = InventorySlots.Count;

            _slotSize = InventorySlots[0].GetComponent<RectTransform>().localScale.x;
            _player = ActorManager.Singleton.Player.gameObject;
            _itemDescriptionText = GameObject.FindWithTag("ItemDescription").GetComponent<TextMeshProUGUI>();
            Inventory = _player.GetComponent<Player>().Inventory;

            Display();
        }

        private void Update()
        {
            if (Activated)
            {
                if (Input.GetKeyDown(KeyCode.A) || Input.GetKeyDown(KeyCode.LeftArrow))
                {
                    MoveSelectorLeft();
                    Display();
                }
                else if (Input.GetKeyDown(KeyCode.D) || Input.GetKeyDown(KeyCode.RightArrow))
                {
                    MoveSelectorRight();
                    Display();
                }
                else if (Input.GetKeyDown(KeyCode.E) || Input.GetKeyDown(KeyCode.Return))
                {
                    if (SelectedSlot + _itemsOffset < Inventory.Count)
                    {
                        Inventory.GetItem(SelectedSlot + _itemsOffset).Use();
                        Display();
                    }
                }
            }
        }

        /// <summary>
        /// Refresh inventory view.
        /// </summary>
        public void Display()
        {
            ClearAllInventorySlots();
            
            for (int i = 0; i < InventorySlots.Count; i++)
            {
                // Instantiate item icon and set correct image and amount value
                if (i < Inventory.Count - _itemsOffset)
                {
                    Item currentItem = GetItem(i + _itemsOffset);
                    GameObject gameObject = InstantiateIcon(InventorySlots[i], currentItem);
                    gameObject.transform.GetChild(0).GetComponent<TextMeshProUGUI>().text =
                        currentItem.Amount.ToString();
                }
                
                // Reset inventory size.
                InventorySlots[i].GetComponent<RectTransform>().localScale =
                    new Vector3(_slotSize, _slotSize, _slotSize);
            }

            if (Activated)
                SelectSlot();
            else
                DeselectSlot();

            DisplayScrollHints();
            DisplayDescription();
        }

        public GameObject InstantiateIcon(GameObject slot, Item item, bool withAmount = true)
        {
            GameObject gameObject;
            gameObject = Instantiate(withAmount ? UIItemWithAmountPrefab : UIItemPrefab, slot.transform);

            gameObject.GetComponent<Image>().sprite = item.Sprite;
            gameObject.GetComponent<RectTransform>().localPosition = new Vector3();
            return gameObject;
        }

        public void ActivateInventory()
        {
            Activated = true;
            _player.GetComponent<Player>().enabled = false;
            Display();
        }

        public void DeactivateInventory()
        {
            Activated = false;
            _player.GetComponent<Player>().enabled = true;
            Display();
        }

        /// <summary>
        /// Display equipped items.
        /// </summary>
        public void DisplayEquipment()
        {
            Player player = ActorManager.Singleton.Player;

            ClearSlot(ArmorSlot);
            ClearSlot(HelmetSlot);
            ClearSlot(WeaponSlot);

            if (player.Equipment.Weapon != null)
            {
                InstantiateIcon(WeaponSlot, player.Equipment.Weapon, false);
                EquipWeapon(ActorManager.Singleton.Player.gameObject, player.Equipment.Weapon);
            }

            if (player.Equipment.Helmet != null)
            {
                InstantiateIcon(HelmetSlot, player.Equipment.Helmet, false);
            }

            if (player.Equipment.Armor != null)
            {
                InstantiateIcon(ArmorSlot, player.Equipment.Armor, false);
            }
        }

        /// <summary>
        /// Display weapon.
        /// </summary>
        /// <param name="player">Player game object</param>
        /// <param name="weapon">Weapon to display</param>
        public void EquipWeapon(GameObject player, Weapon weapon)
        {
            Transform hand = player.transform.GetChild(0);
            foreach (Transform child in hand)
            {
                Destroy(child.gameObject);
            }

            GameObject weaponGO = CreateWeaponInstance(hand, weapon);

            weaponGO.transform.SetParent(hand, false);
            weaponGO.transform.localPosition = new Vector3(0.25f, 0.25f, 0f);
        }
        
        private GameObject CreateWeaponInstance(Transform parent, Weapon weapon)
        {
            GameObject weaponInstance = new GameObject();

            SpriteRenderer sr = weaponInstance.AddComponent<SpriteRenderer>();
            sr.sprite = weapon.Sprite;
            sr.sortingOrder = 4;

            return weaponInstance;
        }

        /// <summary>
        /// Get item from user inventory by index.
        /// </summary>
        /// <param name="index"></param>
        /// <returns>Index of item.</returns>
        private Item GetItem(int index)
        {
            return Inventory.GetItem(index);
        }

        /// <summary>
        /// Object in witch is displaying description.
        /// </summary>
        private TextMeshProUGUI _itemDescriptionText;

        /// <summary>
        /// Display selected item description.
        /// </summary>
        private void DisplayDescription()
        {
            if (Activated)
            {
                _itemDescriptionText.text = SelectedItem != null ? SelectedItem.ToString() : "";
            }
        }

        /// <summary>
        /// Display scrolling hints if you have more items than slots.
        /// </summary>
        private void DisplayScrollHints()
        {
            if (_itemsOffset > 0)
                LeftRoll.SetActive(true);
            else
                LeftRoll.SetActive(false);

            if (Inventory.Count > SlotsCount
                && _itemsOffset + SlotsCount - 1 < Inventory.Count - 1)
                RightRoll.SetActive(true);
            else
                RightRoll.SetActive(false);
        }

        /// <summary>
        /// Remove all icons from every slots.
        /// </summary>
        private void ClearAllInventorySlots()
        {
            foreach (var slot in InventorySlots)
            {
                ClearSlot(slot);
            }
        }

        /// <summary>
        /// Remove icon from slot.
        /// </summary>
        /// <param name="slot"></param>
        private void ClearSlot(GameObject slot)
        {
            foreach (Transform child in slot.transform)
            {
                Destroy(child.gameObject);
            }
        }

        private int _itemsOffset = 0;

        private void MoveSelectorLeft()
        {
            if (Inventory.Count > 0 && SelectedSlot == 0 && _itemsOffset == 0)
            {
                if (Inventory.Count < SlotsCount)
                {
                    SelectedSlot = Inventory.Count - 1;
                }
                else
                {
                    SelectedSlot = SlotsCount - 1;
                }
            }
            else if (_itemsOffset > 0 && SelectedSlot == 0)
            {
                _itemsOffset--;
            }
            else
            {
                SelectedSlot--;
            }
        }

        private void MoveSelectorRight()
        {
            if (Inventory.Count > 0)
            {
                if (SelectedSlot == SlotsCount - 1
                    && Inventory.Count > SlotsCount
                    && _itemsOffset + SelectedSlot < Inventory.Count - 1)
                {
                    _itemsOffset++;
                }
                else if (SelectedSlot == SlotsCount - 1 || SelectedSlot == Inventory.Count - 1)
                {
                    SelectedSlot = 0;
                }
                else
                {
                    SelectedSlot++;
                }
            }
        }

        /// <summary>
        /// Make bigger slot.
        /// </summary>
        private void SelectSlot()
        {
            InventorySlots[SelectedSlot].transform.localScale = new Vector3(SelectedSlotSize,
                SelectedSlotSize,
                SelectedSlotSize);
        }

        /// <summary>
        /// Make standard size slot.
        /// </summary>
        private void DeselectSlot()
        {
            InventorySlots[SelectedSlot].GetComponent<RectTransform>().localScale = new Vector3(_slotSize,
                _slotSize,
                _slotSize);
        }
    }
}