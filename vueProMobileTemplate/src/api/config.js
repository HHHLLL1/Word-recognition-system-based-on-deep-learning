/**
 * 请求数据配置
 * 配置编译环境和线上环境之间的IP切换
 *
 * baseURL: 域名地址
 * fileUpBaseUrl:上传文件
 **/
// var baseURL = ''
// var fileUpBaseUrl = ''
//
// if (process.env.NODE_ENV === 'development') {
//   baseURL = '/apiPath'
//   fileUpBaseUrl = ''
// } else {
//   baseURL = ''
//   fileUpBaseUrl = ''
// }
// export {
//   baseURL,
//   fileUpBaseUrl
// }

const serverRoot = 'http://127.0.0.1:8001/api';

//登录
export const login = `${serverRoot}/user/login/`;

//注册
export const register = `${serverRoot}/user/register/`;

//修改密码
export const changePWD = `${serverRoot}/user/changePWD/`;

//个人信息
export const info = `${serverRoot}/user/info/`;

//图片上传
export const upload = `${serverRoot}/upload/`;
export const upload_lan = `${serverRoot}/uploadlan/`;
export const upload_idcard = `${serverRoot}/uploadidcard/`;
export const upload_carcard = `${serverRoot}/uploadcarcard/`;


//历史记录
export const history = `${serverRoot}/history/`;



//上传文件的路径
export const uploadRoot = 'http://127.0.0.1:8001/upload/';


