running_visit_count = 1200  # 执行阶段合同访视次数

contract_start_site_count = 3  # 合同启动中心数
contract_phone_visit_count = 308  # 合同电话访视次数

ssu_coefficient = 5
study_coefficient = 41.152  # 项目系数（按实际工作量分配）
phone_coefficient = 0.13  # 电话访视系数

cumulative_initial_site_count = 5  # 累计已启动中心数
cumulative_close_site_count = 3  # 累计已关闭中心数
cumulative_visit_count = 88  # 累计随访总次数
cumulative_phone_visit_count = 0  # 累计电话随访总次数

print("---权重---")

# 公共分母
denominator = (contract_start_site_count * (ssu_coefficient - 1) + running_visit_count) \
       * study_coefficient  \
       + contract_phone_visit_count * phone_coefficient
print("公共分母",denominator)

# ssu权重
ssu_weight = (contract_start_site_count * (ssu_coefficient - 1) * study_coefficient * 0.95)  / denominator
print("SSU权重%.6f" % ssu_weight)


# 执行权重
running_weight = (running_visit_count * study_coefficient * 0.95)  \
    / denominator
print("执行阶段权重%.6f" % running_weight)


# 电话权重
phone_weight = (contract_phone_visit_count * phone_coefficient * 0.95)  \
    / denominator
print("电话阶段权重%.6f" % phone_weight)

# 关中心权重
close_weight = 0.05
print("关中心权重%.6f" % close_weight)


print("---进度---")

# 启动进度
start_process = cumulative_initial_site_count / contract_start_site_count
print("启动进度%.6f" % start_process)

# 执行进度
running_process = (cumulative_visit_count - cumulative_phone_visit_count) / running_visit_count
print("执行进度%.6f" % running_process)

# 电话访视进度
phone_process = cumulative_phone_visit_count / contract_phone_visit_count
print("电话访视进度%.6f" % phone_process)

# 关中心进度
close_process = cumulative_close_site_count / cumulative_initial_site_count
print("关中心进度%.6f" % close_process)


print("---总进度---")

# 本月项目进度
process = start_process * ssu_weight \
    + running_process * running_weight \
    + phone_process * phone_weight \
    + close_process * close_weight

print("本月项目进度%.6f" % process)
