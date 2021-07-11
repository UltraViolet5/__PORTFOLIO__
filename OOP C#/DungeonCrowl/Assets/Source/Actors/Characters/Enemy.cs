using System;
using DungeonCrawl;
using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Characters;
using Source.Core.EnemyStateMachine;
using UnityEngine;

[RequireComponent(typeof(EnemyStateMachine))]
public class Enemy : Character, ISelectable 
{
    [Header("State machine")]
    public CharacterState CurrentState = CharacterState.Idle;
    public GameObject[] PatrolPoints;
    public Sprite AttackSprite;
    public float attackDelay = 1;

    public override string DefaultName { get; }

    
    protected override void OnDeath()
    {
        Debug.Log($"Enemy - {name} is dead.");
        gameObject.SetActive(false);
    }

    public void Activate(GameObject owner)
    {
        Character character = owner.GetComponent<Character>();
        
        if (character.Equipment.Weapon != null)
        {
            ApplyDamage(character.Attack);
            if (CurrentHealth <= 0)
            {
                OnDeath();
            }    
        }
    }

    public override string ToString()
    {
        return $"{Name}\nLive:{CurrentHealth.ToString()}/{MaxHealth.ToString()}";
    }
}
