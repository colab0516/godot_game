extends CharacterBody2D

@export var speed = 300.0
@export var jump_velocity = -400.0

# 獲取系統預設重力（先備用）
var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")

@onready var anim = $KnightAnim

func _physics_process(delta):
    # --- [重力區] 如果想啟動跳躍遊戲，請取消下方兩行註解 ---
    # if not is_on_floor():
    #     velocity.y += gravity * delta

    # --- [跳躍區] 如果想啟動跳躍，請取消下方兩行註解 ---
    # if Input.is_action_just_pressed("ui_accept") and is_on_floor():
    #     velocity.y = jump_velocity

    # --- [移動區] 支援左右與上下移動 ---
    var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    
    # 左右移動處理
    if input_dir.x != 0:
        velocity.x = input_dir.x * speed
        anim.flip_h = (input_dir.x < 0)
    else:
        velocity.x = move_toward(velocity.x, 0, speed)

    # 上下移動處理 (重力關閉時可用)
    if input_dir.y != 0:
        velocity.y = input_dir.y * speed
    else:
        # 如果開啟重力，下方這行建議註解掉，改用 velocity.y = move_toward(velocity.y, 0, speed)
        velocity.y = move_toward(velocity.y, 0, speed)

    # 動畫控制
    if input_dir != Vector2.ZERO:
        anim.play("default")
    else:
        anim.stop()

    move_and_slide()
