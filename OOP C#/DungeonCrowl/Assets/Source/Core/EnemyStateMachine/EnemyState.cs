using UnityEngine;

namespace Source.Core.EnemyStateMachine
{
    public abstract class EnemyState : State
    {
        protected EnemyStateMachine EnemyStateMachine { get; set; }
        protected Enemy Enemy { get; set; }
        public EnemyState(GameObject instance) : base(instance)
        {
        }
        
        public override void OnAwake()
        {
            base.OnAwake();
            EnemyStateMachine = Instance.GetComponent<EnemyStateMachine>();
            Enemy = Instance.GetComponent<Enemy>();
        }
    }
}