import axios from "axios";
import * as url from './config'
/**
 * 获取类目
 */

let Login = (username, password) => axios({
    url: url.login,
    method: 'post',
    data: {
        username,
        password
    }
})

let Register = (param) => axios({
    url: url.register,
    method: 'post',
    data: param
})

let Info = (param) => axios({
    url: url.info,
    method: 'post',
    data: param
})

let ChangePwd = (param) => axios({
    /*开启withCredentials后，服务器才能拿到cookie 跨域请求时是否需要使用凭证*/
    // withCredentials: true,
    // headers: {'Content-Type': 'multipart/form-data'},
    url: url.changePWD,
    method: 'post',
    data: param
})

let Upload = (param) => axios({
    /*开启withCredentials后，服务器才能拿到cookie 跨域请求时是否需要使用凭证*/
    withCredentials: true,
    headers: {'Content-Type': 'multipart/form-data'},
    url: url.upload,
    method: 'post',
    data: param
})

let Upload_lan = (param) => axios({
    /*开启withCredentials后，服务器才能拿到cookie 跨域请求时是否需要使用凭证*/
    withCredentials: true,
    headers: {'Content-Type': 'multipart/form-data'},
    url: url.upload_lan,
    method: 'post',
    data: param
})

let Upload_idcard = (param) => axios({
    /*开启withCredentials后，服务器才能拿到cookie 跨域请求时是否需要使用凭证*/
    withCredentials: true,
    headers: {'Content-Type': 'multipart/form-data'},
    url: url.upload_idcard,
    method: 'post',
    data: param
})

let Upload_carcard = (param) => axios({
    /*开启withCredentials后，服务器才能拿到cookie 跨域请求时是否需要使用凭证*/
    withCredentials: true,
    headers: {'Content-Type': 'multipart/form-data'},
    url: url.upload_carcard,
    method: 'post',
    data: param
})


let History_info = (param) => axios({
    /*开启withCredentials后，服务器才能拿到cookie 跨域请求时是否需要使用凭证*/
    withCredentials: true,
    headers: {'Content-Type': 'multipart/form-data'},
    url: url.history,
    method: 'post',
    data: param
})

// export const getCategoryList = () => request.post('/category/list')
export {
    Login,
    Register,
    Info,
    ChangePwd,
    Upload,
    Upload_lan,
    Upload_idcard,
    Upload_carcard,
    History_info
}

// export const usersApi = {
//     login(param) {
//         return axios.post(url.login, param).then((response) => {
//             return response.data
//         })
//     },
//     register(param) {
//         return axios.post(url.register, param).then((response) => {
//             return response.data
//         })
//     },
// }
