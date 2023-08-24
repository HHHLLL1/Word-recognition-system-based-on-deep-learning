<template>
    <div class="view">
<!--        <el-button @click="toMe" style="margin-top: 20px; margin-left: 10px">返回</el-button>-->
        <van-nav-bar title="修改密码" right-text="" left-arrow @click-left="toMe" style="margin-bottom: 10px; background: #409EFF"/>

        <div class="main">
            <el-form :model="userForm" status-icon :rules="rules" ref="userForm">
                <el-row type="flex" justify="center">
                    <el-col :xs="17" :sm="9" :md="7" :lg="5">
                        <el-input
                                placeholder="请输入旧密码"
                                prefix-icon="el-icon-service"
                                v-model="userForm.password"
                                clearable>
                        </el-input>
                    </el-col>
                </el-row>
                <el-row type="flex" justify="center">
                    <el-col :xs="17" :sm="9" :md="7" :lg="5">
                        <el-input
                                placeholder="请输入新密码"
                                prefix-icon="el-icon-view"
                                v-model="userForm.newpassword"
                                clearable
                                ></el-input>
                    </el-col>
                </el-row>
                <el-row type="flex" justify="center" style="margin-left: 50px; margin-right: 50px">
                    <el-col :xs="17" :sm="9" :md="7" :lg="5">
                        <el-button
                                style="width: 100%"
                                type="primary"
                                @click="changePWD"
                                :disabled="!userForm.password || !userForm.newpassword">修改密码</el-button>
                    </el-col>
                </el-row>
            </el-form>
        </div>
    </div>
</template>

<script>
    import { ChangePwd } from '../api/index'

    export default {
        name: "ChangePassword",
        data(){
            return {
                userForm: {
                    username: this.cookie.getCookie('username'),
                    password: '',
                    newpassword: '',
                },
                rules: {
                    password: [{ required: true, message: '旧密码不能为空', trigger: 'blur' }],
                    newpassword: [{ required: true, message: '新密码不能为空', trigger: 'blur' }]
                }
            };
        },
        methods: {
            changePWD() {
                ChangePwd(this.userForm).then((response) => {
                    if(response.status === 200){
                        console.log("success")
                        this.$toast.success('密码修改成功')
                    } else {
                        // console.log(response)
                        // 提示信息
                        this.$toast.fail(response.data.msg)
                        // this.$toast.fail(response.data.msg)
                    }
                }).catch((error) => {
                    console.log(error)
                    this.$toast.fail('密码修改失败')
                })
            },
            toMe() {
                this.$router.push('/me')
            }
        }
    }
</script>

<style scoped>
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


</style>
