using Godot;
using System;
using System.Collections.Generic;
using System.Linq;

namespace MapGen
{
	public partial class NewScript : TileMapLayer
	{

		/// Contains the available locations for a tile.
		public enum Location
		{
			TOP_LEFT = 1,
			LOW_LEFT = 2,
			TOP_RIGHT = 4,
			LOW_RIGHT = 8
		}

		/// Contains the available atlas positions for a tile.
		public static readonly Dictionary<int, Vector2I> NeighborsToAtlas = new Dictionary<int, Vector2I>
		{
			{ 0, new Vector2I(0, 3) },
			{ 1, new Vector2I(3, 3) },
			{ 2, new Vector2I(0, 0) },
			{ 3, new Vector2I(3, 2) },
			{ 4, new Vector2I(0, 2) },
			{ 5, new Vector2I(1, 2) },
			{ 6, new Vector2I(2, 3) },
			{ 7, new Vector2I(3, 1) },
			{ 8, new Vector2I(1, 3) },
			{ 9, new Vector2I(0, 1) },
			{ 10, new Vector2I(3, 0) },
			{ 11, new Vector2I(2, 0) },
			{ 12, new Vector2I(1, 0) },
			{ 13, new Vector2I(2, 2) },
			{ 14, new Vector2I(1, 1) },
			{ 15, new Vector2I(2, 1) }
		};

		private Dictionary<int,TileMapLayer> LayerFromID;
		private Dictionary<string,int> IDFromLayerName;
		private Dictionary<string,int> TS_ID;

		public override void _Ready()
		{
			LayerFromID = new(){
				{0, GetNode<TileMapLayer>("DecOres")},
				{1, GetNode<TileMapLayer>("Collision")},
				{2, GetNode<TileMapLayer>("Walkable")},
				{3, GetNode<TileMapLayer>("Diveable")}
			};

			IDFromLayerName = new(){
				{"DecOres", 0},
				{"Collision", 1},
				{"Walkable", 2},
				{"Diveable", 3}
			};
			TS_ID = new(){
				{"void", -1},
				{"stone", 0},
				{"dirt", 1},
				{"water",37}
			};

			int x = 20;
			int y = 20;
			int z = LayerFromID.Count;
			int[,,] map = new int[x, y, z];
			var indices = Enumerable.Range(0, x * y * z).Select(i => new { 
				x = i % x,
				y = i % (x * y) / x,
				z = i / (x * y) });
			foreach (var idx in indices){
				map[idx.x, idx.y, IDFromLayerName["DecOres"]] = TS_ID["void"];
				map[idx.x, idx.y, IDFromLayerName["Collision"]] = TS_ID["stone"];
				map[idx.x, idx.y, IDFromLayerName["Walkable"]] = TS_ID["dirt"];
				map[idx.x, idx.y, IDFromLayerName["Diveable"]] = TS_ID["water"];
			}

			UpdateRectInLayersFromArray(map, new Rect2I(0, 0, x, y));

			/* /// loop to find tileMapLayers to use later maybe: 
				Node[] nodes = GetNode("../..").GetChildren().ToArray();
				foreach (Godot.Node node in nodes){
					if (node is TileMapLayer layer){}
				}
			*/
		}

		/// Updates the layers from an array.
		/// <param name="map">The array to update the layers from.</param>
		/// <param name="pos">The position of the array in the tilemap.</param>
		private void UpdateRectInLayersFromArray(int[,,] map, Rect2I pos)
		{
			//Loop through each cell in the array
			for (int x = pos.Position.X; x < pos.Size.X + 1; x++)
			{
				for (int y = pos.Position.Y; y < pos.Size.Y + 1; y++)
				{
					for (int z = 0; z < map.GetLength(2); z++)
					{
						//Get the current cell from the array
						int br = map[x, y, z];

						//Get the cells on the top left and right and bottom left and right (-current cell) 
						//a 2x2 to work for dual grid
						int bl,tr,tl;
						try { bl = map[x - 1, y, z]; } catch (IndexOutOfRangeException) { bl = TS_ID["void"]; }
						try { tr = map[x, y - 1, z]; } catch (IndexOutOfRangeException) { tr = TS_ID["void"]; }
						try { tl = map[x - 1, y - 1, z]; } catch (IndexOutOfRangeException) { tl = TS_ID["void"]; }

						//Determine the atlas vector based on the neighboring cells
						int atlasVector = 0;
						if (br != TS_ID["void"]) atlasVector |= (int)Location.LOW_RIGHT;
						if (tr != TS_ID["void"]) atlasVector |= (int)Location.TOP_RIGHT;
						if (tl != TS_ID["void"]) atlasVector |= (int)Location.TOP_LEFT;
						if (bl != TS_ID["void"]) atlasVector |= (int)Location.LOW_LEFT;

						//If the atlas vector is 0, then the current cell is not a collision, so set the walkable layer
						if (atlasVector != 0){
							//TODO: understand how this works correctly plx
							LayerFromID[z].SetCell(new Vector2I(x, y), ((dynamic)tl).Id, NeighborsToAtlas[atlasVector]);
						}
						/* stay transparent
						else{
							GD.Print("The fuck you doing???");
						}
						*/
					}
				}
			}
		}

		public override void _Process(double delta)
		{
		}
	}
}
/*
	dict.add <LayerFromID, getNode>
	
	arr[x,y] = dict.key(0)
	arr[x,y+1] = 1
	if arr[x,y] != 0
	________
	private var whatIDFromLayerName = new Dictionary<string,TileMapLayer>{
	{"stone_collision", GetCollision},
	{"dirt_walkable", GetWalkable},
	{"stone_walkable", GetWalkable}
	}
	private var whatID = new Dictionary<string,int>{
	{"stone_collision", 0},
	{"dirt_walkable", 1},
	{"stone_walkable", 0}
	}
	___________
	string[,] map ="stone_collision"
	arr[,,] map= LayerFromID
	___________
	
	dict<new Vector2i, (getIDFromLayerName, int)>
	*/

	

