<template>
    <div class="top">
        <div class="main">
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-input
                            placeholder="请输入用户名"
                            prefix-icon="el-icon-service"
                            v-model="formData.username"
                            clearable></el-input>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-input
                            placeholder="请输入邮箱"
                            prefix-icon="el-icon-message"
                            type="email"
                            v-model="formData.email"
                            clearable></el-input>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-input
                            placeholder="请输入密码"
                            prefix-icon="el-icon-view"
                            v-model="formData.password1"
                            type="password"
                            clearable></el-input>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-input
                            placeholder="请再次输入密码"
                            prefix-icon="el-icon-view"
                            v-model="formData.password2"
                            type="password"
                            clearable></el-input>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <el-button
                            type="primary"
                            @click="register()"
                            :disabled="!formData.password1 || !formData.username || !formData.password2 || !formData.email">注册</el-button>
                </el-col>
            </el-row>
            <el-row type="flex" justify="center" class="tips">
                <el-col :xs="17" :sm="9" :md="7" :lg="5">
                    <router-link to="/" >
                        <span class="remind">已有账号，去登录</span>
                    </router-link>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    import {Register} from '../api/index'

    export default {
        name: "Register",
        data() {
            return {
                formData: {
                    username: '',
                    email:'',
                    password1:'',
                    password2:'',
                },
            };
        },
        methods: {
            checkMessage: function() {
                if(this.password1 !== this.password2) {
                    this.$message({
                        message: '两次密码不一致',
                        center: true,
                        type: 'warning'
                    });
                    return false
                }
                return true
            },
            //注册
            register: function() {
                if (!this.checkMessage()) {
                    this.$toast.fail('密码不一致')
                    return
                }
                console.log('密码一致')
                var param = new FormData()
                param.append('username', this.formData.username)
                param.append('email', this.formData.email)
                param.append('password', this.formData.password1)
                console.log(param)
                Register(param).then((response) => {
                    if (response.status === 200) {
                        console.log(response)
                        this.$toast.success('注册成功')
                        this.$router.push({
                            name: 'Login',
                        })
                    } else {
                        console.log(response)
                        // 提示信息
                        this.$toast.fail(response.data.msg)
                    }
                }).catch((error) => {
                    console.log(error)
                    // loading.close()
                    this.$toast.fail('注册失败')
                })
            },
        },
        components: {
        }
    }
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
