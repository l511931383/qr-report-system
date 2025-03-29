import os
import sys

# 添加应用目录到Python路径
project_home = '/home/l511931383/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 导入环境变量
from dotenv import load_dotenv
load_dotenv(os.path.join(project_home, '.env'))

# 导入Flask应用
from flask_app import app as application