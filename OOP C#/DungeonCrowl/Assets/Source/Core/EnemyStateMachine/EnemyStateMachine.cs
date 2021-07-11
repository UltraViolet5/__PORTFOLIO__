using System.Collections;
using System.Collections.Generic;
using UnityEngine;

namespace Source.Core.EnemyStateMachine
{
    [RequireComponent(typeof(Enemy))]
    public class EnemyStateMachine : StateMachine
    {
        public EnemyIdleState IdleState { get; set; }
        public EnemyPatrolState PatrolState { get; set; }
        public EnemyChaseState ChaseState { get; set; }
        public EnemyAttackState AttackState { get; set; }

        public List<GameObject> VisibleCharacters
        {
            get => GetComponent<CharacterDetector>().visibleCharacters;
        }

        public GameObject Opponent
        {
            get
            {
                foreach (GameObject character in VisibleCharacters)
                {
                    if (character.CompareTag("Player"))
                    {
                        return character;
                    }
                }

                return null;
            }
        }

        public float? DistanceToOpponent
        {
            get
            {
                if (Opponent != null)
                {
                    return Vector2.Distance(transform.position, Opponent.transform.position);
                }

                return null;
            }
        }

        protected override void OnAwake()
        {
            base.OnAwake();
            IdleState = new EnemyIdleState(gameObject);
            PatrolState = new EnemyPatrolState(gameObject);
            ChaseState = new EnemyChaseState(gameObject);
            AttackState = new EnemyAttackState(gameObject);

            IdleState.OnAwake();
            PatrolState.OnAwake();
            ChaseState.OnAwake();
            AttackState.OnAwake();

            CurrentState = IdleState;
        }

        protected override void OnUpdate()
        {
            base.OnUpdate();
            CurrentState.OnUpdate();

            if (Opponent != null && CurrentState != AttackState)
            {
                CurrentState = ChaseState;
            }
        }
    }
}