<template>
 <el-steps  :active="step" simple>

<el-step title="查询" ></el-step>
<el-step title="解密" ></el-step>
</el-steps>
<div v-if="step == 0" class="form1">
<el-input
    v-model="inputValue"
    placeholder="请输入关键词，来得到对应的陷门"
    clearable
/>
<el-button type="primary" @click="handleCreate">生成陷门</el-button>
<el-card class="box-card">
    <div class="tag-container">
      <el-tag
        v-for="item in trapdoors"
        :key="item"
        type="success"
        size="large"
        effect="dark"
        style="margin: 5px;"
      >
        {{ item }}
      </el-tag>
    </div>
  </el-card>
  <el-button type="primary" @click="handleSearch">查询</el-button>
  <el-card>
    <template #header>
      <span>加密文件列表</span>
    </template>

    <el-table :data="fileList" style="width: 100%" border stripe>
      
      <el-table-column prop="uuid" label="文件uuid" />
      
      <el-table-column prop="ciphername" label="加密文件名" />

    </el-table>
  </el-card>
  <el-button type="primary" @click="decryptFile">解密</el-button>
</div>
<div v-if="step == 1">
    <el-table :data="fileList" style="width: 100%" border stripe>
      
      <el-table-column prop="uuid" label="文件uuid" />
      
      <el-table-column prop="plain_name" label="加密文件名" />

    </el-table>
</div>
</template>

<script lang="ts" setup name="App_search">
import axios from 'axios';
import { reactive, ref } from 'vue';
let step = ref(0)
let inputValue = ref('')
const trapdoors = ref([])
const fileList = ref([])
const handleCreate = () => {
    axios.post('/func/gentrapdoor', {
        "keyword": inputValue.value 
    }).then(res => {
        if (res.data.header.code == 200) {
            // console.log(res.data)
            trapdoors.value = res.data.trapdoor
            // console.log("trapdoors",trapdoors.value)  
        }
       else {
            alert("生成失败")
       }
    })
}
const handleSearch = () => {
    axios.post('/store/search', {
        "trapdoor": trapdoors.value,
        "user_id": sessionStorage.getItem('username'),
    }).then(res => {
        console.log(res.data)
        if (res.data.header.code == 200) {
            fileList.value= res.data.ciphername_list
        }
    })
}
const decryptFile = () => {
    step.value = 1
    console.log(fileList.value)
    axios.post('/func/getplainname', {
        "ciphername_list": fileList.value,
        "user_id": sessionStorage.getItem('username'),
    }).then(res => {
        console.log(res.data)
        if (res.data.header.code == 200) {
            fileList.value= res.data.plainname_list
        }
    })
}


</script>
