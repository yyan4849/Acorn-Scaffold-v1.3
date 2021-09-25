glassmore功能文档

> Glassmore ui-毛玻璃效果的UI组件库

# 一、文档说明

该文档主要记录了glassmore产生的背景，需求范围，以及根据需求范围作出的设计和实现方案，并对每一个功能模块进行了详细的描述。

# 二、需求背景

在 2020 年 11 月有关毛玻璃效果的第一篇设计文章面世之后，这一风格由此成为了一种全新的UI设计趋势。它最明显的特征是：

- 透明度（使用背景模糊的磨砂玻璃效果）

- 物体漂浮在空间中的多层方法

- 鲜艳的色彩突出了模糊的透明度

- 半透明物体上的微妙轻边框。

这种垂直性以及您可以通过它看到的事实意味着用户可以建立界面的层次结构和深度。他们只是看哪一层在哪一层上面，就像*虚拟玻璃*碎片一样。这样的设计效果在微软的 Fluent 设计系统以及Mac OS Big Sur系统设计中都有涉及。

但是在做了简单的竞品分析后，我们发现，现存的UI组件库没有涉及到这一流行的毛玻璃效果，即使用户可以到一些毛玻璃的网站复制整段的代码，但是这样重复的操作无疑加重了程序员们的工作时间，降低了效率，所以我们希望自己封装一个毛玻璃效果的组件库让程序员可以在可视化的界面选择相应的组件一键部署。

总需求概括为将前端项目模块化，自动化，提升开发效率，保证开发质量，降低开发成本。

# 三、 技术栈及成员简介

1. ## 技术栈

Vue3; element-plus

2. ## 人员简介

| 组件库   |      |
| -------- | ---- |
| 官网     |      |
| cli      |      |
| 需求文档 |      |

# 四、需求详情

| 需求                             | 简要说明                                               |
| -------------------------------- | ------------------------------------------------------ |
| 提供网页初始化                   | 用户可以通过cli命令自动初始化网站安装本地UI库          |
| 在官网(localhost)查找glassmore库 | 用户可以在本地打开glassmore-ui官网，查找需求组件和特效 |
| 使用封装好的组件库               | 通过选中组件的部署按钮，组件被导入component文件夹      |
| 使用预设的效果库                 | 在glassmore-ui官网，挑选需要的效果可以全局调用         |

# 五、功能详情

1. ## 组件库部分

   <table>
     <tr>
       <th>组件名</th>
       <th>属性</th>
       <th>功能</th>
     </tr>
     <tr>
     	<td rowspan="2">button</td>
     	<td>normal/rect(boolean)</td>
     	<td rowspan="2">属性为normal时，按钮为圆角按钮；属性为rect时，按钮为长方形按钮；属性为disabled表示当前按钮不可点击。</td>
     </tr>
     <tr>
       <td>disabled(boolean)</td>
     </tr>
     <tr>
       <td>btn-group</td>
       <td>disabled(boolean)</td>
       <td>btn-group内必须放button，属性为disabled表示当前这组按钮不可点击。</td>
     </tr>
     <tr>
     	<td rowspan="2">radio(border)</td>
       <td>disabled(boolean)</td>
       <td rowspan="2">在一组备选项中进行单选。属性text-color表示按钮形式的 Radio 激活时的文本颜色；属性为disable的时候表示当前按钮不可点击。</td>
     </tr>
     <tr>
       <td>text-color(str)</td>
     </tr>
     <tr>
       <td>radio-group</td>
       <td>disabled(boolean)</td>
       <td>radio-group内必须放button，属性为disabled表示当前这组单选组不可点击。</td>
     </tr>
     <tr>
     	<td rowspan="2">checkbox</td>
       <td>disabled(boolean)</td>
       <td rowspan="2">一组备选项中进行多选。属性为disabled表示当前checkbox不可选；text-color表示			checkbox激活时文本颜色。</td>
     </tr>
     <tr>
       <td>text-color(str)</td>
     </tr>
     <tr>
     	<td rowspan="3">checkbox-group</td>
       <td>min(number)</td>
       <td rowspan="3">属性min用来表示在checkbox-group中可被勾选的checkbox的最小数量；属性max用来表			示在checkbox-group中可被勾选的checkbox的最大数量；
   			当属性为disable时，checkbox-group不可用。属性为disable的时候表示当前checkbox-group不可点			击。
   	</td>
     </tr>
     <tr>
       <td>max(number)</td>
     </tr>
     <tr>
       <td>disabled(boolean)</td>
     </tr>
     <tr>
     	<td rowspan="3">switch</td>
       <td>active-color(str)</td>
       <td rowspan="3">表示两种相互对立的状态间的切换，多用于触发「开/关」。属性active-color属性表示			switch打开时的背景颜色；属性inactive-color表示switch关闭时的背景颜色；属性为disable的时候表示当		前switch不可点击。
   	</td>
     </tr>
     <tr>
       <td>inactive-color(str))</td>
     </tr>
     <tr>
       <td>disabled(boolean)</td>
     </tr>
     <tr>
       <td>input</td>
       <td>disabled(boolean)</td>
       <td>通过鼠标或键盘输入字符。属性为disabled的时候表示当前input不可使用。</td>
     </tr>
     <tr>
       <td>inputNumber</td>
     	<td>disabled(boolean)</td>
       <td>属性为disabled的时候表示当前inputNumber不可使用</td>
     </tr>
      <tr>
       <td>message</td>
     	<td>type(str): error(red)/success(green)/default(white)</td>
       <td>常用于主动操作后的反馈提示。属性type用来定义改message的类型，提供error和success和默认透明玻				璃选项。</td>
     </tr>
     <tr>
       <td>card</td>
     	<td>shadow(str):always/hover/never</td>
       <td>将信息聚合在卡片容器中展示。属性shadow用来定以卡片阴影出现的时机，默认为never。</td>
     </tr>
      <tr>
       <td>dialog</td>
     	<td>disabled(boolean)</td>
       <td>属性为disabled的时候表示当前dialog不可使用。</td>
     </tr>

   

   </table>

   

3. ## 官网部分

官网由三个部分组成，导航栏部分，组件效果预览展示部分，以及相应组件的属性列表

| 模块     | 功能                     | 功能详细说明                                                 |
| -------- | ------------------------ | ------------------------------------------------------------ |
| 导航栏   | 实现各组件页面之间的跳转 | 通过点击导航栏中的组件名称跳转到相应组件介绍页面。           |
| 效果展示 | 展示效果并提供部署       | 用来展示组件各个属性的效果。                                 |
| 属性列表 | 展示组件所包含的属性     | 用来列出组件的相关属性代码，并且提供一件部署功能：点击部署按钮，自动导入组件进入component文件。 |



3. ## CLI及服务器部分

| 模块          | 功能                               | 功能详情                                                     |
| ------------- | ---------------------------------- | ------------------------------------------------------------ |
| 搭建vue项目   | 自动化搭建vue项目                  | 通过cli命令初始化vue项目，可选项除了基础库以外，额外提供本地glassmore组件库，工具库。 |
| localhost服务 | 提供本地服务                       | 通过cli命令启用本地服务，localhost 查看 glassmore-ui官网，vue工程预览。 |
| vite-vue-cli  | 提供多类选项（vue3.2支持最新功能） | 用户可以在vite-vue-cli内选择包括vuex, jsx, mock在内的功能。  |

- 本地CLI UI  组件库，工具库快速导入vue项目
- vite-vue-cli  提供多类选项（vuex jsx mock）vue3.2支持最新功能
- 原生库 http  缩小体积
- 自动检测端口和错误命令
- 自定义导入工具包
