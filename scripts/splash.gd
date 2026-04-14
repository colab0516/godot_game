extends Node2D
func _ready():
    Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)
    await get_tree().process_frame
    await get_tree().process_frame
    get_tree().change_scene_to_file("res://scenes/main.tscn")
