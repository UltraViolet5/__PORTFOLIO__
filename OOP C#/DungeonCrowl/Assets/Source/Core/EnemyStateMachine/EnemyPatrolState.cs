using System;
using DungeonCrawl;
using UnityEngine;
using Random = System.Random;

namespace Source.Core.EnemyStateMachine
{
    public class EnemyPatrolState : EnemyState
    {
        private GameObject[] PatrolPoints { get; set; }
        
        /// <summary>
        /// Current patrol point.
        /// </summary>
        private GameObject Target { get; set; }
        private int TargetIndex { get; set; } = 0;
        private float MovementTolerance { get; } = 0.3f;

        public EnemyPatrolState(GameObject instance) : base(instance)
        {
        }

        public override void OnUpdate()
        {
            base.OnUpdate();
            
            float distanceToTarget = Vector2.Distance(Instance.transform.position, Target.transform.position);

            if (distanceToTarget >= MovementTolerance)
            {
                this.Enemy.Move(Target.transform.position);
            }
            else
            {
                int chanceToChangeState = new Random().Next(1, 11);
                if (chanceToChangeState < 4)
                    this.EnemyStateMachine.CurrentState = this.EnemyStateMachine.IdleState;
                
                TargetIndex = TargetIndex + 1 < PatrolPoints.Length ? ++TargetIndex : 0;
                Target =  PatrolPoints[TargetIndex];
            }
        }

        public override void OnAwake()
        {
            base.OnAwake();
            PatrolPoints = Instance.GetComponent<Enemy>().PatrolPoints;
            Target = PatrolPoints[TargetIndex];
        }

        public override void OnEnter()
        {
            base.OnEnter();
            // Debug.Log($"{Enemy.name} - Enter patrol state.");
            Enemy.CurrentState = CharacterState.Patrol;
        }
    }
}