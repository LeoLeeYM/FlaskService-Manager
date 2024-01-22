<template>
  <div id="app">
    <el-container>
      <el-aside width="200px" class="left_nav">
        <div style="padding-top: 20px;">
          <img src="@/assets/logo.png" style="max-width: 100px; text-align: center;"/>
        <h2>FlaskService<p>Manager</p></h2>
        </div>
        
        <el-menu default-active="1-4-1" class="el-menu-vertical-demo" :router="true" style="text-align: left;">
          <el-menu-item index="/">
            <i class="el-icon-menu"></i>
            <span slot="title">首页</span>
          </el-menu-item>
          <el-menu-item index="/manage">
            <i class="el-icon-document"></i>
            <span slot="title">服务器管理</span>
          </el-menu-item>
          <el-menu-item>
            <el-button @click="exitLogin">退出登录</el-button>
          </el-menu-item>
        </el-menu>

      </el-aside>
      <el-container>
        <el-main class="main_box">
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Cookies from 'js-cookie'

export default {
  name: 'app',
  components: {
    HelloWorld
  },
  mounted(){
    if(Cookies.get('token') == undefined || Cookies.get('token') == ''){
      this.$router.push('/login')
    }
  },
  methods:{
    exitLogin(){
      Cookies.set('token', ''); 
      this.$router.push('/login')
    }
  }
}
</script>

<style>
.main_box {
  position: absolute;
  left: 200px;
  right: 0;
  top: 0;
  bottom: 0;
  overflow-y: scroll;
}
.left_nav {
  display: block;
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  z-index: 1000;
}
.el-menu {
  border: 0 !important;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
