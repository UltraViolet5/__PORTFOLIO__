using DungeonCrawl;
using UnityEngine;

namespace Source.Core.EnemyStateMachine
{
    public class EnemyIdleState : EnemyState
    {
        private float Delay { get; } = 5;
        private float Timer { get; set; }


        public EnemyIdleState(GameObject instance) : base(instance)
        {
            Timer = Delay;
        }

        public override void OnUpdate()
        {
            Timer -= Time.deltaTime;

            base.OnUpdate();
            if (Timer <= 0)
            {
                EnemyStateMachine.CurrentState = EnemyStateMachine.PatrolState;
            }
        }

        public override void OnEnter()
        {
            base.OnEnter();
            // Debug.Log($"{Enemy.name} - Enter Idle State");
            Enemy.CurrentState = CharacterState.Idle;
            Timer = Delay;
        }
    }
}