using DungeonCrawl;
using UnityEngine;

namespace Source.Core.EnemyStateMachine
{
    public class EnemyChaseState : EnemyState
    {
        public EnemyChaseState(GameObject instance) : base(instance)
        {
        }


        public override void OnEnter()
        {
            base.OnEnter();
            // Debug.Log($"{Enemy.name} - Enter chase state");
            Enemy.CurrentState = CharacterState.Chase;
        }

        public override void OnUpdate()
        {
            base.OnUpdate();

            if (EnemyStateMachine.Opponent == null)
            {
                EnemyStateMachine.CurrentState = EnemyStateMachine.IdleState;
            }
            else
            {
                if (EnemyStateMachine.DistanceToOpponent > 1.2f)
                {
                    Enemy.Move(EnemyStateMachine.Opponent.transform.position);
                }
                else
                {
                    EnemyStateMachine.CurrentState = EnemyStateMachine.AttackState;
                }
            }
        }
    }
}