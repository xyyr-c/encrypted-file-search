import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import VueSetupExtend from 'vite-plugin-vue-setup-extend'
import fs from 'fs'
//每次替换从代理替换即可。
// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    VueSetupExtend(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    port: 443,
    host: "0.0.0.0",
    https:
    {
      key: fs.readFileSync("./https/web.pkey"),
      cert: fs.readFileSync("./https/web.crt"),
    },
    proxy: {
        '/func':
        {
          target: 'https://10.33.36.243:8080',
          changeOrigin: true,
          secure:false,
        },
        '/store':
        {
          target: 'https://10.33.36.243:8081',
          changeOrigin: true,
          secure:false,
        }
     },
  },}

)
