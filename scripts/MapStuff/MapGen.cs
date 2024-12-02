using Godot;
using System;
using System.Collections.Generic;
using System.Linq;
using character;
using globals;
using System.Security.Cryptography.X509Certificates;
using System.Net;
using System.Numerics;

namespace MapGen
{
	public partial class MapGen : Node2D
	{
		readonly globals.globals global = new();
		RandomNumberGenerator rng = new();
		character.PC PC = new();
		CharacterBody2D characterBody;

		/// Contains the available locations for a tile.
		public enum Location{
			TOP_LEFT = 1,
			LOW_LEFT = 2,
			TOP_RIGHT = 4,
			LOW_RIGHT = 8
		}

		/// Contains the available atlas positions for a tile.
		public static readonly Dictionary<int, Vector2I> NeighborsToAtlas = new(){
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

		private Dictionary<int,TileMapLayer> LayerRegistry;
		private static readonly Dictionary<string, int> getLayer_ID = new(){
			{"DecOres", 0},
			{"Collision", 1},
			{"Walkable", 2},
			{"Diveable", 3}
		};
		private static readonly Dictionary<string, int> getTS_ID = new(){
			{"none", -1},
			{"stone", 0},
			{"dirt", 1},
			{"water", 37}
		};

		int map_width;
		int map_height;
		int[,,] map;
		public override void _Ready()
		{
			setMapsize();
			RegisterLayers();
			InitMapArray();
			CreateRooms();
			UpdateTileMapLayers();
			setCharacterBody();
			setChar();
			}

		public void setCharacterBody()
		{
			characterBody = GetNode<CharacterBody2D>("PC");
		}

		public void setMapsize(){
			map_width = global.map_width;
			map_height = global.map_height;
		}

		private void RegisterLayers(){
			LayerRegistry = new(){
				{0, GetNode<TileMapLayer>("DecOres")},
				{1, GetNode<TileMapLayer>("Collision")},
				{2, GetNode<TileMapLayer>("Walkable")},
				{3, GetNode<TileMapLayer>("Diveable")}
			};
		}

		private void InitMapArray(){
			map = new int[map_width, map_height, getLayer_ID.Count];
			var indices = Enumerable.Range(0, map_width * map_height * getLayer_ID.Count).Select(i => new { 
				x = i % map_width,
				y = (i % (map_width * map_height)) / map_width,
				z = i / (map_width * map_height) 
			});
			foreach (var idx in indices){
				map[idx.x, idx.y, getLayer_ID["DecOres"]] = getTS_ID["none"];
				map[idx.x, idx.y, getLayer_ID["Collision"]] = getTS_ID["stone"];
				map[idx.x, idx.y, getLayer_ID["Walkable"]] = getTS_ID["dirt"];
				map[idx.x, idx.y, getLayer_ID["Diveable"]] = getTS_ID["water"];
			}
		}

		/// Updates all the layers in the LayerRegistry.
		/// This function is used to update all the layers in the LayerRegistry.
		/// It loops through each layer in the LayerRegistry and calls the UpdateTilemapLayers.
		private void UpdateTileMapLayers(){
			foreach (var layer in LayerRegistry){
				UpdateTileMapLayers(new Rect2I(0,0,map_width,map_height), layer.Key);
			}
		}

		/// Updates a single cell on the given layer.
		/// <param name="pos">The position of the cell to update.
		/// <param name="layerID">The id of the layer to update.
		private void UpdateTileMapLayers(Vector2I pos, int layerID){
			UpdateTileMapLayers(new Rect2I(pos,pos), layerID);
		}
		
		/// Updates all layers at a specific position.
		/// This function iterates over each layer in the LayerRegistry and updates the tilemap 
		/// layers at the specified position.
		/// <param name="pos">The position of the cell to update across all layers.
		private void UpdateTileMapLayers(Vector2I pos){
			foreach (var layer in LayerRegistry){
				UpdateTileMapLayers(new Rect2I(pos,pos), layer.Key);
			}
		}

		/// Updates a given Rect2I portion on all layers.
		/// This function iterates over each layer in the LayerRegistry and updates the tilemap 
		/// layers within the given Rect2I.
		/// <param name="pos">The Rect2I that contains the cells to update across all layers.
		private void UpdateTileMapLayers(Rect2I pos){
			foreach (var layer in LayerRegistry){
				UpdateTileMapLayers(pos, layer.Key);
			}
		}

		/// Updates a given Rect2I portion on the given Layer.
		/// <param name="pos">The position of the Rect2I.
		/// <param name="layerID">The id of the layer to update.
		private void UpdateTileMapLayers(Rect2I pos, int layerID)
		{
			//Loop through each cell in the array
			for (int x = pos.Position.X; x < pos.Size.X +1; x++)
			{
				for (int y = pos.Position.Y; y < pos.Size.Y +1; y++)
				{
					//Get the current cell from the array


					//Get the cells on the top left and right and bottom left and right (-current cell) 
					//a 2x2 to work for dual grid
					int br,bl,tr,tl;
					int ts = -1;
					try { br = map[x, y, layerID]; } catch (IndexOutOfRangeException) { br = getTS_ID["none"]; }
					try { bl = map[x - 1, y, layerID]; } catch (IndexOutOfRangeException) { bl = getTS_ID["none"]; }
					try { tr = map[x, y - 1, layerID]; } catch (IndexOutOfRangeException) { tr = getTS_ID["none"]; }
					try { tl = map[x - 1, y - 1, layerID]; } catch (IndexOutOfRangeException) { tl = getTS_ID["none"]; }

					//Determine the atlas vector based on the neighboring cells
					int atlasVector = 0;
					if (br != getTS_ID["none"]) {atlasVector |= (int)Location.LOW_RIGHT; ts = br;}
					if (tr != getTS_ID["none"]) {atlasVector |= (int)Location.TOP_RIGHT; ts = tr;}
					if (tl != getTS_ID["none"]) {atlasVector |= (int)Location.TOP_LEFT; ts = tl;}
					if (bl != getTS_ID["none"]) {atlasVector |= (int)Location.LOW_LEFT; ts = bl;}

					//If the atlas vector is 0, then the current cell is not a collision, so set the walkable layer
					if (atlasVector != 0){
						//TODO: understand how this works correctly plx && run/debug
						LayerRegistry[layerID].SetCell(new Vector2I(x, y), ts, NeighborsToAtlas[atlasVector]);
					}
					//stay transparent
						/* else{
							GD.Print("The fuck you doing???");
						} */
					
				}
			}
		}

		public void CreateRooms()
		{
			int FailedCounter = 0;

			int roomAmount = rng.RandiRange(1, 400);
			int min_size = 2;
			int max_size = 6;
			
			for (int i = 0; i < roomAmount; i++)
			{
				rng.Randomize();
				Vector2I roomPos = new(rng.RandiRange(0, map_width-1), rng.RandiRange(0, map_height-1));
				Vector2I roomSize = new(rng.RandiRange(min_size, max_size), rng.RandiRange(min_size, max_size));

				GD.Print("RoomPos: " + roomPos + "\n" + "RoomSize: " + roomSize);
				
				if (roomPos.X + roomSize.X > map_width || roomPos.Y + roomSize.Y > map_height)
				{
					FailedCounter++;
					continue;
				}
				for (int x = roomPos.X; x < roomPos.X + roomSize.X; x++)
				{
					for (int y = roomPos.Y; y < roomPos.Y + roomSize.Y; y++)
					{
						map[x, y, getLayer_ID["Collision"]] = getTS_ID["none"];
						//map[x, y, getLayer_ID["Walkable"]] = getTS_ID["dirt"];
					}
				}
			GD.Print("RoomAmount: " + roomAmount);
			GD.Print("FailedCounter: " + FailedCounter);
			}
		}

		public void setChar()
		{ //set sprite for layer
			rng.Randomize();
			bool posFlag = false;
			int x;
			int y;
			while (posFlag != true)
			{
				x = rng.RandiRange(0, map_width - 1);
				y = rng.RandiRange(0, map_height - 1);
				if (map[x,y,getLayer_ID["Collision"]] == getTS_ID["none"]);
				{	
					posFlag = true;
					characterBody.Position = new Vector2I(x,y);
				}		
			}
			GD.Print(characterBody.Position);
		}

		public override void _Process(double delta)
		{
		}
	}
}


