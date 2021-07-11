using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Flying : MonoBehaviour
{
    public float speed = 1;
    public float ampithude = 1;
    private float sin;
    
    
    // Update is called once per frame
    void Update()
    {
        sin = Mathf.Sin(Time.realtimeSinceStartup * 0.5f  * speed) * ampithude;
        transform.position += new Vector3(0, sin * Time.deltaTime);
    }
}
