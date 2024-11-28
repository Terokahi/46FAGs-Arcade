using Godot;
using System;
using System.Collections.Generic;

public partial class MapGenTest : Node2D
{
	/// The layers of the map
	/// @wall > The layer that is used to block the player's movement
	/// @floor > The layer that is used as the visible floor of the map
	/// @fluid > The layer that is used for fluids such as lava and water
	private TileMapLayer wall, floor;
	
	/// Sets the wall layer of the map
	/// <param name="node">The wall layer of the map
	public void setWall()
	{
		wall = GetNode<TileMapLayer>("Wall");
	}
	
	/// Sets the floor layer of the map
	/// <param name="node">The floor layer of the map
	public void setFloor()
	{
		floor = GetNode<TileMapLayer>("Floor");
	}
	
	public void setDict(Dictionary<int, TileMapLayer> TLM_ID)
	{		
		TLM_ID.Add(0, wall);
		TLM_ID.Add(1, floor);
	}
	/// Getter Methods for the Layers
	public TileMapLayer getWall => wall;
	public TileMapLayer getFloor => floor;
	
	/// Called when the node enters the scene tree for the first time
	public override void _Ready()
	{
		Dictionary<int, TileMapLayer> TLM_ID = new Dictionary <int, TileMapLayer>();
		
		setWall();
		setFloor();
		
		setDict(TLM_ID);
		
		// Set Map Size relative to screen Size
		// Saved in var for future use
		int width = 1920;
		int height = 1080;
		
		MapInit(new Vector2I(0,0), new Vector2I(width, height), getWall);
	}
	
	/// Initializes the map with the given size and wall layer
	/// <param name="X">The width of the map
	/// <param name="Y">The height of the map
	/// <param name="wall">The wall layer of the map
	
	/// This function sets the map to a solid stone layer.

	/// <remarks>
	/// This function is used to initialize the map with a solid stone layer.
	/// The map is then ready to be used with the room generation algorithm.
	private void MapInit(Vector2I pos, Vector2I size, TileMapLayer type)
	{
		Vector2I SolidStone = new Vector2I(2,1);
		int TS_ID = 0;
		for (int x = pos.X -1; x < size.X; x++)
		{
			for (int y = pos.Y -1; y < size.Y; y++)
			{
				Vector2I TilePos = new Vector2I(x,y);
				type.SetCell(TilePos,TS_ID,SolidStone);
			}
		}
	}
	
	/*	
	
	// replaces MapInit() later please
	private void setArea(Vector2I pos, Vector2I size, [TML_ID, TS_ID])
	{
		Vector2I SolidStone = new Vector2I(2,1);
		wall = getFloor;
		for (int x = pos.X -1; x < size.X; x++)
		{
			for (int y = pos.Y -1; y < size.Y; y++)
			{
				Vector2I Tilepos = new Vector2I(x,y);
				wall.SetCell(Tilepos,TS_ID,SolidStone);
			}
		}
	}
	*/
	/// Called every frame. 'delta' is the elapsed time since the previous frame
	/// <param name="delta">The time elapsed since the previous frame
	public override void _Process(double delta)
	{
	}
}
