-- 检测报告表结构
CREATE TABLE IF NOT EXISTS reports (
    report_id VARCHAR(20) PRIMARY KEY,    -- 报告编号（格式：REP-20231005-001）
    report_name TEXT NOT NULL,           -- 报告名称
    testing_unit TEXT NOT NULL,          -- 检测单位
    inspector TEXT NOT NULL,             -- 检测员
    approver TEXT NOT NULL,              -- 批准人
    test_date DATE NOT NULL,             -- 检测时间
    valid_until DATE NOT NULL,           -- 有效时间
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- 生成时间
);

-- 注意：此SQL仅用于记录表结构，实际数据存储在Airtable中
-- 字段说明：
-- report_id: 主键，使用特定格式的报告编号
-- report_name: 报告的名称
-- testing_unit: 进行检测的单位名称
-- inspector: 负责检测的人员
-- approver: 批准报告的人员
-- test_date: 进行检测的日期
-- valid_until: 报告的有效期截止日期
-- created_at: 记录创建时间，自动生成