using System;
using DungeonCrawl;
using UnityEngine;

namespace Source
{
    public static class Utilities
    {
        public static Vector2 ToVector(this Direction dir)
        {
            return dir switch
            {
                Direction.Up => new Vector2(0, 1),
                Direction.Down => new Vector2(0, -1),
                Direction.Left => new Vector2(-1, 0),
                Direction.Right => new Vector2(1, 0),
                Direction.UpLeft => new Vector2(-1, 1),
                Direction.UpRight => new Vector2(1, 1),
                Direction.DownLeft => new Vector2(-1, -1),
                Direction.DownRight => new Vector2(1, -1),
                _ => throw new ArgumentOutOfRangeException(nameof(dir), dir, null)
            };
        }
    }
}
