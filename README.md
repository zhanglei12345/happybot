#### My bot for Telegram

happybot

## Features  

1. /start  -- say hello 
2. /songci	-- Get songci
3. /tangshi	-- Get tangshi
4. echo your text
5. 待开发...

## 利用 Docker 或 Supervisor 部署。

### Docker

* 编写 requirements.txt 和 Dockerfile。

* 构建：`docker build -t happybot:v1 .`

* 运行：`docker run -d --env 'TELEGRAM_TOKEN=XXX' --env 'APPKEY=XXX' happybot:v1`

### Supervisor (不再使用)

* 在VPS服务器上利用Supervisor工具来监控服务进程。编写一个Supervisor的配置文件happybot.conf，存放到/etc/supervisor/conf.d/目录下：
	
	```
	[program:happybot]

	environment = HAPPY_TOKEN="***",HAPPY_APPKEY="***"
	command     = /root/study/happybot/happybot.py
	directory   = /root/study/happybot
	user        = root
	startsecs   = 3

	redirect_stderr         = true
	stdout_logfile_maxbytes = 50MB
	stdout_logfile_backups  = 10
	stdout_logfile          = /root/study/happybot/log/app.log
	```
	
* 在本地开发机上利用 Fabric 来进行自动化部署。编写 fabfile.py。

* 部署：`fab deploy`

## Links

* [极速数据-API申请](http://www.jisuapi.com/)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [DrakeetLoveBot](https://github.com/drakeet/DrakeetLoveBot)

