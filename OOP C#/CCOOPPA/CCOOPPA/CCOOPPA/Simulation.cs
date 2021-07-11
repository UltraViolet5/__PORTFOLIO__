using System.Collections.Generic;
using CCOOPPA.Factory;
using CCOOPPA.Mines;
using CCOOPPA.Plants;

namespace CCOOPPA
{
    public class Simulation
    {
        public List<CoalMine> CoalMines;
        public List<NuclearPlant> NuclearPlants;
        public List<SolarPlant> SolarPlants;
        public List<UraniumMine> UraniumMines;
        public List<CoalPlant> CoalPlants;
        public int? CPlantCount;
        public int? NPlantCount;
        public int? UMineCount;
        public int? CMineCount;
        public int? SolarPlantCount;
        
        
        public Simulation(int? nPlant, int? cPlant, int? sPlant, int? uMines, int? cMines)
        {
            CMineCount = cMines;
            NPlantCount = nPlant;
            UMineCount = uMines;
            CPlantCount = cPlant;
            SolarPlantCount = sPlant;
        }

        public void CreateWorkPlaces()
        {
            this.CoalPlants = WorkplaceFactory.Factory<CoalPlant>(CPlantCount);
            this.NuclearPlants = WorkplaceFactory.Factory<NuclearPlant>(NPlantCount);
            this.CoalMines = WorkplaceFactory.Factory<CoalMine>(CMineCount);
            this.SolarPlants = WorkplaceFactory.Factory<SolarPlant>(SolarPlantCount);
            this.UraniumMines = WorkplaceFactory.Factory<UraniumMine>(UMineCount);
        }
        
        public void CreatResource<T>(List<T> resources) where T : IWorkPlace
        {
            foreach (var resours in resources)
            {
                resours.Production();
            }
        }
    }
}