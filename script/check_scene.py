from command.get_position import get_pic_position_without_cap,  get_pic_position

scenes = {"retry": 0,  # 网络波动，随时遇见

          # 战斗前中后
          "choose_sinners_to_fight": 1, "in_battle": 2, "selecting_ego": 3, "battle_victory": 4, "battle_defeat": 5,

          # 各个镜牢页面
          "init_mirror": 10, "mirror_select_init_ego": 11, "mirror_road": 12, "selecting_a_fight_room": 13,
          "selecting_an_other_room": 14,
          "select_reward_card": 15, "in_shop": 16, "mirror_setting": 17, "settlement_page": 18, "settlement_reward": 19,

          # 主界面六个功能
          "main_window": 30, "sinnners": 31, "drive": 32, "theater": 33, "extract": 34, "dispense": 35,

          # 可以靠点击空白位置或esc键退出
          "notif": 36, "mailbox": 37, "settings": 38, "charge_enkephalin": 39,

          # 剧情对话界面
          "plot_dialogue": 40,

          # 这几个左上角有退后键
          "inventory": 41, "shop": 42, "refund_policy": 43, "display_page": 44, "refraction_railway": 45,
          "luxcavation": 46,

          # 升级页面
          "leave_up": 50,

          # 登录界面
          "log_in": 51,

          # 加载中
          "waiting": 52,

          # 其他未知情况
          "unknown": -1
          }


def where_am_i(lang_model=-1):
    # 优先处理可能出现的网络问题
    if get_pic_position("./pic/scenes/network/retry_countdown.png", lang_model=lang_model) \
            or get_pic_position_without_cap("./pic/scenes/network/retry.png", lang_model=lang_model) \
            or get_pic_position_without_cap("./pic/scenes/network/try_again.png", lang_model=lang_model):
        return 0

    # 接下来识别是否在战斗中
    if get_pic_position_without_cap("./pic/teams/formation_features.png", lang_model=lang_model):
        return 1
    elif get_pic_position_without_cap("./pic/battle/in_battle.png", lang_model=lang_model):
        return 2
    elif get_pic_position_without_cap("./pic/battle/use_ego_features.png", lang_model=lang_model) or \
            get_pic_position_without_cap("./pic/battle/use_ego_features_2.png", lang_model=lang_model) or \
            get_pic_position_without_cap("./pic/battle/ego_resistances.png", lang_model=lang_model):
        return 3
    elif get_pic_position_without_cap("./pic/battle/victory.png", lang_model=lang_model):
        return 4
    elif get_pic_position_without_cap("./pic/battle/defeat.png", lang_model=lang_model):
        return 5

    # 判断是否在镜牢的情况
    if get_pic_position_without_cap("./pic/scenes/init_mirror.png", lang_model=lang_model):
        return 10
    elif get_pic_position_without_cap("./pic/scenes/mirror_select_ego.png", lang_model=lang_model):
        return 11
    elif get_pic_position_without_cap("./pic/scenes/road_in_mirror.png", lang_model=lang_model):
        return 12
    elif get_pic_position_without_cap("./pic/mirror/battle_clear_rewards.png", lang_model=lang_model):
        return 13
    elif get_pic_position_without_cap("./pic/mirror/select_an_other_room.png", lang_model=lang_model):
        return 14
    elif get_pic_position_without_cap("./pic/mirror/select_encounter_reward_card.png", lang_model=lang_model):
        return 15
    elif get_pic_position_without_cap("./pic/mirror/event/shop/shop_features_1.png", lang_model=lang_model) and \
            get_pic_position_without_cap("./pic/mirror/event/shop/shop_features_2.png", lang_model=lang_model):
        return 16
    elif get_pic_position_without_cap("./pic/mirror/mirror_setting_forfeit.png", lang_model=lang_model) and \
            get_pic_position_without_cap("./pic/mirror/mirror_setting_continue.png", lang_model=lang_model) and \
            get_pic_position_without_cap("./pic/mirror/mirror_setting_to_window.png", lang_model=lang_model):
        return 17
    elif get_pic_position_without_cap("./pic/mirror/total_progress.png", lang_model=lang_model):
        return 18
    elif get_pic_position_without_cap("./pic/mirror/exploration_reward.png", lang_model=lang_model):
        return 19
    elif get_pic_position("./pic/mirror/select_encounter_reward_card.png", lang_model=lang_model):
        return 20

    # 如果在主界面的几个窗口，或其他乱七八糟的位置
    if get_pic_position_without_cap("./pic/scenes/init_window.png", lang_model=lang_model) \
            or get_pic_position_without_cap("./pic/scenes/select_window.png", lang_model=lang_model):
        # 代号38,39会因为窗体过小无法遮挡其他识别点，导致无限循环，所以优先度提高
        if get_pic_position_without_cap("./pic/scenes/settings.png", lang_model=lang_model):
            return 38
        elif get_pic_position_without_cap("./pic/scenes/charge_enkephalin.png", lang_model=lang_model):
            return 39
        elif get_pic_position_without_cap("./pic/scenes/select_window.png", lang_model=lang_model) and \
                get_pic_position_without_cap("./pic/scenes/mail.png", lang_model=lang_model) and \
                get_pic_position_without_cap("./pic/prize/now_season.png", lang_model=lang_model):
            return 30
        elif get_pic_position_without_cap("./pic/scenes/sinners_features.png", lang_model=lang_model):
            return 31
        elif get_pic_position_without_cap("./pic/scenes/drive_features.png", lang_model=lang_model):
            return 32
        elif get_pic_position_without_cap("./pic/scenes/therter_features.png", lang_model=lang_model):
            return 33
        elif get_pic_position_without_cap("./pic/scenes/extract_features.png", lang_model=lang_model):
            return 34
        elif get_pic_position_without_cap("./pic/scenes/dispense_features.png", lang_model=lang_model):
            return 35

    elif get_pic_position_without_cap("./pic/scenes/notifs.png", lang_model=lang_model):
        return 36
    elif get_pic_position_without_cap("./pic/scenes/mailbox.png", lang_model=lang_model):
        return 37
    elif get_pic_position_without_cap("./pic/scenes/plot/plot_dialogue.png", lang_model=lang_model):
        return 40
    elif get_pic_position_without_cap("./pic/scenes/inventory.png", lang_model=lang_model):
        return 41
    elif get_pic_position_without_cap("./pic/scenes/shop.png", lang_model=lang_model):
        return 42
    elif get_pic_position_without_cap("./pic/scenes/refund_policy.png", lang_model=lang_model):
        return 43
    elif get_pic_position_without_cap("./pic/scenes/display_page_features.png", lang_model=lang_model):
        return 44
    elif get_pic_position_without_cap("./pic/scenes/refraction_railway.png", lang_model=lang_model):
        return 45
    elif get_pic_position_without_cap("./pic/scenes/luxcavation.png", lang_model=lang_model):
        return 46
    elif get_pic_position_without_cap("./pic/battle/level_up_message.png", lang_model=lang_model) or \
            get_pic_position_without_cap("./pic/battle/level_up_message2.png", lang_model=lang_model):
        return 50
    elif get_pic_position_without_cap("./pic/scenes/login_in.png", lang_model=lang_model):
        return 51
    elif get_pic_position_without_cap("./pic/wait.png", lang_model=lang_model) or \
            get_pic_position_without_cap("./pic/wait_2.png", lang_model=lang_model):
        return 52
    return -1
