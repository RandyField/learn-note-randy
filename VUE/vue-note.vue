
<template>
	
</template>

<script>

var app=new Vue({
	el:'#',
	data:{
		message:
	},
	methods:{
		functionname:function(){
			this.message
		}
	}
	
});

// v-bind
// v-if
// v-else
// v-else-if
// v-for
// v-on
// v-model
// v-once
// v-html

//设置npm国内淘宝镜像
// npm install -g cnpm --registry= https://registry.npm.taobao.org

//安装webpack
//npm install webpack -g

//安装vue-cli脚手架构建工具
//npm install vue-cli -g

//安装vue脚手架
//vue init webpack project-name

This will install Vue 2.x version of the template. ---------------------这里说明将要创建一个vue 2.x版本的项目
For Vue 1.x use: vue init webpack#1.0 exprice
? Project name (exprice) ---------------------项目名称
? Project name exprice
? Project description (A Vue.js project) ---------------------项目描述
? Project description A Vue.js project
? Author Datura --------------------- 项目创建者
? Author Datura
? Vue build (Use arrow keys)
? Vue build standalone
? Install vue-router? (Y/n) --------------------- 是否安装Vue路由，也就是以后是spa（但页面应用需要的模块）
? Install vue-router? Yes
? Use ESLint to lint your code? (Y/n) n ---------------------是否启用eslint检测规则，这里个人建议选no
? Use ESLint to lint your code? No
? Setup unit tests with Karma + Mocha? (Y/n)
? Setup unit tests with Karma + Mocha? Yes
? Setup e2e tests with Nightwatch? (Y/n)
? Setup e2e tests with Nightwatch? Yes
vue-cli · Generated "exprice".
To get started: --------------------- 这里说明如何启动这个服务
cd exprice
npm install
npm run dev

//使用yarn，cd到项目目录，执行yarn（yarn install的简写，功能与npm install）
//yarn run dev


//安装项目依赖
//npm install

//安装 vue 路由模块 vue-router 和网络请求模块 vue-resource
//cnpm install vue-router vue-resource --save。

export default {
  
}
</script>

<style scoped>

</style>


国内镜像整不动

npm config set -g registry https://registry.npm.taobao.org

npm i element-ui -S