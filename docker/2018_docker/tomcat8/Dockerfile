# First docker file from bolingcavalry
# VERSION 0.0.1
# Author: bolingcavalry

#基础镜像
FROM tomcat:8-jre8

#作者
MAINTAINER yuyilun <773778632@qq.com>

#定义工作目录
ENV WORK_PATH /usr/local/tomcat/conf

#定义要替换的文件名
ENV USER_CONF_FILE_NAME tomcat-users.xml

#定义要替换的server.xml文件名
ENV SERVER_CONF_FILE_NAME server.xml

#定义上传文件
ENV MANAGER_FILE_NAME manager.xml

#删除原文件tomcat-users.xml
RUN rm $WORK_PATH/$USER_CONF_FILE_NAME

#复制文件tomcat-users.xml
COPY  ./$USER_CONF_FILE_NAME $WORK_PATH/

#删除原文件server.xml
RUN rm $WORK_PATH/$SERVER_CONF_FILE_NAME

#复制文件server.xml
COPY  ./$SERVER_CONF_FILE_NAME $WORK_PATH/

#复制文件manager.xml，增加远程访问
COPY ./$MANAGER_FILE_NAME $WORK_PATH/Catalina/localhost/
