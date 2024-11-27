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


		private TileMapLayer wall,floor;
		public void SetWall(){wall = GetNode<TileMapLayer>("Wall");}
		public void SetFloor(){floor = GetNode<TileMapLayer>("Floor");}
		public TileMapLayer GetWall => wall;
		public TileMapLayer GetFloor => floor;

		public override void _Ready()
		{
			SetWall();
			SetFloor();
			int x = 20;
			int y = 20;
			string[,] map = new string[x, y];
			var indices = Enumerable.Range(0, x * y).Select(i => new { x = i % x, y = i / x });
			foreach (var idx in indices){
				map[idx.x, idx.y] = "stone_wall";
			}
			UpdateRectInLayersFromArray(map, new Rect2I(0, 0, x, y));
			///loop to find tileMapLayers to use later maybe: 
			Node[] nodes = GetNode("../..").GetChildren().ToArray();
			foreach (Godot.Node node in nodes){
				if (node is TileMapLayer layer){}
			}
		}

		/// Updates the layers from an array.
		/// <param name="map">The array to update the layers from.</param>
		/// <param name="pos">The position of the array in the tilemap.</param>
		private void UpdateRectInLayersFromArray(string[,] map, Rect2I pos)
		{
			for (int x = pos.Position.X; x < pos.Size.X + 1; x++)
			{
				for (int y = pos.Position.Y; y < pos.Size.Y + 1; y++)
				{
					string br = map[x, y];
					string bl;
					string tr;
					string tl;
					try { bl = map[x - 1, y]; } catch (IndexOutOfRangeException) { bl = "void"; }
					try { tr = map[x, y - 1]; } catch (IndexOutOfRangeException) { tr = "void"; }
					try { tl = map[x - 1, y - 1]; } catch (IndexOutOfRangeException) { tl = "void"; }
					int atlasVector = 0;
					if (br.Contains("wall")) atlasVector |= (int)Location.LOW_RIGHT;
					if (bl.Contains("wall")) atlasVector |= (int)Location.LOW_LEFT;
					if (tr.Contains("wall")) atlasVector |= (int)Location.TOP_RIGHT;
					if (tl.Contains("wall")) atlasVector |= (int)Location.TOP_LEFT;
					if (atlasVector == 0)
					{
						if (br.Contains("floor")) atlasVector |= (int)Location.LOW_RIGHT;
						if (bl.Contains("floor")) atlasVector |= (int)Location.LOW_LEFT;
						if (tr.Contains("floor")) atlasVector |= (int)Location.TOP_RIGHT;
						if (tl.Contains("floor")) atlasVector |= (int)Location.TOP_LEFT;
						GetFloor.SetCell(new Vector2I(x, y), 1, NeighborsToAtlas[atlasVector]);
						GetWall.SetCell(new Vector2I(x, y), 0, NeighborsToAtlas[0]);//transparent
					}
					else
					{
						GetFloor.SetCell(new Vector2I(x, y), 1, NeighborsToAtlas[15]);//full tile below walls
						GetWall.SetCell(new Vector2I(x, y), 0, NeighborsToAtlas[atlasVector]);
					}
				}
			}
		}

		public override void _Process(double delta)
		{
		}
	}
}
