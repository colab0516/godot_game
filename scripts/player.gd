extends CharacterBody2D
@export var speed = 250.0
@onready var anim = $KnightAnim
func _physics_process(_delta):
    var d = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = d * speed
    if d.x != 0: anim.flip_h = d.x < 0
    if d != Vector2.ZERO: anim.play("default")
    else: anim.stop()
    move_and_slide()
