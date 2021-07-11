using System.Collections;
using System.Collections.Generic;
using DungeonCrawl.Actors.Items;
using NUnit.Framework;
using Source.Actors.Characters;
using Source.Actors.Items;
using UnityEngine;
using UnityEngine.TestTools;

public class InventoryTests
{
    // Arrange
    public Player _player;
    public Item _item;

    [SetUp]
    public void SetUp()
    {
        GameObject player = new GameObject("Player",
            typeof(SpriteRenderer),
            typeof(Rigidbody2D));
        GameObject hand = new GameObject("Hand", typeof(SpriteRenderer));
        hand.transform.parent = player.transform;
        player.AddComponent<Player>();
        _player = player.GetComponent<Player>();

        GameObject item = new GameObject("Item",
            typeof(SpriteRenderer),
            typeof(Item));
        _item = item.GetComponent<Item>();
    }

    // // A Test behaves as an ordinary method
    // [Test]
    // public void TestAddingItemToPlayerInventory()
    // {
    //     // Act
    //     _player.Inventory.AddItem(_item);
    //
    //     // Assert
    //     Assert.AreEqual(_item.Id, _player.Inventory.GetItem(_item.Id).Id);
    // }

    // A UnityTest behaves like a coroutine in Play Mode. In Edit Mode you can use
    // `yield return null;` to skip a frame.
    [UnityTest]
    public IEnumerator TestAddingItemToPlayerInventory()
    {
        // Act
        _player.Inventory.AddItem(_item);

        // Assert
        Assert.AreEqual(_item.Id, _player.Inventory.GetItem(_item.Id).Id);
        // Use yield to skip a frame.
        yield return null;
    }
    
    [UnityTest]
    public IEnumerator TestRemovingItemFromPlayerInventory()
    {
        // Arrange
        _player.Inventory.AddItem(_item);
        
        // Act
        _player.Inventory.RemoveItem(_item);
        
        // Assert
        Assert.AreEqual(0, _player.Inventory.Count);
        // Use yield to skip a frame.
        yield return null;
    }
    
    [UnityTest]
    public IEnumerator TestRemovingItemFromPlayerInventoryById()
    {
        // Arrange
        _player.Inventory.AddItem(_item);
        
        // Act
        _player.Inventory.RemoveItem(_item.Id);
        
        // Assert
        Assert.AreEqual(0, _player.Inventory.Count);
        // Use yield to skip a frame.
        yield return null;
    }

    [UnityTest]
    public IEnumerator TestIfInventoryHaveNotItem()
    {
        // Arrange
        // Act
        // Assert
        Assert.IsFalse(_player.Inventory.HaveItem(_item.Id));
        // Use yield to skip a frame.
        yield return null;
    }
    
    [UnityTest]
    public IEnumerator TestIfInventoryHaveItem()
    {
        // Arrange
        _player.Inventory.AddItem(_item);
        // Act
        // Assert
        Assert.IsTrue(_player.Inventory.HaveItem(_item.Id));
        // Use yield to skip a frame.
        yield return null;
    }
    
    [UnityTest]
    public IEnumerator TestGetItemFromInventoryByIndex()
    {
        // Arrange
        _player.Inventory.AddItem(_item);
        
        // Act
        Item gotItem = _player.Inventory.GetItem(0);
        
        // Assert
        Assert.AreEqual(_item.Id, gotItem.Id);
        // Use yield to skip a frame.
        yield return null;
    }
    
    [UnityTest]
    public IEnumerator TestGetItemFromInventoryById()
    {
        // Arrange
        _player.Inventory.AddItem(_item);
        
        // Act
        Item gotItem = _player.Inventory.GetItem(_item.Id);
        
        // Assert
        Assert.AreEqual(_item.Id, gotItem.Id);
        // Use yield to skip a frame.
        yield return null;
    }

    [UnityTest]
    public IEnumerator TestGetItems()
    {
        // Arrange
        Item item1 = new GameObject("Item1",
            typeof(SpriteRenderer),
            typeof(Item)).GetComponent<Item>();
        Item item2 = new GameObject("Item2",
            typeof(SpriteRenderer),
            typeof(Item)).GetComponent<Item>();
        Item item3 = new GameObject("Item3",
            typeof(SpriteRenderer),
            typeof(Item)).GetComponent<Item>();
        _player.Inventory.AddItem(item1);
        _player.Inventory.AddItem(item2);
        _player.Inventory.AddItem(item3);
        
        // Act
        List<Item> items = _player.Inventory.GetItems();
        
        // Assert
        Assert.AreEqual(3, items.Count);
        yield return null;
    }
}