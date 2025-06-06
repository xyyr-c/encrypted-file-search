<template>
<div class="form">
          <el-col :span="24">
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
                <div class="el-upload__text" style="font-size: 40px">
                  将文件拖到此处，或<em>点击上传</em>
                </div>
                <div class="el-upload__tip" slot="tip">
                  请上传文件，大小不要超过 100 KB
                </div>
              </el-upload>
            </el-card>
          </el-col>
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
::v-deep .upload-demo   {
    height: 475px; /* 调整高度 */
    width: 100%; /* 调整宽度 */
}
::v-deep .el-upload__text {
  height: auto; /* 调整文本区域的高度 */
  line-height: 1.5; /* 调整文本区域的行高 */
  font-size: x-large; /* 调整文本区域的字体大小 */
  color: #c74b0d; /* 调整文本区域的字体颜色 */
  text-align: center; /* 调整文本区域的文本对齐方式 */
  margin-bottom: 10px; /* 调整文本区域下边距 */
}
.el-upload__tip {
  font-size: 14px; /* 调整提示文本的字体大小 */
  color: #909399; /* 调整提示文本的字体颜色 */
}
:deep(.el-upload-dragger) {
  flex: 1; /* 拖拽区域填充空间 */
  display: flex;
  flex-direction: column;
  justify-content: center; /* 内容垂直居中 */
  align-items: center;
  height: 475px; /* 调整高度 */
  width: 100%; /* 调整宽度 */
}
</style>