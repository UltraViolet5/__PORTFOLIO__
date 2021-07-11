using System;
using Source.Core.SavingManager;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace Source.UI
{
    public class MainMenu : Menu
    {
        protected override void HandleOption()
        {
            switch (Selected)
            {
                case 0:
                    SceneManager.LoadScene("Level1");
                    break;
                case 1:
                    if (SavingManager.Singleton.HasSaveDataToLoad)
                        SavingManager.Singleton.LoadGame();
                    break;
                case 2:
                    Application.Quit();
                    break;
            }
        }

        private void OnEnable()
        {
            TextMeshProUGUI text = Options[1].GetComponent<TextMeshProUGUI>();
            if (SavingManager.Singleton.HasSaveDataToLoad)
                text.color = new Color(text.color.r, text.color.g, text.color.b, 1);
            else
                text.color = new Color(text.color.r, text.color.g, text.color.b, 0.5f);
        }
    }
}