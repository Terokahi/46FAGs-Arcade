using System;
using System.Collections.Generic;
using System.Numerics;
using Godot;

namespace character
{
    public partial class PC : CharacterBody2D
    {
        int tileSize = 16;
        Vector2I Pos;
        public Vector2I Move(){
            
            var inputs = new Dictionary<string, Vector2I>() {
                {"move_right", Vector2I.Right},
                {"move_left",Vector2I.Left},
                {"move_down", Vector2I.Down},
                {"move_up", Vector2I.Up}
            };

            foreach (string dir in inputs.Keys)
                {
                    if (Input.IsActionPressed(dir))
                    {
                        Pos = inputs[dir];
                    }
                }
            return Pos;
        }
    }
}
