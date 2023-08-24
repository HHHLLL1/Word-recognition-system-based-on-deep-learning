import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/home.vue'
import Login from '../views/login.vue'
import Register from "../views/register";
import Upload from "../views/upload"
import Upload_lan from "../views/upload_lan"
import Detail from "../views/detail";
import Me from "../views/me"
import History from "../views/history"
import MyInfo from "../views/myInfo"
import ChangePWD from "../views/changePassword"
import Upload_idcard from "../views/upload_idcard";
import Upload_carcard from "../views/upload_carcard"

import cookie from "../utils/cookie";

Vue.use(VueRouter)

  const routes = [
    {
      path: '/',
      name: 'Login',
      component: Login,
      meta: {
        title: '登录',
        isMenu: false
      }
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
      meta: {
        title: '注册',
        isMenu: false
      }
    },
    {
      path: '/info',
      name: 'MyInfo',
      component: MyInfo,
      meta: {
        title: '个人信息',
        isMenu: false
      }
    },
    {
      path: '/changePWD',
      name: 'ChangePWD',
      component: ChangePWD,
      meta: {
        title: '修改密码',
        isMenu: false
      }
    },
    {
      path: '/upload',
      name: 'Upload',
      component: Upload,
      meta: {
        title: '上传',
        isMenu: false
      }
    },
    {
      path: '/upload_lan',
      name: 'Upload_lan',
      component: Upload_lan,
      meta: {
        title: 'lan上传',
        isMenu: false
      }
    },
    {
      path: '/upload_idcard',
      name: 'Upload_idcard',
      component: Upload_idcard,
      meta: {
        title: 'idcard上传',
        isMenu: false
      }
    },
    {
      path: '/upload_carcard',
      name: 'Upload_carcard',
      component: Upload_carcard,
      meta: {
        title: 'carcard上传',
        isMenu: false
      }
    },
    {
      path: '/detail',
      name: 'Detail',
      component: Detail,
      meta: {
        title: '识别结果',
        isMenu: false
      }
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      meta: {
        title: '首页',
        isMenu: true,
        isHead: true
      }
    },
    {
      path: '/me',
      name: 'Me',
      component: Me,
      meta: {
        title: '我的',
        isMenu: true,
        isHead: true
      }
    },
    {
      path: '/history',
      name: 'History',
      component: History,
      meta: {
        title: '识别历史',
        isMenu: false
      }
    }
  ]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location, onResolve, onReject) {
  if (onResolve || onReject) return originalPush.call(this, location, onResolve, onReject)
  return originalPush.call(this, location).catch(err => err)
}

/*
* beforeEach:从一个页面跳转到另外一个页面时触发
* to:要跳转的页面
* from:从哪个页面出来
* next:决定是否通过
*/
router.beforeEach((to, from, next) => {
  // 如果跳转的页面不存在，跳转到404页面
  if(to.matched.length===0){
    next('/404')
  }
  if (cookie.getCookie("username")) {
    next()
  } else {
    if (to.path === "/" || to.path === '/register') {
      next()
    } else {
      next('/')
    }
  }
})




export default router
