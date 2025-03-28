import os
from dotenv import load_dotenv
from app import app

# 加载环境变量
load_dotenv()

# 配置生产环境变量
os.environ['FLASK_ENV'] = 'production'

# 应用入口
if __name__ == '__main__':
    app.run()