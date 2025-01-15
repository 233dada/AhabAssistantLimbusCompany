# import yaml
from ruamel.yaml import YAML

from my_log.my_log import my_log

yaml = YAML()

default_config = {
    "default_page": 0,
    "set_lang_setting": 0,
    "set_windows": True,
    "daily_task": False,
    "get_reward": False,
    "buy_enkephalin": False,
    "mirror": False,
    "set_win_size": 0,
    "set_win_position": 0,
    "set_reduce_miscontact": 0,
    "set_EXP_count": 1,
    "set_thread_count": 3,
    "all_teams": 1,
    "set_get_prize": 0,
    "set_lunacy_to_enkephalin": 2,
    "set_mirror_count": 1,
    "team1": False,
    "team2": False,
    "team3": False,
    "team4": False,
    "team5": False,
    "team6": False,
    "team7": False,
    "teams_be_select": 0,
    "team1_order": "",
    "team2_order": "",
    "team3_order": "",
    "team4_order": "",
    "team5_order": "",
    "team6_order": "",
    "team7_order": "",
    "team1_setting": {
        "all_system": 0,
        "all_teams": 1,
        "sinners_be_select": 0,
        "YiSang": False,
        "YiSang_order": "",
        "Faust": False,
        "Faust_order": "",
        "DonQuixote": False,
        "DonQuixote_order": "",
        "Ryoshu": False,
        "Ryoshu_order": "",
        "Meursault": False,
        "Meursault_order": "",
        "HongLu": False,
        "HongLu_order": "",
        "Heathcliff": False,
        "Heathcliff_order": "",
        "Ishmael": False,
        "Ishmael_order": "",
        "Rodion": False,
        "Rodion_order": "",
        "Sinclair": False,
        "Sinclair_order": "",
        "Outis": False,
        "Outis_order": "",
        "Gregor": False,
        "Gregor_order": "",
        "fuse": False,
        "burn": False,
        "bleed": False,
        "tremor": False,
        "rupture": False,
        "poise": False,
        "sinking": False,
        "charge": False,
        "slash": False,
        "pierce": False,
        "blunt": False,
    },
    "team2_setting": {
        "all_system": 0,
        "all_teams": 1,
        "sinners_be_select": 0,
        "YiSang": False,
        "YiSang_order": "",
        "Faust": False,
        "Faust_order": "",
        "DonQuixote": False,
        "DonQuixote_order": "",
        "Ryoshu": False,
        "Ryoshu_order": "",
        "Meursault": False,
        "Meursault_order": "",
        "HongLu": False,
        "HongLu_order": "",
        "Heathcliff": False,
        "Heathcliff_order": "",
        "Ishmael": False,
        "Ishmael_order": "",
        "Rodion": False,
        "Rodion_order": "",
        "Sinclair": False,
        "Sinclair_order": "",
        "Outis": False,
        "Outis_order": "",
        "Gregor": False,
        "Gregor_order": "",
        "fuse": False,
        "burn": False,
        "bleed": False,
        "tremor": False,
        "rupture": False,
        "poise": False,
        "sinking": False,
        "charge": False,
        "slash": False,
        "pierce": False,
        "blunt": False,
    },
    "team3_setting": {
        "all_system": 0,
        "all_teams": 1,
        "sinners_be_select": 0,
        "YiSang": False,
        "YiSang_order": "",
        "Faust": False,
        "Faust_order": "",
        "DonQuixote": False,
        "DonQuixote_order": "",
        "Ryoshu": False,
        "Ryoshu_order": "",
        "Meursault": False,
        "Meursault_order": "",
        "HongLu": False,
        "HongLu_order": "",
        "Heathcliff": False,
        "Heathcliff_order": "",
        "Ishmael": False,
        "Ishmael_order": "",
        "Rodion": False,
        "Rodion_order": "",
        "Sinclair": False,
        "Sinclair_order": "",
        "Outis": False,
        "Outis_order": "",
        "Gregor": False,
        "Gregor_order": "",
        "fuse": False,
        "burn": False,
        "bleed": False,
        "tremor": False,
        "rupture": False,
        "poise": False,
        "sinking": False,
        "charge": False,
        "slash": False,
        "pierce": False,
        "blunt": False,
    },
    "team4_setting": {
        "all_system": 0,
        "all_teams": 1,
        "sinners_be_select": 0,
        "YiSang": False,
        "YiSang_order": "",
        "Faust": False,
        "Faust_order": "",
        "DonQuixote": False,
        "DonQuixote_order": "",
        "Ryoshu": False,
        "Ryoshu_order": "",
        "Meursault": False,
        "Meursault_order": "",
        "HongLu": False,
        "HongLu_order": "",
        "Heathcliff": False,
        "Heathcliff_order": "",
        "Ishmael": False,
        "Ishmael_order": "",
        "Rodion": False,
        "Rodion_order": "",
        "Sinclair": False,
        "Sinclair_order": "",
        "Outis": False,
        "Outis_order": "",
        "Gregor": False,
        "Gregor_order": "",
        "fuse": False,
        "burn": False,
        "bleed": False,
        "tremor": False,
        "rupture": False,
        "poise": False,
        "sinking": False,
        "charge": False,
        "slash": False,
        "pierce": False,
        "blunt": False,
    },
    "team5_setting": {
        "all_system": 0,
        "all_teams": 1,
        "sinners_be_select": 0,
        "YiSang": False,
        "YiSang_order": "",
        "Faust": False,
        "Faust_order": "",
        "DonQuixote": False,
        "DonQuixote_order": "",
        "Ryoshu": False,
        "Ryoshu_order": "",
        "Meursault": False,
        "Meursault_order": "",
        "HongLu": False,
        "HongLu_order": "",
        "Heathcliff": False,
        "Heathcliff_order": "",
        "Ishmael": False,
        "Ishmael_order": "",
        "Rodion": False,
        "Rodion_order": "",
        "Sinclair": False,
        "Sinclair_order": "",
        "Outis": False,
        "Outis_order": "",
        "Gregor": False,
        "Gregor_order": "",
        "fuse": False,
        "burn": False,
        "bleed": False,
        "tremor": False,
        "rupture": False,
        "poise": False,
        "sinking": False,
        "charge": False,
        "slash": False,
        "pierce": False,
        "blunt": False,
    },
    "team6_setting": {
        "all_system": 0,
        "all_teams": 1,
        "sinners_be_select": 0,
        "YiSang": False,
        "YiSang_order": "",
        "Faust": False,
        "Faust_order": "",
        "DonQuixote": False,
        "DonQuixote_order": "",
        "Ryoshu": False,
        "Ryoshu_order": "",
        "Meursault": False,
        "Meursault_order": "",
        "HongLu": False,
        "HongLu_order": "",
        "Heathcliff": False,
        "Heathcliff_order": "",
        "Ishmael": False,
        "Ishmael_order": "",
        "Rodion": False,
        "Rodion_order": "",
        "Sinclair": False,
        "Sinclair_order": "",
        "Outis": False,
        "Outis_order": "",
        "Gregor": False,
        "Gregor_order": "",
        "fuse": False,
        "burn": False,
        "bleed": False,
        "tremor": False,
        "rupture": False,
        "poise": False,
        "sinking": False,
        "charge": False,
        "slash": False,
        "pierce": False,
        "blunt": False,
    },
    "team7_setting": {
        "all_system": 0,
        "all_teams": 1,
        "sinners_be_select": 0,
        "YiSang": False,
        "YiSang_order": "",
        "Faust": False,
        "Faust_order": "",
        "DonQuixote": False,
        "DonQuixote_order": "",
        "Ryoshu": False,
        "Ryoshu_order": "",
        "Meursault": False,
        "Meursault_order": "",
        "HongLu": False,
        "HongLu_order": "",
        "Heathcliff": False,
        "Heathcliff_order": "",
        "Ishmael": False,
        "Ishmael_order": "",
        "Rodion": False,
        "Rodion_order": "",
        "Sinclair": False,
        "Sinclair_order": "",
        "Outis": False,
        "Outis_order": "",
        "Gregor": False,
        "Gregor_order": "",
        "fuse": False,
        "burn": False,
        "bleed": False,
        "tremor": False,
        "rupture": False,
        "poise": False,
        "sinking": False,
        "charge": False,
        "slash": False,
        "pierce": False,
        "blunt": False,
    },
}

default_blacklist = {
    "keys": [
        "outcast",
        "unloving",
        "flowers",
        "abyss",
        "bones",
        "time",
        "warp",
        "violet",
        "dicers",
        "pierces",
        "breakers",
        "wrath",
        "sloth",
        "flood",
        "vain",
    ]
}


def get_yaml_information():
    try:
        with open('config.yaml', 'r', encoding='utf-8') as file:
            config_data = yaml.load(file)
            return config_data
    except:
        msg = f"读取yaml配置失败,使用默认配置"
        my_log("debug", msg)
        save_yaml(default_config)
        return default_config


def save_yaml(config_data):
    with open('config.yaml', 'w', encoding='utf-8') as file:
        msg = f"保存yaml配置文件"
        my_log("debug", msg)
        yaml.dump(config_data, file)


def get_black_list_keyword_yaml():
    try:
        with open('black_list_keyword.yaml', 'r', encoding='utf-8') as file:
            msg = f"读取镜牢主题包黑名单"
            my_log("debug", msg)
            config_data = yaml.load(file)
        return config_data
    except:
        with open('black_list_keyword.yaml', 'w', encoding='utf-8') as file:
            msg = f"读取镜牢主题包黑名单失败,使用默认黑名单"
            my_log("debug", msg)
            yaml.dump(default_blacklist, file)
        return default_blacklist


# 递归函数，用于替换所有的"clash"字符串为"pierce",处理历史遗留问题用
def replace_old_with_new(item, old="clash", new="pierce"):
    if isinstance(item, dict):
        for key, value in item.items():
            item[key] = replace_old_with_new(value)
    elif isinstance(item, list):
        for i in range(len(item)):
            item[i] = replace_old_with_new(item[i])
    elif isinstance(item, str):
        item = item.replace(old, new)
    return item


# 为配置文件添加设置项
def add_keyword_to_yaml(config_datas):
    for i in range(1, 8):
        target_dict = config_datas[f'team{i}_setting']
        if 'fuse' not in target_dict:
            new_items = []
            for key, value in target_dict.items():
                if key == 'burn':
                    new_items.append(('fuse', False))
                new_items.append((key, value))
            target_dict.update(new_items)
    return config_datas

