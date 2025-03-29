# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS
from airtable import Airtable
from dotenv import load_dotenv
import os
import requests
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 加载环境变量
load_dotenv()

# 初始化Flask应用
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)  # 启用CORS跨域支持

# 添加根路由重定向到query.html
@app.route('/')
def index():
    return app.send_static_file('query.html')

# Airtable配置
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY')
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME')

# 初始化Airtable客户端
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)

# QR Code生成API
QR_CODE_API = 'https://api.qrserver.com/v1/create-qr-code/'

@app.route('/get_report/<string:report_number>', methods=['GET'])
def get_report(report_number):
    try:
        logger.info(f'正在查询报告编号: {report_number}')
        
        # 首先尝试从测试数据中获取报告
        import json
        try:
            with open('test_data.json', 'r', encoding='utf-8') as f:
                test_data = json.load(f)
                for report in test_data['reports']:
                    if report['报告编号'] == report_number:
                        logger.info('从测试数据中找到报告')
                        report_data = report
                        break
                else:
                    report_data = None
        except Exception as e:
            logger.error(f'读取测试数据出错: {str(e)}')
            report_data = None
            
        # 如果测试数据中没有找到，则尝试从Airtable获取
        if not report_data:
            # 检查Airtable配置
            if not all([AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME]):
                logger.error('Airtable配置不完整')
                return jsonify({
                    'status': 'error',
                    'message': 'Airtable配置错误'
                }), 500
                
            # 查询Airtable数据
            records = airtable.search('报告编号', report_number)
            
            if not records:
                return jsonify({
                    'status': 'error',
                    'message': '未找到报告'
                }), 404
                
            # 获取第一条匹配记录
            report_data = records[0]['fields']
            
        if not report_data:
            return jsonify({
                'status': 'error',
                'message': '未找到报告'
            }), 404
        
        # 生成二维码URL
        base_url = os.getenv('BASE_URL')
        report_url = f'{base_url}/report.html?number={report_number}'
        qr_code_url = f'{QR_CODE_API}?size=200x200&data={report_url}'
        
        return jsonify({
            'status': 'success',
            'data': {
                'report': report_data,
                'qr_code_url': qr_code_url
            }
        })
        
    except Exception as e:
        logger.error(f'处理请求时发生错误: {str(e)}')
        return jsonify({
            'status': 'error',
            'message': '服务器内部错误'
        }), 500

if __name__ == '__main__':
    app.run()