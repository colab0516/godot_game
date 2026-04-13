extends CharacterBody2D
const SPEED = 200.0
func _physics_process(_delta):
    var dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = dir * SPEED
    if dir.x != 0: $KnightAnim.flip_h = dir.x < 0
    move_and_slide()
