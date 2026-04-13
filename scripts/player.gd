extends CharacterBody2D
@export var speed = 300.0
@export var jump_p = 60.0
var is_jumping = false
@onready var anim = $KnightAnim
func _physics_process(_delta):
    var dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = dir * speed if dir != Vector2.ZERO else velocity.move_toward(Vector2.ZERO, speed)
    if dir.x != 0: anim.flip_h = dir.x < 0
    if dir != Vector2.ZERO: anim.play("default")
    if Input.is_action_just_pressed("ui_accept") and not is_jumping:
        is_jumping = true
        var tw = create_tween()
        tw.tween_property(anim, "offset:y", -jump_p, 0.2).set_trans(Tween.TRANS_SINE)
        tw.tween_property(anim, "offset:y", 0, 0.2).set_trans(Tween.TRANS_SINE)
        tw.finished.connect(func(): is_jumping = false)
    move_and_slide()