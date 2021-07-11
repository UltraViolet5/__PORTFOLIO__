using System;
using System.Collections.Generic;
using System.Linq;
using DungeonCrawl.Actors.Items;
using Source.Core;

namespace Source.Actors.Items
{
    public class Inventory
    {
        private List<Item> _content;

        private List<Item> Content
        {
            get => _content;
            set => _content = value;
        }

        public int Count => Content.Count;

        public Inventory()
        {
            Content = new List<Item>();
        }

        public bool HaveItem(string id)
        {
            try
            {
                Content.First(item => item.Id == id);
                return true;
            }
            catch (InvalidOperationException e)
            {
                return false;
            }
        }

        public void RemoveItem(string id)
        {
            Content.Remove(GetItem(id));
        }

        public void RemoveItem(Item item)
        {
            Content.Remove(item);
        }

        public Item GetItem(string id)
        {
            return Content.First(i => i.Id == id);
        }

        public Item GetItem(int index)
        {
            return Content[index];
        }

        public void AddItem(Item item)
        {
            Content.Add(item);
        }

        public List<Item> GetItems()
        {
            return Content;
        }
    }
}