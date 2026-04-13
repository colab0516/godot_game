extends CharacterBody2D
func _physics_process(_delta):
    var dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = dir * 400.0
    move_and_slide()