# 该文件为综述文件，用于：
# 1.题目表述的变量和公式
# 2.流程的转义实现
# 3.其他数据层面
#

# 各变量含义

# edge：道路线
# name	路段名
# id	边序号
# length	路段长度li
# dir	方向：0为双向，1为s→e，2为e→s
# highway	道路等级：1快速路，2主干路，3次干路，4支路
# s_id	起始节点id
# e_id	终止节点id
# key	关键路段：0否，1是

# junction1：路段节点
# Node_id	节点序号
# Pos_x	x坐标
# Pos_y	y坐标
# Key_node	关键节点：0否，1是
# Damage_i	Damage值
# Time_i	交叉口信号周期
# Lamata_i	交叉口直行绿信比
# Cross_i	交叉口直行通行能力
# Land_use	土地利用：1住宅商用，2其他
# key=1	按模型计算Td
# key=0	最短路径经过节点需要加△T的时长，△T=5s

# junction2：分裂节点，即道路的岔路口
# id	分裂节点序号，1上，2左，3下，4右
# o_id	对应原始节点序号
