using UnityEngine;

namespace DungeonCrawl.Actors
{
    public interface ISelectable
    {
        /// <summary>
        /// Activate item interaction.
        /// </summary>
        /// <param name="owner">Object which activate item.</param>
        public void Activate(GameObject owner);
    }
}