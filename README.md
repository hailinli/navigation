# 脚本介绍
**功能介绍**

抓取 http://www.ais.msa.gov.cn/hsj/ 网站中船只航行数据

**实现方式**

利用google chrome://chrome-urls/中的chrome://net-internals/#events记录google浏览器访问记录功能记录下访问过的请求。而后写python脚本去请求这些历史请求，并解析返回的数据，从而不用自己去构造请求。


# 脚本使用

1. 开启google事件页

    记录访问请求历史：浏览器里打开以下页面
    ```
    chrome://net-internals/#events
    ```
2. 进入网址访问数据
    - 进入网站 http://www.ais.msa.gov.cn/hsj/
    - 登录: 用户名:lijun3161239,密码:lijun870321234
    - 点击右边展开，
    - 选择画自定义区域，选择区域
    - 点击三角键运行
    - 选择时间运行
    
3. 航海网站数据播放完后，将`chrome://net-internals/#events`对应的页面另存为以`net-internals`开头命名的文件

4. 并把它放到 navigation/data目录下

5. 运行脚本
    ```
    python get_navigation_req.py
    ```

# 依赖环境
1. python3.6.0 （>3.0就行）
2. lxml 4.2.0（不用关心特别版本）
3. requests 2.18.4（不用关心特定版本）

