extends CharacterBody2D
@export var speed = 300.0
@onready var anim = $KnightAnim
func _physics_process(delta):
    var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    if input_dir != Vector2.ZERO:
        velocity = input_dir * speed
        anim.flip_h = (input_dir.x < 0)
        anim.play("default")
    else:
        velocity = velocity.move_toward(Vector2.ZERO, speed)
        anim.stop()
    move_and_slide()
