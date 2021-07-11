using UnityEngine;

namespace Source.Actors
{
    [RequireComponent(typeof(SpriteRenderer))]
    public class FlippingSprite : MonoBehaviour
    {
        // Inspector variables
        public bool x = true;
        public bool y = true;
        public float flippingDelay = 0.5f;
        private SpriteRenderer _sr { get; set; }
        private float Timer { get; set; }
        
        private void Awake()
        {
            _sr = GetComponent<SpriteRenderer>();
            Timer = flippingDelay;
        }

        // Update is called once per frame
        void Update()
        {
            if (Timer > 0)
            {
                Timer -= Time.deltaTime;
            }
            else
            {
                Timer = flippingDelay;
                if (x)
                    _sr.flipX = !_sr.flipX;
                if (y)
                    _sr.flipY = !_sr.flipY;
            }
        }
    }
}
