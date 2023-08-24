<template>
    <div class="top">
        <div class="main">
<!--            <span class="title">华农一屋</span>-->
            <el-form :model="userForm" status-icon :rules="rules" ref="userForm">
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-input
                            placeholder="请输入用户名"
                            prefix-icon="el-icon-service"
                            v-model="userForm.username"
                            clearable>
                    </el-input>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-input
                            placeholder="请输入密码"
                            prefix-icon="el-icon-view"
                            v-model="userForm.password"
                            clearable
                            type="password"></el-input>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-button
                            type="primary"
                            @click="login('userForm')"
                            :disabled="!userForm.password || !userForm.username">登录</el-button>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center" class="tips">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <router-link to="/register" >
                        <span class="remind">还没有账号？去注册</span>
                    </router-link>
                </el-col>
            </el-row>
            </el-form>
        </div>
    </div>
</template>

<script>
    import {Login} from '../api/index'

    export default {
        name: "login",
        data() {
            return {
                userForm: {
                    username: '',
                    password: '',
                },
                rules: {
                    username: [{ required: true, message: '用户名不能为空', trigger: 'blur' }],
                    password: [{ required: true, message: '密码不能为空', trigger: 'blur' }]
                }
            };
        },
        mounted() {
            // this.autoLogin();
        },
        methods: {
            login: function(formName) {
                this.$refs[formName].validate().then((result) => {
                    if (result) {
                        // const loading = this.$loading({})
                        Login(this.userForm.username, this.userForm.password)
                            .then((response) => {
                                if (response.status === 200) {
                                    console.log(response)
                                    // this.$store.commit('GET_USER', response.data)
                                    // loading.close()
                                    //记录COOKIE
                                    var param = {'username': this.userForm.username}
                                    this.cookie.setCookie(param, 3)
                                    // 提示信息
                                    this.$toast.success('登录成功')
                                    // 路由跳转
                                    // this.$router.push(this.$route.query.redirect || {name: 'Home'})
                                    this.$router.push({
                                        name: 'Home',
                                    })
                                } else {
                                    console.log(response)
                                    // loading.close()
                                    // 提示信息
                                    this.$toast.fail(response.data.msg)
                                }
                            })
                            .catch((error) => {
                                console.log(error)
                                // loading.close()
                                this.$toast.fail('登录失败')
                            })
                    }
                })
            },
            // //读取cookie
            // autoLogin:function () {
            // if (document.cookie.length>0) {
            //         this.userForm.username = this.cookie.getCookie('username');//保存到保存数据的地方
            //         this.userForm.password = this.cookie.getCookie('password');
            //     }
            // },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        },
        components: {
        }
    };
</script>

<style scoped>
    .top {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0px;
        background-size: cover;
        background-image: url('../assets/images/background5.jpg');
    }
    .main {
        /*position: absolute;
        top: 50%;
        transform: translate(0, -50%);*/
        margin-top: 70px;
        width: 100%;
    }
    .el-row {
        margin-top: 30px;
    }
    .title {
        color: #409EFF;
        font-size: 40px;
    }
    .el-button {
        width: 100%;
    }
    .remind {
        font-size: 15px;
        float: left;
        /* margin-top: 20px;*/
        color:#b22222;
    }
    .tips {
        margin-top: 20px
    }
</style>
