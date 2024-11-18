using Godot;
using System;

public partial class MapGen : Node2D
{
    // Called when the node enters the scene tree for the first time.
    public override void _Ready()
    {
        Random rng = new Random();
        rng.NextInt64();
    }
}
