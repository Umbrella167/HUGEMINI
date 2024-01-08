# HUGEMINI

## 项目描述

该项目是对Gemini提供的API创建的web服务，可以通过web界面来更方便地使用Gemini模型。

## 命名规则

- 变量、函数：全小写+下划线命名法
- 全局变量（Config）：全大写+下划线命名法
- 类：大驼峰命名法

## 接口描述

### website.py

- `/`
  methods：GET、POST
  function：Index()
  功能：跳转去`/Chat`
- `/Chat`
  methods：GET、POST
  function：Chat()
  功能：新建对话界面
- `/chat/<conversation_id>`
  methods：GET、POST
  function：Chat()
  功能：指定conversation_id的对话界面

### backend.py

- 

## 模板描述

### index.py

