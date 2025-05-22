# Auto-backup-with-navicat
Using navicat to realize batch automatic backup of database

1、先在navicat上创建一个名为：oceanbase-auto-bak 的自动运行任务
![image](https://github.com/user-attachments/assets/f59295d5-0e6e-43b0-9553-2ffe0fe1a304)

2、在这个任务中添加你需要备份的库，然后点击开始测试备份是否正常，若正常就保存下来
![image](https://github.com/user-attachments/assets/2bfffe9b-e9ee-42bd-ab87-8c163dea3bde)

3、配置这个自动运行任务为定时执行，例如配置：每天凌晨1:00开始执行备份
![image](https://github.com/user-attachments/assets/c74cfcee-aa22-432c-8422-aacc270f31da)

4、使用Python3环境启动这个main.py的备份脚本,脚本默认会监听本机的8089端口

注意：Python脚本中navicat的自动备份任务名要配置必须一致，可以改成自己的，一致就行

cd ./Auto-backup-with-navicat/  && ./main.py

5、在命令行访问本机启动的8089端口，触发自动备份（注意token需要带上，可以在脚本中修改成自定义的token）
curl.exe -N "http://127.0.0.1:8089/?token=ssifM7jf40aK6f9isfuwsKBUKMpxRnMp2s3B3tUJINU"
执行结果如下图：
![img_v3_02m7_894f3462-a342-4fed-87cb-c78599c71fbg](https://github.com/user-attachments/assets/4242aba4-f545-4a01-82fd-081a66a01d58)
