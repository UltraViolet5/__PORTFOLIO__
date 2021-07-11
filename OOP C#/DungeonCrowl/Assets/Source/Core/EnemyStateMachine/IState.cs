using DungeonCrawl.Actors.Characters;
using UnityEngine;

namespace Source.Core.EnemyStateMachine
{
    public interface IState
    {
        GameObject Instance { get; set; }
        public void OnUpdate();
        public void OnAwake();
        public void OnEnter();
        public void OnExit();
    }
}