using Godot;
using System;

namespace Room
{
	class Rooms
	{
		private int roomAmount;
		private int pos;
		private Vector2I size;
		
		private int Random(int min, int max)
		{
			int number;
			var rng = new RandomNumberGenerator();
			rng.Randomize();
			number = rng.RandiRange(min,max);
			return number;
		}
		
		private void setRoomAmount()
		{
			roomAmount = Random(1,400);
		}
		
		public void setSize(int maxX, int maxY, int minX,int minY)
		{
			size = new Vector2I(Random(minX, maxX), Random(minY,maxY));
		}
		
		public int getRoomAmount()
		{
			setRoomAmount();
			return roomAmount;
		}
		
		public Vector2I getSize()
		{
			return size;
		}
	}
}
