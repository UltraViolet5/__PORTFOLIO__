using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterDetector : MonoBehaviour
{
    [SerializeField] private bool _xRay;

    public bool XRay
    {
        get => _xRay;
        set => _xRay = value;
    }

    [SerializeField] private LayerMask _visionMask;

    public LayerMask VisionMask
    {
        get => _visionMask;
        set => _visionMask = value;
    }

    public List<GameObject> visibleCharacters;

    [SerializeField] private float _viewDistance;

    public float ViewDistance
    {
        get => _viewDistance;
        set => _viewDistance = value;
    }

    private void OnTriggerStay2D(Collider2D other)
    {
        if (other.CompareTag("Character") || other.CompareTag("Player"))
        {
            RaycastHit2D hit;
            if (XRay)
            {
                hit = Physics2D.Raycast(transform.position,
                    other.transform.position - transform.position,
                    10,
                    VisionMask);
            }
            else
            {
                hit = Physics2D.Raycast(transform.position,
                    other.transform.position - transform.position);
            }
            
            if (hit.collider != null
                && (hit.collider.CompareTag("Character")
                    || hit.collider.CompareTag("Player")))
            {
                Debug.DrawRay(transform.position,
                    (other.transform.position - transform.position) * 1,
                    Color.red);
                if (!visibleCharacters.Contains(hit.collider.gameObject))
                {
                    visibleCharacters.Add(hit.collider.gameObject);
                }
            }
            else
            {
                Debug.DrawRay(transform.position,
                    (other.transform.position - transform.position) * 1,
                    Color.green);
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        List<GameObject> updatedListOfVisibleCharacters = new List<GameObject>();

        foreach (GameObject character in visibleCharacters)
        {
            float distance = Vector2.Distance(transform.position, character.transform.position);
            if (distance < _viewDistance)
            {
                updatedListOfVisibleCharacters.Add(character);
            }
        }

        visibleCharacters = updatedListOfVisibleCharacters;
    }
}