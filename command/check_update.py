import os
import requests
from my_decorator.decorator import begin_and_finish_time_log
from my_log.my_log import my_log
import re
from packaging import version

API_URL="https://api.github.com/repos/233dada/AhabAssistantLimbusCompany/releases/latest"
local_version="" 

@begin_and_finish_time_log(task_name="检查更新")
def check_update():
    global local_version
    if local_version == "":
        my_log("info", f"当前版本号为空, 如果你是从Github上下载的请联系开发者")
        return
    try:
        # 尝试获取 GitHub 最新版本信息
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # 如果状态码不为 200，会抛出 HTTPError
    except requests.exceptions.RequestException as e:
        # 捕获网络相关的异常并记录日志
        my_log("warning", f"无法检测更新，请检查网络连接: {e}")
        return

    try:
        # 尝试解析返回的 JSON 数据
        release_data = response.json()
    except ValueError:
        my_log("error", "无法解析 GitHub API 的响应数据")
        print("更新检查失败，数据解析错误")
        return

    # 查找 .7z 文件的下载链接
    download_url = None
    for asset in release_data.get('assets', []):
        if asset['name'].endswith('.7z'):
            match = re.search(r'AALC_(.+)\.7z', asset['name'])
            if match:
                current_version = match.group(1)
                if current_version == local_version:
                    my_log("info", f"当前版本为最新版本：{current_version}")
                    return
                elif version.parse(current_version.lstrip('Vv')) < version.parse(local_version.lstrip('Vv')):
                    my_log("info", f"当前版本高于最新版本：{current_version}")
                else:
                    my_log("info", f"本地版本为 {local_version}, 低于云端版本{current_version}")
                    download_url = asset['browser_download_url']
                    break

    else:
        # 如果循环结束后没有找到下载链接
        my_log("info", "未找到更新文件 (.7z)")
        print("未找到更新文件 (.7z)")
        return
    if download_url:
        file_name = download_url.split('/')[-1]  # 提取文件名
        my_log("info", f"正在下载 {file_name} ...")
        print(f"正在下载 {file_name} ...")

        try:
            # 下载文件
            with requests.get(download_url, stream=True, timeout=60) as r:
                r.raise_for_status()
                with open(file_name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print(f"下载完成，请手动解压 {file_name} 完成更新")
            my_log("info", f"下载完成：{file_name}")
        except requests.exceptions.RequestException as e:
            my_log("error", f"文件下载失败: {e}")
            print(f"文件下载失败，请检查网络连接或下载链接：{e}")
    else:
        my_log("warning", "未找到有效的下载链接")
        print("未找到有效的下载链接")

    return