<template>
    <user/>
  </template>
  
  <script lang="ts">
    import user from '../components/User.vue'
  
    export default {
      name:'App', //组件名
      components:{user} //注册组件
    }
    
  </script>