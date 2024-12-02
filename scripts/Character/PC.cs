using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Runtime.CompilerServices;
using Godot;

namespace character
{
    public partial class PC : CharacterBody2D
    {
        Sprite2D Sprite;
        Texture2D Texture;
        Sprite2D Ressource;
        public Sprite2D GetSprite(){
            var Sprite = GetNode<Sprite2D> ("PC/PCSprite");
            return Sprite;
        }
        public  Sprite2D GetRessource(){
            return Ressource;
        }
        public Texture2D GetTexture(){
            return Texture;
        }
    }
}