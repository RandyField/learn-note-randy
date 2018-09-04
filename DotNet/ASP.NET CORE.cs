dotnet new [classlib,web,mvc,angular,react,webapi,globaljson,nugetconfig,sln]

/* 
--------------------------------------------发布 
发布.net core :dotnet publish -c Release -o ./Publish

Options:
  -h, --help                            Show help information.---帮助
  -o, --output <OUTPUT_DIR>             Output directory in which to place the published artifacts.---发布的文件输出的目录

  要发布的目标框架。目标框架必须在项目文件中指定。
  -f, --framework <FRAMEWORK>           Target framework to publish for. The target framework has to be specified in the project file.

  为给定的运行时发布项目。在创建自包含部署时使用此选项。默认是发布一个与框架依赖的应用程序。
  -r, --runtime <RUNTIME_IDENTIFIER>    Publish the project for a given runtime. This is used when creating self-contained deployment. 
  										Default is to publish a framework-dependent app.
  
  用于构建项目的配置。大多数项目的默认值是“调试”。
  -c, --configuration <CONFIGURATION>   Configuration to use for building the project.  Default for most projects is  "Debug".
  --version-suffix <VERSION_SUFFIX>     Defines the value for the $(VersionSuffix) property in the project.
  --manifest <manifest.xml>             The path to a target manifest file that contains the list of packages to be excluded from the publish step.
  --self-contained                      Publish the .NET Core runtime with your application so the runtime doesn't need to be installed on the target machine. Defaults to 'true' if a runtime identifier is specified.
  --no-restore                          Does not do an implicit restore when executing the command.
  -v, --verbosity                       Set the verbosity level of the command. Allowed values are q[uiet], m[inimal], n[ormal], d[etailed], and diag[nostic].
  --no-dependencies                     Set this flag to ignore project to project references and only restore the root project.
  --force                               Set this flag to force all dependencies to be resolved even if the last restore was successful. This is equivalent to deleting project.assets.json.
 */


/* 
--------------------------------------------------------发布到指定运行时
dotnet publish -r 1.0.0 -o ./rpublish
Microsoft (R) Build Engine version 15.5.180.51428 for .NET Core
Copyright (C) Microsoft Corporation. All rights reserved.

  Restoring packages for /home/randy/vscode/github/.net-core-mvc-vscode-debug-ubuntu/firstapp.csproj...
  Restore completed in 50.82 ms for /home/randy/vscode/github/.net-core-mvc-vscode-debug-ubuntu/firstapp.csproj.
  Restore completed in 647.76 ms for /home/randy/vscode/github/.net-core-mvc-vscode-debug-ubuntu/firstapp.csproj.
/usr/share/dotnet/sdk/NuGetFallbackFolder/microsoft.netcore.app/2.0.0/build/netcoreapp2.0/Microsoft.NETCore.App.targets(19,5): error : Project is targeting runtime '1.0.0' but did not resolve any runtime-specific packages for the 'Microsoft.NETCore.App' package.  This runtime may not be supported by .NET Core. [/home/randy/vscode/github/.net-core-mvc-vscode-debug-ubuntu/firstapp.csproj]
 
 */