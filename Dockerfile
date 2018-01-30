FROM microsoft/dotnet
WORKDIR /app
COPY  ./Publish .

#配置容器启动后执行的命令,并且不可被docker run提供的参数覆盖
ENTRYPOINT [ "dotnet","Web.dl" ]