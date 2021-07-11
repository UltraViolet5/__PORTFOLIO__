using UnityEngine;

namespace DungeonCrawl.Actors.Characters
{
    public class Skeleton : Character
    {
        protected override void OnDeath()
        {
            Debug.Log("Well, I was already dead anyway...");
        }

        public override string DefaultName => "Skeleton";
    }
}
