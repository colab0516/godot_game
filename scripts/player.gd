extends CharacterBody2D
@export var speed: float = 300.0
@onready var anim = $KnightAnim

func _physics_process(_delta):
    var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = direction * speed if direction else velocity.move_toward(Vector2.ZERO, speed)
    if direction.x != 0: anim.flip_h = direction.x < 0
    move_and_slide()
