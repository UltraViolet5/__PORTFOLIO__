using System;
using DungeonCrawl.Core;
using Source;
using Source.Core;
using UnityEngine;

namespace DungeonCrawl.Actors
{
    public abstract class Actor : MonoBehaviour
    {
        [UniqueIdentifier] public string Id;
        [SerializeField] private string _name;
        public string Name
        {
            get => _name; 
            set => _name = value;
        }
      
        // Unity inspector params
        [SerializeField] private float _speed = 5;
      

        public float Speed
        {
            get => _speed;
            set => _speed = value;
        }

        public Sprite Sprite
        {
            get => _spriteRenderer.sprite;
            set => _spriteRenderer.sprite = value;
        }

        public Vector3 Position
        {
            get => transform.position;
            set => transform.position = value;
        }

        private SpriteRenderer _spriteRenderer;

        private void Awake()
        {
            _spriteRenderer = GetComponent<SpriteRenderer>();
            Position = new Vector3(Position.x, Position.y, Z);

            OnAwake();
        }

        private void Start()
        {
            OnStart();
        }

        private void Update()
        {
            OnUpdate(Time.deltaTime);
        }

        public virtual void Move()
        {
        }

        /// <summary>
        /// Move object to the destination
        /// </summary>
        /// <param name="targetPosition">Point 2D to move</param>
        public virtual void Move(Vector2 targetPosition)
        {
            Vector3 currentPosition = transform.position;

            Vector3 newPosition = Vector3.MoveTowards(currentPosition, targetPosition, Speed * Time.deltaTime);
            Position = newPosition;
        }

        /// <summary>
        /// Move in specific direction.
        /// </summary>
        /// <param name="direction">Enum Direction is the direction of movement.</param>
        public virtual void Move(Direction direction)
        {
            Vector2 vector = direction.ToVector();
            float xMovement = vector.x * Speed * Time.deltaTime;
            float yMovement = vector.y * Speed * Time.deltaTime;
            Vector3 newPosition = new Vector3(xMovement + Position.x,
                yMovement + Position.y,
                Position.z);
            Position = newPosition;
        }


        /// <summary>
        ///     Invoked every animation frame, can be used for movement, character logic, etc
        /// </summary>
        /// <param name="deltaTime">Time (in seconds) since the last animation frame</param>
        protected virtual void OnUpdate(float deltaTime)
        {
        }

        protected virtual void OnAwake()
        {
        }

        protected virtual void OnStart()
        {
        }

        /// <summary>
        ///     Z position of this Actor (0 by default)
        /// </summary>
        public virtual int Z => 0;

        /// <summary>
        ///     Default name assigned to this actor type
        /// </summary>
        public abstract string DefaultName { get; }
    }
}