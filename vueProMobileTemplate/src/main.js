import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import utils from './utils'
import 'amfe-flexible'
import ElementUI from 'element-ui'
import Vuex from 'vuex'
import 'element-ui/lib/theme-chalk/index.css'
// import Mint from 'mint-ui';
import { Toast } from 'vant'
import VuePreview from 'vue-preview'
import { NavBar } from 'vant';



Vue.use(Toast);
Vue.use(ElementUI)
Vue.use(Vuex)
// Vue.use(Mint)
Vue.use(VuePreview);
Vue.use(NavBar);


//初始化样式
import './common/stylus/index.styl'
Vue.config.productionTip = false
Vue.prototype.bus = new Vue;

import cookie from "./utils/cookie";
Vue.prototype.cookie = cookie;

Vue.use(utils)
import { Button } from 'vant';
Vue.use(Button)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
