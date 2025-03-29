# 部署指南

## 前端部署（GitHub Pages）

1. 创建GitHub仓库
   - 在GitHub上创建新仓库
   - 将本地代码推送到仓库：
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin <你的仓库URL>
   git push -u origin main
   ```

2. GitHub Pages配置
   - 仓库已配置自动部署工作流（.github/workflows/deploy.yml）
   - 推送代码到main分支后会自动部署到gh-pages分支
   - 在仓库设置中启用GitHub Pages，选择gh-pages分支作为源

## 后端部署（PythonAnywhere）

1. 注册PythonAnywhere账号
   - 访问 https://www.pythonanywhere.com 注册免费账号

2. 上传代码
   - 在PythonAnywhere的Files页面创建新目录
   - 上传以下文件：
     - app.py
     - wsgi.py
     - requirements.txt
     - .env（包含必要的环境变量）

3. 安装依赖
   - 打开PythonAnywhere的Bash终端
   - 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. 配置Web应用
   - 在Web页面点击Add a new web app
   - 选择Python版本和Flask框架
   - 配置WSGI文件路径为wsgi.py
   - 设置虚拟环境路径
   - 配置静态文件映射（如需要）

5. 环境变量配置
   在.env文件中设置以下变量：
   ```
   AIRTABLE_API_KEY=你的Airtable API密钥
   AIRTABLE_BASE_ID=你的Airtable Base ID
   AIRTABLE_TABLE_NAME=你的表格名称
   BASE_URL=你的GitHub Pages URL
   FLASK_ENV=production
   ```

6. 更新前端配置
   - 修改前端API请求地址为PythonAnywhere的URL
   - 确保CORS配置正确

## 测试部署

1. 访问GitHub Pages URL测试前端
2. 测试API接口连通性
3. 验证二维码生成和报告查询功能

## 注意事项

- 确保所有敏感信息（API密钥等）都通过环境变量配置
- 定期备份数据和代码
- 监控应用性能和错误日志
- 根据需要调整PythonAnywhere的配置参数