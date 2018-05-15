# First docker file from bolingcavalry
# VERSION 0.0.1
# Author: yuyilun

#基础镜像
FROM nginx:stable

#作者
MAINTAINER yuyilun <773778632@qq.com>

#定义工作目录
ENV WORK_PATH /etc/nginx

#定义conf文件名
ENV CONF_FILE_NAME nginx.conf

#删除原有配置文件
RUN rm $WORK_PATH/$CONF_FILE_NAME

#复制新的配置文件
COPY ./$CONF_FILE_NAME $WORK_PATH/

#给shell文件赋读权限
RUN chmod a+r $WORK_PATH/$CONF_FILE_NAME