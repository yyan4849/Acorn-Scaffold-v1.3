# glassmore功能文档

# 一、文档说明

该文档主要记录了glassmore产生的背景，需求范围，以及根据需求范围作出的设计和实现方案，并对每一个功能模块进行了详细的描述。

# 二、需求背景

# 三、需求详情

| 需求                             | 简要说明                                               |
| -------------------------------- | ------------------------------------------------------ |
| 提供网页初始化                   | 用户可以通过cli命令自动初始化网站安装本地UI库          |
| 在官网(localhost)查找glassmore库 | 用户可以在本地打开glassmore-ui官网，查找需求组件和特效 |
| 使用封装好的组件库               | 通过选中组件的部署按钮，组件被导入component文件夹      |
| 使用预设的效果库                 | 在glassmore-ui官网，挑选需要的效果可以全局调用         |

# 四、功能详情

1. ## 组件库部分

| 组件名         | 属性         | 功能                   |
| -------------- | ------------ | ---------------------- |
| button         | circle/plain | 属性为circle时，按钮为 |
|                |              |                        |
| disabled       |              |                        |
|                |              |                        |
| btn-group      | disabled     |                        |
| radio(border)  | disabled     |                        |
| text-color     |              |                        |
| radio-group    | disabled     |                        |
| checkbox       | min          |                        |
| max            |              |                        |
| text-color     |              |                        |
| disabled       |              |                        |
| checkbox-group | disabled     |                        |
| switch         | disabled     |                        |
| active-color   |              |                        |
| inactive-color |              |                        |
| input          | disabled     |                        |
| inputNumber    | disabled     |                        |
| message        | error(red)   |                        |
| success(green) |              |                        |
| card           | shadow       |                        |
| dialog         | disabled     |                        |

组件：xxxx

功能：xxxx

attrs: x





1. ## 官网部分

官网由三个部分组成，导航栏部分，组件效果预览展示部分，以及相应组件的属性列表

| 模块     | 功能                     | 功能详细说明 |
| -------- | ------------------------ | ------------ |
| 导航栏   | 实现各组件页面之间的跳转 |              |
| 效果展示 | 展示效果并提供部署       |              |
| 属性列表 | 展示组件所包含的属性     |              |



1. ## CLI及服务器部分

| 模块        | 功能              | 功能详情                                                     |
| ----------- | ----------------- | ------------------------------------------------------------ |
| 搭建vue项目 | 自动化搭建vue项目 | 通过cli命令初始化vue项目，可选项除了基础库以外，额外提供本地glassmore组件库，工具库 |
|             |                   |                                                              |

- 本地CLI UI  组件库，工具库快速导入vue项目
- vite-vue-cli  提供多类选项（vuex jsx mock）vue3.2支持最新功能
- 原生库 http  缩小体积
- 自动检测端口和错误命令
- 自定义导入工具包