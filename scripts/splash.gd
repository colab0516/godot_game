extends Node2D
func _ready():
    # 確保滑鼠隱藏
    Input.set_mouse_mode(Input.MOUSE_MODE_HIDDEN)
    # 等待兩幀，確保引擎已經切換到這個全黑場景後再載入主場景
    await get_tree().process_frame
    await get_tree().process_frame
    get_tree().change_scene_to_file("res://scenes/main.tscn")
