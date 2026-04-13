extends CharacterBody2D
@export var speed: float = 300.0
@export var jump_power: float = 60.0
var is_jumping: bool = false
@onready var anim = $KnightAnim
func _physics_process(_delta):
    var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    if direction != Vector2.ZERO:
        velocity = direction * speed
        if direction.x != 0: anim.flip_h = direction.x < 0
        anim.play("default")
    else:
        velocity = velocity.move_toward(Vector2.ZERO, speed)
    if Input.is_action_just_pressed("ui_accept") and not is_jumping:
        perform_visual_jump()
    move_and_slide()
func perform_visual_jump():
    is_jumping = true
    var tween = create_tween()
    tween.tween_property(anim, "offset:y", -jump_power, 0.25).set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_OUT)
    tween.tween_property(anim, "offset:y", 0, 0.25).set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_IN)
    tween.finished.connect(func(): is_jumping = false)
