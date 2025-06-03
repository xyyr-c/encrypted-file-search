<template>
  <div class="upload">
    <input type="file" @change="onFileChange" />
    <button @click="uploadFile">Upload</button>
  </div>
</template>

<script lang="ts" setup name="App_upload">
import axios from 'axios';
import { ref } from 'vue';

const file = ref<File | null>(null);

const onFileChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  file.value = input.files?.[0] || null;
};

const uploadFile = async () => {
  if (!file.value) return;

  try {
    const formData = new FormData();
    formData.append('file', file.value);
  }   catch (error) {
    console.error(error);
  }
  }
</script>