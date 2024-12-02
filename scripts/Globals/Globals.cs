using Godot;
namespace globals
{
    public partial class Globals : Node
    {
        private static readonly int tilesize = 16;
        private static readonly int map_width = 1920 / tilesize;
        private static readonly int map_height = 1080 / tilesize;
        public static int GetTileSize() { return tilesize; }
        public static int GetMapWidth() { return map_width; }
        public static int GetMapHeight() { return map_height; }
    }
}