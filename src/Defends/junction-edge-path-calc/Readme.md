# 该项目在交付的时候被店家强行停止，无法联系客户

> 
>
> 通过既定算法实现线段Edge和节点JunctionNode及其Child的各段耗时

## 需求分析

### 内容分析

1. 定义量字典

1.1 定义主数据

1.1.1 定义 Edge列表及其相应属性

1.1.2 定义 JunctionNode列表及其属性

1.1.3 定义 JunctionChildNode列表及其属性

1.2 定义常量数据

1.2.1 定义 EdgeHighway及其对应值

1.2.2 定义 EdgeKey及其对应布尔

1.2.3 定义常量 α1 α2 β1 β2 vf γ1




2. 模块一实现

2.1 输入 x拔

2.2 开始枚举道路Edge从index=0到index=EdgeLength

      并根据输入和常量case定义η1(index) η2(index)

2.3 定义中间变量x(index) = η1(index) · η2(index) · x拔

2.4 定义行进速度v(index) = x(index)≤γ1，是则返回 α1-β1 · x(index)，否则返回 vf/(1+α2·(x(index) ^ β2 ))

2.5 result(index) = 道路长度l(index) / v(index)



3. 模块二实现

3.1 输入 x拔

3.2 开始枚举节点JunctionNode从index=0到index=JunctionLength
      根据x(index)的key=1决定走向A和走向B

3.3 走向A

3.3.1 根据x拔≤γ2决定走向A1和走向A2从而得到x(index)

3.3.2 根据x拔≤γ2决定走向A3和走向A4从而得到result(index)

3.3.3 根据JunctionChildNode列表的子节点位置关系（西北东南对应 v1 v2 v3 v4）

         判断是左转还是直行还是右转，从而得到η3，定义delay(index) =η3 · result(index)

3.4 走向B result(index)直接定义为5



4. 模块三实现 略，本项目不实现



5. 实现方式及要求

5.1 能够在Python3.6运行通过

5.2 用户能够自定义所有变量和常量以及输入项的值

### 结构定义
**各变量含义**

Edge.edge：道路线

Edge.name	路段名

Edge.id	边序号

Edge.length	路段长度li

Edge.dir	方向：0为双向，1为s→e，2为e→s

Edge.highway	道路等级：1快速路，2主干路，3次干路，4支路

Edge.s_id	起始节点id

Edge.e_id	终止节点id

Edge.key	关键路段：0否，1是



JunctionNode：路段节点

JunctionNode.Node_id	节点序号

JunctionNode.Pos_x	x坐标

JunctionNode.Pos_y	y坐标

JunctionNode.Key_node	关键节点：0否，1是

JunctionNode.Damage_i	Damage值

JunctionNode.Time_i	交叉口信号周期

JunctionNode.Lamata_i	交叉口直行绿信比

JunctionNode.Cross_i	交叉口直行通行能力

JunctionNode.Land_use	土地利用：1住宅商用，2其他

JunctionNode.key=1	按模型计算Td

JunctionNode.key=0	最短路径经过节点需要加△T的时长，△T=5s




JunctionChildNode：分裂节点，即道路的岔路口

JunctionChildNode.id	分裂节点序号，1上，2左，3下，4右

JunctionChildNode.o_id	对应原始节点序号