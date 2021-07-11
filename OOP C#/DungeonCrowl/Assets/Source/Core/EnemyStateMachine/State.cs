using DungeonCrawl.Actors.Characters;
using UnityEngine;

namespace Source.Core.EnemyStateMachine
{
    public abstract class State : IState
    {
        public GameObject Instance { get; set; }

        public State(GameObject instance)
        {
            Instance = instance;
        }
        public virtual void OnUpdate()
        {
        }

        public virtual void OnAwake()
        {
        }

        public virtual void OnEnter()
        {
        }

        public virtual void OnExit()
        {
        }
    }
}