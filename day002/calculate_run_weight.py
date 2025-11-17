running_visit_count = 1200 # 执行阶段合同访视次数
start_site_count = 3 # 合同启动中心数
ssu = 5
study_coefficient = 41.152 # 项目系数（按实际工作量分配）
phone_visit_count = 308 # 电话访视次数
phone_coefficient = 0.13 # 电话访视系数

running_weight = (running_visit_count * study_coefficient * 0.95)  \
    / ((start_site_count * (ssu - 1) + running_visit_count) * study_coefficient 
        + phone_visit_count * phone_coefficient)

print("执行阶段权重", running_weight)




running_visit_count = 1200 # 执行阶段合同访视次数
start_site_count = 3 # 合同启动中心数
ssu = 5
study_coefficient = 41.152 # 项目系数（按实际工作量分配）
phone_visit_count = 308 # 电话访视次数
phone_coefficient = 0.13 # 电话访视系数

phone_weight = (phone_visit_count * phone_coefficient * 0.95)  \
    / ((start_site_count * (ssu - 1) + running_visit_count) * study_coefficient 
        + phone_visit_count * phone_coefficient)

print("电话阶段权重", phone_weight)


# 启动进度
site_count_actual = 1 # 累计已启动中心数
site_count = 1  # 合同启动中心数

start_process = site_count_actual / site_count
print("启动进度", start_process)

# 执行进度
visit_count = 1 #累计随访总次数
phone_count = 1 #累计电话总次数
running_visit_count #执行阶段合同访视次数

running_process = (visit_count - phone_count) / running_visit_count
print("执行进度", running_process)

# 电话访视进度
phone_visit_count_actual = 1 # 累计电话随访总次数
phone_visit_count = 1 # 电话合同访视次数
phone_process = phone_visit_count_actual / phone_visit_count

print("电话访视进度", phone_process)

# 关中心进度
actual_close_count = 1
actual_start_count = 1

close_process


