using System.Collections;
using System.Collections.Generic;
using DungeonCrawl;
using DungeonCrawl.Actors.Characters;
using Source.Actors;
using UnityEngine;

namespace Source.Core.EnemyStateMachine
{
    public class EnemyAttackState : EnemyState
    {
        public float Timer { get; set; }

        private AudioSource _audioSource;

        public EnemyAttackState(GameObject instance) : base(instance)
        {
        }

        public override void OnEnter()
        {
            base.OnEnter();

            Debug.Log($"{Enemy.name} - Enter Attack state.");
            Enemy.CurrentState = CharacterState.Attack;
            Timer = 0;
        }

        public override void OnUpdate()
        {
            base.OnUpdate();
            if (EnemyStateMachine.DistanceToOpponent > 1.4f)
            {
                if (EnemyStateMachine.Opponent != null)
                    EnemyStateMachine.CurrentState = EnemyStateMachine.ChaseState;
                else
                    EnemyStateMachine.CurrentState = EnemyStateMachine.IdleState;
            }

            if (Timer >= 0)
                Timer -= Time.deltaTime;
            else
            {
                _audioSource.Play();
                SetAttackSprite();
                _audioSource.Play();
                EnemyStateMachine.Opponent.GetComponent<Character>().ApplyDamage(Enemy.Attack);
                Timer = Enemy.attackDelay;
            }
        }

        /// <summary>
        /// Set attack sprite and after 0.5 s. return idle sprite.
        /// </summary>
        public void SetAttackSprite()
        {
            SpriteRenderer sr = Enemy.gameObject.GetComponent<SpriteRenderer>();

            sr.sprite = Enemy.AttackSprite;
            sr.flipX = false;
            sr.flipY = false;
            FlippingSprite flippingSprite = Enemy.gameObject.GetComponent<FlippingSprite>();
            if (flippingSprite != null)
                flippingSprite.enabled = false;


            IEnumerator coroutine = ReturnIdleSprite();
            EnemyStateMachine.StartCoroutine(coroutine);
        }

        private IEnumerator ReturnIdleSprite()
        {
            yield return new WaitForSeconds(0.4f);

            SpriteRenderer sr = Enemy.gameObject.GetComponent<SpriteRenderer>();
            sr.sprite = Enemy.IdleSprite;
            FlippingSprite flippingSprite = Enemy.gameObject.GetComponent<FlippingSprite>();
            if (flippingSprite != null)
                flippingSprite.enabled = true;
        }

        public override void OnAwake()
        {
            base.OnAwake();
            _audioSource = EnemyStateMachine.GetComponent<AudioSource>();
        }
    }
}