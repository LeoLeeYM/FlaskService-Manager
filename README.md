<h2 align="center">⭐ 欢迎使用 FlaskService Manager ⭐<h2/>
<p align="center" style="font-weight">🌹 这是一款专用于 Python Flask 服务器的管理平台 <p/>


## 项目起源

这个项目是因为我最近一直在负责我的社团服务器后台的开发和管理，我们的服务主要用Flask搭建，由于部分服务的特殊性，我们服务器用的是Windows Server，在Windows Server上运行Flask服务器一般就是直接运行.py文件（我没找到更好的办法，应该是我的问题，感谢大佬们可以支招），久而久之服务多了后台就乱七八糟不知道那个命令行窗口对应哪一个服务。

后来实在烦的不行，就自己鼓捣了一个Flask服务器管理器~



## 项目介绍

该项目使用 Flask + Vue + element 开发，采用前后端分离的开发模式，在服务器端部署后端服务，可在前端页面实现 Flask 服务器的添加、运行、关闭、编辑等功能，可以在前端实时查看每一个服务器的 Log 输出。

项目自带登录鉴权功能，登录用户名密码在 `fs-manage-Service/configs/config.json` 修改。

- 默认用户名：admin

- 默认密码：password

#### 未来计划

[✗] 可视化编辑 Flask 服务器的配置项

[✗] 提供简单的代码编辑器功能，允许直接编辑服务器代码

[✗] Log 输出的高亮显示

[✗] 提供服务器的定时重启、定时开关功能

待续补充...



## 项目部署

### 安装依赖

前端项目：进入`flask-service-manager`文件夹

```shell
npm install
```

后端项目：进入`fs-manage-Service`文件夹

```shell
pip install -r requirements.txt
```

### 运行项目

**后端项目**

- Windows

  - 直接运行 `processManage.py`

- Linux & MacOS

  - ```shell
    nohup python3 processManage.py &
    ```

**前端项目**

- 配置

  - 在运行前端项目前需要进行配置，打开前端项目的 `./src/utils/request.js` 文件，找到以下代码

  - ```javascript
    const service = axios.create({
      // axios中请求配置有baseURL选项，表示请求URL公共部分
      baseURL: "your server url (如 http://10.xx.xx.xx:6060)",
      // 超时
      timeout: 10000
    })
    ```

  - 将 `baseURL` 修改为你服务器的实际地址

- 开发调试

  - ```shell
    npm run serve
    ```

- 部署

  - ```shell
    npm run build
    ```

  - 将生成的 `./dict` 文件夹部署至服务器中（如nginx）
