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
        public Sprite2D getSprite(){
            var Sprite = GetNode<Sprite2D> ("PC/PCSprite");
            return Sprite;
        }
        public Sprite2D getRessource(){
            var Ressource = getRessource();
            return Ressource;
        }
        public Texture2D getTexture(){
            Texture2D texture = getTexture();
            return texture;
        }
    }
}