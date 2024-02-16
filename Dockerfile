# 使用官方Python镜像作为基础镜像
FROM python:3.8
# 设置工作目录
WORKDIR /app
# 将所有文件复制到工作目录
COPY . .
# 安装依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
# 暴露应用程序运行的端口
EXPOSE 5050
# 运行应用程序
CMD [ "python", "run.py" ]