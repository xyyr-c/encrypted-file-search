import {createRouter,createWebHashHistory} from 'vue-router';

import upload from '@/components/pages/upload.vue';
import search_file from '@/components/pages/search_file.vue';

const router = createRouter({
  history: createWebHashHistory(),
  routes:[
    {
      name:'upload_file', //路由名称
      path: '/upload_file',
      component: upload
    },
    {
      name:'search_file',
      path: '/search_file',
      component: search_file
    }
    ]
})

export default router;
