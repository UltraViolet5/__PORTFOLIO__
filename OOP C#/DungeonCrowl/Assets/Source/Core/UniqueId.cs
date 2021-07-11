using System.Collections;
using UnityEngine;

namespace Source.Core
{
    // Placeholder for UniqueIdDrawer script
    public class UniqueIdentifierAttribute : PropertyAttribute {}
 
    public class UniqueId : MonoBehaviour {
        [UniqueIdentifier]
        public string uniqueId;
    }
}