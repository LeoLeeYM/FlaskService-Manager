<template>
    <div style="display: flex; justify-content: center; padding: 100px; padding-top: 15vh;">
        <el-card style="width: 500px;">
            <div style="margin: 20px;">
                <h2>登录</h2>
                <el-form label-width="80px" :model="formLabelAlign" label-position="left" style="padding: 30px;"
                    :rules="rules">
                    <el-form-item label="用户名" prop="userId">
                        <el-input v-model="formLabelAlign.userId"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="pwd" >
                        <el-input v-model="formLabelAlign.pwd" show-password></el-input>
                    </el-form-item>
                </el-form>
                <el-button type="primary" style="width: 30%;" @click="login()">登录</el-button>
            </div>

        </el-card>
    </div>
</template>

<script>
import request from '../utils/request'
import Cookies from 'js-cookie'
import { Message } from 'element-ui'

function login(data) {
    return request({
        url: '/login',
        method: 'post',
        data: data,
    })
}

export default {
    data() {
        return {
            formLabelAlign: {
                userId: '',
                pwd: ''
            },
            rules: {
                userId: [
                    { required: true, message: '请输入用户名', trigger: 'blur' },
                ],
                pwd: [
                    { required: true, message: '请输入密码', trigger: 'blur' }
                ]
            }
        }

    },
    methods: {
        login() {
            if (this.formLabelAlign.userId == '' || this.formLabelAlign.pwd == '') {
                Message({ message: '请正确输入用户名和密码', type: 'error' })
                return
            }
            login(this.formLabelAlign).then(res => {
                if(res.status == 'success'){
                    Cookies.set('token', res.token);
                    this.$router.push('/')
                }else{
                    Message({ message: '登录失败', type: 'error' })
                }
            })
        }
    }
}
</script>

<style></style>