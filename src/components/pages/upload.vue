<template>
<div class="form">
        <el-row :gutter="10">
          <el-col :span="40">
            <el-card class="box-card tag" shadow="hover">
              <el-upload
                class="upload-demo"
                drag
                action=""
                :http-request="upload_file"
                accept=".txt"
                name="file"
                :auto-upload="true"
                :limit="1"
              >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">
                  将文件拖到此处，或<em>点击上传</em>
                </div>
                <div class="el-upload__tip" slot="tip">
                  请上传文件，大小不要超过 100 KB
                </div>
              </el-upload>
            </el-card>
          </el-col>
        </el-row>
      </div>

</template>

<script lang="ts" setup name="App_upload">
import axios from 'axios';
import { ref } from 'vue';

interface UploadFileParam {
      file: File;  // 上传的文件对象
      onSuccess: (response: any) => void;  // 上传成功的回调
      onError: (error: any) => void;  // 上传失败的回调
      [key: string]: any;  // 可以有其他可选属性
    }

function upload_file (param: UploadFileParam) {
      const formData = new FormData();
      formData.append('file', param.file);  // 上传文件字段名为 'file'
      console.log(formData)
      for (const [key, value] of formData) {
      console.log(key, value);
}
      axios.post('/func/upload', formData,{ withCredentials: true })
   .then((response) => {
    console.log(response.data);
    if (response.data.header.code == 200)
      {
        alert("上传成功")
      }
      else
      {
        alert("上传失败，请检查文件类型重新上传")
      }
  })
}
</script>

<style scoped>
::v-deep .upload-demo  .el-upload-dragger {
    height: 475px; /* 调整高度 */
    width: 100%; /* 调整宽度 */
}
.el-upload__text {
  height: auto; /* 调整文本区域的高度 */
  line-height: 1.5; /* 调整文本区域的行高 */
  margin-top: 40px; /* 调整文本区域的上边距 */
}
</style>