using Godot;
using System;
using RoomGen;

public partial class MapGen : Map
{
	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
		TileSetSource tileSource = new TileSetSource();
		// Set Map Size relative to screen Size
		// Saved in var for future use
		int width = 1920 / 16;
		int height = 1080 / 16;

		//Generate Map
		for (int x = 0; x < width; x++)
		{
			for (int y = 0; y < height; y++)
			{
				var Map[x, y] = 0;
			}
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}


