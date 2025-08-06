from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo

from PyQt5.QtWidgets import QApplication

from module.config import cfg
from module.logger import log
# from app.my_app import MainWindow # 不要导入这个

import inspect

# 遵从 IETF BCP-47 除非和 Qt 的不一样
SUPPORTED_LANG_CODE = {
    "zh_cn": "简体中文", #暂时是zh_cn 等之后全局替换
    "en": "English",
}

# 反转字典，方便设置界面显示语言名称
SUPPORTED_LANG_NAME = {v: k for k, v in SUPPORTED_LANG_CODE.items()}

retranslateUi = "retranslateUi"

class LanguageManager:
    """语言管理器
    ---
    \n实例化后通过`.instance()`方法获取实例 不要直接实例化, 请通过`instance()`实例化
    ---
    \n通过`register_component(cls)`可以直接在对应文件下注册类
    \n通过`set_language`会触发注册过的类的`retranslateUi`方法, 如果该方法需要参数, 会且仅会传入一个参数, lang_code: `str`
    \n该文件下(不是本类)有两个全局变量
    - SUPPORTED_LANG_CODE: `dict`
        - 键值为语言**代码**, 字典值为对应名称
    - SUPPORTED_LANG_NAME: `dict`
        - 键值为对语言**名称**, 字典值为对应代码
    """

    _instance = None

    def __init__(self, ui=None):

        self.app = QApplication.instance()
        self.translatable_components = []  # 存储所有需要翻译的组件
        self.settings_language = cfg.language_in_program 

        if ui:
            self.register(ui)
        
    @classmethod
    def instance(cls, ui=None):
        """返回当前实例"""
        if cls._instance is None:
            cls._instance = cls(ui)
        return cls._instance

    def register(self, ui):
        """注册对应组件以更新文本内容"""
        self.register_component(ui)
        self.register_component(ui.farming_interface)
        self.register_component(ui.help_interface)
        self.register_component(ui.setting_interface)

    def register_component(self, component):
        """注册需要翻译的组件"""
        if component in self.translatable_components:
            return
        
        if hasattr(component, retranslateUi):
            self.translatable_components.append(component)
            component_name = self.check_component_name(component)
            log.DEBUG(f"注册翻译组件: {component_name}")
        else:
            component_name = self.check_component_name(component)
            
            log.WARNING(f"组件 {component_name} 没有 {retranslateUi} 方法，无法翻译")
        
    def init_language(self):
        """初始化语言设置"""

        if self.settings_language is None:
            lang = self.match_language() 
        else:
            lang = self.settings_language


        self.set_language(lang)
        

    def match_language(self) -> str:
        """在支持的语言中匹配最接近用户系统语言的语言"""
        user_lang = QLocale.system().name() # 获取语言代码 示例: zh_CN
        log.DEBUG(f"检查到用户语言代码为: {user_lang}")

        if user_lang in SUPPORTED_LANG_CODE:
            return user_lang

        main_lang = user_lang.split('_')[0] # 截取主要语言代码

        if main_lang in SUPPORTED_LANG_CODE:
            return main_lang

        for lang_code in SUPPORTED_LANG_CODE:
            if lang_code.startswith(main_lang) :
                return lang_code

        return 'en' # 默认英文
        
    def set_language(self, lang_code):
        """设置应用语言"""
        if lang_code == "zh_cn":
            lang_code = "zh_CN" #暂时特殊处理 等之后全局替换

        # 更新配置
        log.DEBUG(f"切换语言到: {lang_code}")
        
        
        # 移除旧翻译器
        for translator in self.app.findChildren(QTranslator):
            self.app.removeTranslator(translator)
        
        # 加载Qt基础翻译
        qt_translator = QTranslator()
        qt_path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
        if qt_translator.load(f"qt_{lang_code}", qt_path):
            self.app.installTranslator(qt_translator)
            log.DEBUG(f"加载Qt翻译: qt_{lang_code}")
        
        # 加载应用翻译
        app_translator = QTranslator()
        ts_path = "i18n"
        if app_translator.load(f"myapp_{lang_code}", ts_path):
            self.app.installTranslator(app_translator)
            log.DEBUG(f"加载应用翻译: myapp_{lang_code}")
        

        
        # 更新UI
        self.retranslate_all(lang_code)
    
    def retranslate_all(self, lang_code = None):
        """更新所有注册组件的翻译"""
        
        log.DEBUG("开始更新所有组件翻译...")

        
        # 更新所有注册的组件
        for component in self.translatable_components:
            try:
                if hasattr(component, retranslateUi):
                    if self.method_needs_args(getattr(component, retranslateUi)):
                        if lang_code is None:
                            component_name = self.check_component_name(component)
                            raise ValueError(f"component {component_name}.{retranslateUi} 需要参数 但是为空")
                        component.retranslateUi(lang_code)
                    else:
                        component.retranslateUi()
            except Exception as e:
                component_name = self.check_component_name(component)
                log.ERROR(f"翻译错误 {component_name}: {str(e)}")

        
        log.DEBUG("所有组件翻译更新完成")


    def method_needs_args(self, method):
        """检查方法是否需要参数"""
        sig = inspect.signature(method)
        parameters = sig.parameters
        required_params = []

        for param in parameters.values():
            if param.default == inspect.Parameter.empty: # 没有默认值
                if param.kind not in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD):
                # 排除可变参数
                    required_params.append(param)

        if required_params:
            if required_params[0].name == "self" or required_params[0].name == "cls":
                required_params = required_params[1:]

        return len(required_params) > 0

    def check_component_name(self,component) -> str:

        if component.objectName():
            return component.objectName()
        else:
            return component
        
