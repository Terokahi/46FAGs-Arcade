using System;
using System.Collections.Generic;
using Godot;

namespace character
{
    public partial class PC : CharacterBody2D
    {
        int tileSize = 16;
        Vector2I Pos;
        Dictionary<Key, Vector2> inputs = new Dictionary<Key, Vector2>(){
            {Key.W, Vector2.Up},
            {Key.S, Vector2.Down},
            {Key.D, Vector2.Right},
            {Key.A, Vector2.Left}
        };
     
        public Vector2 Move()
        {
            Vector2 move = Vector2.Zero;
            foreach (var key in inputs.Keys)
            {
                if (Input.IsKeyPressed(key))
                {
                    move = inputs[key];
                }
            }
            return move;
        }
    }
}
