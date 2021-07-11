using UnityEngine;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using Source.Actors.Characters;

namespace Source.Core.SavingManager
{
    public static class SaveSystem
    {
        public static void SavePlayer(Player player)
        {
            BinaryFormatter formatter = new BinaryFormatter();
            string path = Application.persistentDataPath + "save.fun";
            FileStream stream = new FileStream(path, FileMode.Create);

            PlayerSaveData data = new PlayerSaveData(player);
            
            formatter.Serialize(stream, data);
            stream.Close();
        }

        public static PlayerSaveData LoadData()
        {
            string path = Application.persistentDataPath + "save.fun";
            if (File.Exists(path))
            {
                BinaryFormatter formatter = new BinaryFormatter();
                FileStream stream = new FileStream(path, FileMode.Open);

                PlayerSaveData data = (PlayerSaveData)formatter.Deserialize(stream);
                stream.Close();
                
                return data;
            }
            else
            {
                Debug.LogError("Save file not found in " + path);
                return null;
            }
        }
    }
}