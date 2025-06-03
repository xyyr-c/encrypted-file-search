import { createApp } from 'vue'
import App from './views/App_user.vue'
import router from './router/router.ts'
import ElementPlus from 'element-plus'
import "element-plus/dist/index.css"

const app =createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
