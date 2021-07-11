using System;
using UnityEngine;

namespace DungeonCrawl.Core
{
    /// <summary>
    ///     Class used for manipulating camera's position
    /// </summary>
    public class CameraController : MonoBehaviour
    {
        public float followingSpeed = 5;
        public float offsetX = 0;
        public float offsetY = 0;
        
        /// <summary>
        ///     CameraController singleton
        /// </summary>
        public static CameraController Singleton { get; private set; }
        

        /// <summary>
        ///     Camera's size (how much space can it see)
        /// </summary>
        public float Size
        {
            get => _camera.orthographicSize;
            set => _camera.orthographicSize = value;
        }

        private (int x, int y) _position;
        private Camera _camera;
        private GameObject _player;

        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;

            _camera = GetComponent<Camera>();
        }

        private void Start()
        {
            _player = GameObject.FindGameObjectWithTag("Player");
        }

        private void Update()
        {
            FollowPlayer();
        }

        private void FollowPlayer()
        {
            Vector3 playerPosition = _player.transform.position;
            Vector3 cameraPosition = transform.position;

            Vector3 targetPosition = new Vector3(playerPosition.x + offsetX, playerPosition.y + offsetY, cameraPosition.z);
            Vector3 newPosition = Vector3.MoveTowards(cameraPosition, targetPosition, followingSpeed * Time.deltaTime);

            transform.position = newPosition;
        }
    }
}
