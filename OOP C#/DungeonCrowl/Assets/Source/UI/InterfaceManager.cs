using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using DungeonCrawl.Actors.Items;
using DungeonCrawl.Core;
using Source.Actors.Characters;
using Source.Core;
using Source.Core.SavingManager;
using Source.UI;
using UnityEditor;
using UnityEngine;
using UnityEngine.SceneManagement;

public class InterfaceManager : MonoBehaviour
{
    public GameObject QuickMenu;
    private GameObject _player;

    private void Awake()
    {
        _player = GameObject.FindWithTag("Player");
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            // (Quick menu) Display configuration and saving menu
            QuickMenu.SetActive(!QuickMenu.activeSelf);
            _player.GetComponent<Player>().enabled = !QuickMenu.activeSelf;
        }

        if (Input.GetKeyDown(KeyCode.I))
        {
            if (InventoryManager.Singleton.Activated)
                InventoryManager.Singleton.DeactivateInventory();
            else
                InventoryManager.Singleton.ActivateInventory();
        }

        if (Input.GetKeyDown(KeyCode.X))
        {
            foreach (var itemObject in ActorManager.Singleton.AllItems)
            {
                Debug.Log(itemObject.gameObject.name);
                Debug.Log(itemObject.Id);
                Debug.Log(itemObject.gameObject.activeInHierarchy);
            }
        }
    }
}