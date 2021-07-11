using System;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace Source.UI
{
    public class AuthorsScreen : MonoBehaviour
    {
        public float timer = 5;

        private void Awake()
        {
            Cursor.visible = false;
        }

        // Update is called once per frame
        void Update()
        {
            if (timer > 0)
            {
                timer -= Time.deltaTime;
            }
            else
            {
                SceneManager.LoadScene("MainMenu");
            }
        }
    }
}