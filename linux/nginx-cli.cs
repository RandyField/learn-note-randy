cd 至nginx的目录下

grep nginx

kill -QUIT 6015

kill -HUP 6022

    -c ：使用指定的配置文件而不是 conf 目录下的 nginx.conf 。


    -t：测试配置文件是否正确，在运行时需要重新加载配置的时候，此命令非常重要，用来检测所修改的配置文件是否有语法错误。


    -s reload 重载


    -s stop 停止


nginx启动/重启/停止


    这个很简单，就是运行命令：


    sudo /etc/init.d/nginx {start|restart|stop} 




nginx检查配置


    /usr/local/nginx/sbin/nginx -t nginx.conf


nginx修改配置后重载


    /usr/local/nginx/sbin/nginx -s reload 