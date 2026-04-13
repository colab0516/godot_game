extends Node2D
func _ready():
    # 秒開後立刻切換到主場景
    get_tree().change_scene_to_file("res://scenes/main.tscn")
