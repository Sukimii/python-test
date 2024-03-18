from selenium import webdriver
import sys

if __name__ == "__main__":
    # 获取用户输入的日期和货币代号
    date = sys.argv[1]
    currency_code = sys.argv[2]

    # 打开中国银行外汇牌价网站
    driver = webdriver.Chrome()
    driver.get('https://www.boc.cn/sourcedb/whpj/')

    # 输入日期和选择货币
    driver.find_element_by_id('erectDate').send_keys(date)
    driver.find_element_by_id('pjname').send_keys(currency_code)

    # 点击查询按钮
    driver.find_element_by_css_selector('.inputButton').click()

    # 获取现汇卖出价
    xianhui_sell_price = driver.find_element_by_css_selector('.sell').text

    print(xianhui_sell_price)

    # 关闭浏览器
    driver.quit()