from pathlib import Path

project_root = Path(__file__).parent.parent
app_apk = f'{project_root}\whatsapp.apk'
appium_server = "http://127.0.0.1:4723/wd/hub"  # URL to appium server
device_platform = "Android"
system_port = 8251
app_package = "com.whatsapp"
app_activity = ".Main"
home_activity = ".HomeActivity"
app_file = "whatsapp.apk"
no_reset = True
device_name = 'GalaxyA7'
device_udid = "5210e1c5b6a0a497"
bulk_message = "با آرزوی سالی سرشار از شادی و موفقیت، پیشاپیش فرارسیدن نوروز را به شما تبریک عرض می نمایم. / ارادتمند شما محمد منفرد"
