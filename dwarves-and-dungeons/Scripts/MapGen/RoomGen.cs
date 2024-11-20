using System;

namespace RoomGen
{
    public class Rooms
    {
        int width;
        int height;
        int posX;
        int posY;

        // Sets amount of Rooms on the Map
        private int set_roomAmount()
        {
            var random = new Random();
            int roomAmount = random.Next(1, 400);
            return roomAmount;
        }

        // Sets width of the Room
        private int set_width()
        {
            var random = new Random();
            width = random.Next(2, 6);
            return width;
        }
        
        // Sets height of the Room
        private int set_height()
        {
            var random = new Random();
            height = random.Next(2, 6);
            return height;
        }

        // Returns amount of Rooms
        public int get_roomAmount()
        {
            int roomAmount = set_roomAmount();
            return roomAmount;
        }

        // Returns width of the Room
        public int get_width()
        {
            width = set_width();
            return width;
        }
        
        // Returns height of the Room
        public int get_height()
        {
            height = set_height();
            return height;
        }
    }
}