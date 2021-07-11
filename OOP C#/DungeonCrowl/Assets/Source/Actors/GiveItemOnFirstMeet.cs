using System.Collections.Generic;
using DungeonCrawl.Actors.Characters;
using UnityEngine;

namespace Source.Actors
{
    public class GiveItemOnFirstMeet : MonoBehaviour
    {
        public List<GameObject> itemsToGive;

        public void GivItem()
        {
            foreach (GameObject item in itemsToGive)
            {
                item.SetActive(true);
            }
            Destroy(gameObject.GetComponent<GiveItemOnFirstMeet>());
        }
    }
}
