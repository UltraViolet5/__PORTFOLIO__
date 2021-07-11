using System.Collections.Generic;
using Source.Actors.Characters;
using UnityEngine;

namespace Source.UI
{
    public abstract class Menu : MonoBehaviour
    {
        public int startSelectorPosition;
        public GameObject selector;
        
        protected List<GameObject> Options;
        
        protected int _selected;

        protected int Selected
        {
            get => _selected;
            private set
            {
                _selected = value;
                UpdateSelectorPosition();
            }
        }

        private void Awake()
        {
            Options = new List<GameObject>();
            foreach (Transform child in transform)
            {
                Options.Add(child.gameObject);
            }

            _selected = startSelectorPosition;
            
            UpdateSelectorPosition();
            OnAwake();
        }

        protected virtual void OnAwake()
        {
        }

        // Update is called once per frame
        void Update()
        {
            NavigateMenu();
        }

        protected void NavigateMenu()
        {
            if (Input.GetKeyDown(KeyCode.Return))
            {
                HandleOption();
            }
            else if (Input.GetKeyDown(KeyCode.W) || Input.GetKeyDown(KeyCode.UpArrow))
            {
                if (Selected > 0)
                    Selected--;
                else
                    Selected = Options.Count - 1;
            }
            else if (Input.GetKeyDown(KeyCode.S) || Input.GetKeyDown(KeyCode.DownArrow))
            {
                if (Selected < Options.Count - 1)
                    Selected++;
                else
                    Selected = 0;
            }
        }

        private void UpdateSelectorPosition()
        {
            selector.transform.position = Options[Selected].transform.position;
        }

        /// <summary>
        /// Define behaviour for menu buttons.
        /// </summary>
        protected abstract void HandleOption();
    }
}