<template>
    <div class="app">
      <!-- 头部区 -->
      <div class="header">
        <h4>密文检索系统</h4>
      </div>
      <!-- 导航区 -->
      <div class="navigate">
        <RouterLink :to="{name:'upload_file'}" active-class="active" @click="user_test">文件上传</RouterLink>
        <RouterLink :to="{name:'search_file'}" active-class="active" @click="user_test">查询</RouterLink>
        <button class="logout-btn"@click="logout"> 退出登录 </button>
      </div>
      <!-- 展示区 -->
      <div class="main-content">
        <RouterView></RouterView>
      </div>
    </div>
  </template>
  
  <script lang="ts" setup name="App">
    import {RouterView,RouterLink} from 'vue-router'
    import axios from 'axios'
  
    const user_test = ()=>{
      let username = sessionStorage.getItem("username")
      if (username == null)
      {
        alert("您还没有登录，请先登录！")
        setTimeout(function() {
          window.location.replace("/login");
          }, 0)
      }
    }
  
    const logout = () =>{
      let username = sessionStorage.getItem("username")
      if (username == null)
      {
        alert("您还没有登录，请先登录！")
        setTimeout(function() {
          window.location.replace("/login");
          }, 0)
      }
      //http://127.0.0.1:5000/api/auth/logout
      axios.post('/func/logout', {
        "username": username
      },{ withCredentials: true }).then(response => {
        // 处理登出逻辑
        console.log(response.data);
        if (response.data.status == "success")
        {
          sessionStorage.clear()
          window.location.href = "/login"
        }
        else
        {
          window.location.href = '/login'
        }
      }).catch(error => {
        // 处理登出失败逻辑
        alert("出错了，请联系网站管理员修复。")
      })
  
    }
  
  </script>
  
  <style>
      /* App */
    .logout-btn {
      display: block;
      text-align: center;
      padding: 50px;
      width: 200px;
      height: 120px;
      line-height: 30px;
      border-radius: 10px;
      background-color: gray;
      text-decoration: none;
      color: white;
      font-size: 18px;
      letter-spacing: 5px;
    }
    .logout-btn:hover {
      background-color: #64967E;
      color: #ffc268;
      font-weight: 900;
      text-shadow: 0 0 1px black;
    }
    .header{
      text-align: center;
      margin: 0 auto;
      margin-top: 20px;
      font-size: 40px;
      font-weight: 900;
      color: #ffc268;
      text-shadow: 0 0 1px black;
      font-family: 微软雅黑;
    }
    .navigate {
      display: flex;
      justify-content: space-around;
      margin: 0 100px;
    }
    .navigate a {
      display: block;
      text-align: center;
      padding: 40px;
      width: 130px;
      height: 40px;
      line-height: 40px;
      border-radius: 10px;
      background-color: gray;
      text-decoration: none;
      color: white;
      font-size: 18px;
      letter-spacing: 5px;
    }
    .navigate a.active {
      background-color: #64967E;
      color: #ffc268;
      font-weight: 900;
      text-shadow: 0 0 1px black;
      font-family: 微软雅黑;
    }
    .navigate a:hover {
      background-color: #64967E;
      color: #ffc268;
      font-weight: 900;
      text-shadow: 0 0 1px black;
      font-family: 微软雅黑;
    }
    .main-content {
      margin: 0 auto;
      margin-top: 30px;
      border-radius: 10px;
      width: 90%;
      border: 1px solid;
      display: flex;
      flex-direction: column;
      min-height: 100vh
    }
  </style>
  