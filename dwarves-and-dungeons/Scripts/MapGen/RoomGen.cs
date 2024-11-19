namespace RoomGen
{
    public class Rooms
    {
        int width;
        int height;
        int posX;
        int posY;

        public set_width()
        {
            random = new Random();
            width = random.Next(2, 6);
        }
    }
}