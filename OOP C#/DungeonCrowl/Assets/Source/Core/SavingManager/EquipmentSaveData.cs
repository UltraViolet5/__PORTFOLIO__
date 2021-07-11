namespace Source.Core.SavingManager
{
    [System.Serializable]
    public class EquipmentSaveData
    {
        public string helmet;
        public string armor;
        public string weapon;

        public EquipmentSaveData(string helmet, string armor, string weapon)
        {
            this.helmet = helmet;
            this.armor = armor;
            this.weapon = weapon;
        }
    }
}