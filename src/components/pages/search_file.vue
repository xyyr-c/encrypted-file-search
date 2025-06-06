<template>
 <el-steps  :active="step" simple>

<el-step title="查询" ></el-step>
<el-step title="解密" ></el-step>
</el-steps>
<!-- 查询步骤 -->
<div v-if="step == 0" class="form-section">
  <div class="form-header">
      <el-input
          v-model="inputValue"
          placeholder="请输入关键词，来得到对应的陷门"
          clearable
          />
      </div>
<div class="btn-container">
<el-button type="primary" @click="handleCreate">生成陷门</el-button>
</div>
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
  <div class="btn-container">
    <el-button type="primary" @click="handleSearch">查询</el-button>
  </div>
  <el-card>
    <template #header>
      <span>加密文件列表</span>
    </template>

    <el-table :data="fileList" style="width: 100%" border stripe>
      
      <el-table-column prop="uuid" label="文件uuid" />
      
      <el-table-column prop="ciphername" label="加密文件名" />

    </el-table>
  </el-card>
  <div class="btn-container">
  <el-button type="primary" @click="decryptFile">解密</el-button>
</div>
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

<style scoped>
.el-button {
transition: all 0.3s ease;
border-radius: 8px;
padding: 12px 24px;
font-weight: 500;
}
        
.el-button:hover {
transform: translateY(-2px);
box-shadow: 0 4px 10px rgba(64, 158, 255, 0.3);
display: flex;
}
.el-card {
            border-radius: 12px;
            border: none;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            margin: 25px 0;
            transition: all 0.3s ease;
        }
        
        .el-card:hover {
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
        }
        
        .el-card__header {
            background: #f8fafc;
            border-bottom: 1px solid #eef2f6;
            padding: 18px 20px;
            font-weight: 600;
            font-size: 18px;
            color: #3c4b64;
            border-radius: 12px 12px 0 0 !important;
        }
.btn-container {
display: flex;
justify-content: center;
margin-top: 25px;
}
        /* 表单区域 */
.form-section {
            background: white;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }
        
        .form-section:hover {
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.06);
        }
</style>