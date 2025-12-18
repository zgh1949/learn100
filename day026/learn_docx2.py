from docx import Document

employeeList = [
    {
        'name': '骆昊',
        'id': '100200198011280001',
        'sdate': '2008年3月1日',
        'edate': '2012年2月29日',
        'department': '产品研发',
        'position': '架构师',
        'company': '成都华为技术有限公司'
    },
    {
        'name': '王大锤',
        'id': '510210199012125566',
        'sdate': '2019年1月1日',
        'edate': '2021年4月30日',
        'department': '产品研发',
        'position': 'Python开发工程师',
        'company': '成都谷道科技有限公司'
    },
    {
        'name': '李元芳',
        'id': '2102101995103221599',
        'sdate': '2020年5月10日',
        'edate': '2021年3月5日',
        'department': '产品研发',
        'position': 'Java开发工程师',
        'company': '同城企业管理集团有限公司'
    },
]

for employee in employeeList:
    print("==========================")
    doc = Document('day026/离职证明模板.docx')

    # 遍历所有段落
    for p in doc.paragraphs:
        # 检查段落中是否包含占位符
        if '{' not in p.text:
            continue
            
        # 收集所有run的文本
        runs = p.runs
        if not runs:
            continue
            
        # 构建整个段落的文本，记录每个run的起始位置
        full_text = ""
        run_positions = []
        current_pos = 0
        
        for run in runs:
            run_positions.append((current_pos, current_pos + len(run.text)))
            full_text += run.text
            current_pos += len(run.text)
        
        # 查找所有占位符
        import re
        pattern = r'\{(\w+)\}'
        matches = list(re.finditer(pattern, full_text))
        
        # 从后往前替换，避免位置变化影响
        for match in reversed(matches):
            key = match.group(1)
            placeholder = match.group(0)
            start_pos = match.start()
            end_pos = match.end()
            
            if key in employee:
                # 找到包含占位符的run
                for i, (run_start, run_end) in enumerate(run_positions):
                    # 检查占位符是否在这个run中
                    if run_start <= start_pos < run_end:
                        # 计算在run中的相对位置
                        rel_start = start_pos - run_start
                        rel_end = end_pos - run_start
                        
                        # 替换文本
                        run_text = runs[i].text
                        runs[i].text = run_text[:rel_start] + str(employee[key]) + run_text[rel_end:]
                        break

    doc.save(f'day026/target/{employee["name"]}离职证明.docx')
