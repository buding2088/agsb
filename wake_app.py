import time
from playwright.sync_api import sync_playwright

# 1. 替换为你的 Streamlit 应用真实 URL
APP_URL = "https://chyuy2rgszgsw6xrujaqvv.streamlit.app"

def wake_up():
    with sync_playwright() as p:
        # 启动无头浏览器
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print(f"正在打开应用页面: {APP_URL}")
        page.goto(APP_URL, timeout=60000)
        
        # 等待页面基础元素加载
        time.sleep(8)
        
        # 查找是否有 "Wake it up" 唤醒按钮
        # Streamlit 睡眠页面的按钮通常叫 "Wake it up" 或包含该文字
        wake_button = page.locator('button:has-text("Wake it up")')
        
        if wake_button.count() > 0 and wake_button.is_visible():
            print("检测到应用已睡眠，正在点击 'Wake it up' 按钮唤醒...")
            wake_button.click()
            # 唤醒启动容器需要一些时间，等待 20 秒确保容器加载完成
            time.sleep(20)
            print("唤醒指令已发送完成！")
        else:
            print("应用当前处于活跃状态（未睡眠），无需唤醒。")
            
        browser.close()

if __name__ == "__main__":
    wake_up()
