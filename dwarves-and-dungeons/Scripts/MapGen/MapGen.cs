using Godot;
using System;
using RoomGen;

public partial class MapGen : MapNode
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		width = 1920 / 16;
		height = 1080 / 16;
		array = new int[width, height];

		Room = Rooms.set_width();
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}


