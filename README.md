#### my bot for Telegram


## Features  

1. /start  -- say hello 
2. /songci	-- Get songci
3. /tangshi	-- Get tangshi
4. echo your text
5. 待开发...

## Deploy

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
	
* 在本地开发机上利用Fabric来进行自动化部署。编写fabfile.py。
* 部署：`fab deploy`

## Links

* [极速数据-API申请](http://www.jisuapi.com/)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* [DrakeetLoveBot](https://github.com/drakeet/DrakeetLoveBot)

