

extends CharacterBody2D 
 
@export var speed: float = 300.0 

# 跳躍 使用
@export var jump_power: float = 60.0  # 跳躍的高度（像素）
var is_jumping: bool = false

@onready var anim = $KnightAnim

 
func _physics_process(_delta): 
    # 獲取四個方向的輸入向量 (-1 到 1) 
    var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down") 
 
    if direction != Vector2.ZERO: 
        velocity = direction * speed 
        # 根據左右移動翻轉圖片 
        if direction.x != 0: 
            $KnightAnim.flip_h = direction.x < 0 
        $KnightAnim.play("default") 
    else: 
        velocity = velocity.move_toward(Vector2.ZERO, speed) 
        # 停止移動時可以選擇停止動畫 
        # $AnimatedSprite2D.stop() 

        

    # 2. 無重力跳躍觸發 (按下空白鍵)
    # 我們不再檢查 is_on_floor()，改用自定義的 is_jumping 變數
    if Input.is_action_just_pressed("ui_accept") and not is_jumping:
        perform_visual_jump()
 
    move_and_slide() 

# 核心：利用 Tween 讓「圖片」上下彈動，而不是讓「身體」上下移動
func perform_visual_jump():
    is_jumping = true
    var tween = create_tween()
    
    # 第一步：圖片往上彈 (修改 offset.y)
    tween.tween_property(anim, "offset:y", -jump_power, 0.25).set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_OUT)
    
    # 第二步：圖片掉回原位
    tween.tween_property(anim, "offset:y", 0, 0.25).set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_IN)
    
    # 結束後重置狀態
    tween.finished.connect(func(): is_jumping = false)
