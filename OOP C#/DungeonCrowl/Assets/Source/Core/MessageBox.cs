using TMPro;
using UnityEngine;

namespace Source.Core
{
    public class MessageBox : MonoBehaviour
    {
        public float delay = 5;
        public GameObject messageBoxInstance;
        private float timer;

        public static MessageBox Singleton { get; private set; }

        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;

            timer = delay;
        }

        private void Update()
        {
            if (timer > 0)
            {
                timer -= Time.deltaTime;
            }
            else if (messageBoxInstance.activeSelf && timer <= 0)
            {
                messageBoxInstance.SetActive(false);
            }
        }

        public void DisplayMessage(string message)
        {
            timer = delay;
            messageBoxInstance.transform.GetChild(0).GetComponent<TextMeshProUGUI>().text = message;
            messageBoxInstance.SetActive(true);
        }
    }
}