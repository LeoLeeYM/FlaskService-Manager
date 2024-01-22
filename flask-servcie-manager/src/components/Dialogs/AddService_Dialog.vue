<template>
    <el-dialog title="添加服务器" :visible.sync="dialogVisible" width="30%" style="text-align: left;">
        <el-form label-position="left" label-width="80px" :model="formLabelAlign" style="padding: 20px" :rules="rules">
            <el-form-item label="名称" prop="title">
                <el-input v-model="formLabelAlign.title"></el-input>
            </el-form-item>
            <el-form-item label="路径" prop="path">
                <el-input v-model="formLabelAlign.path" placeholder="服务器入口文件的绝对路径">
                    <!-- <el-button slot="append">选择</el-button> -->
                </el-input>
            </el-form-item>
            <el-form-item label="备注">
                <el-input v-model="formLabelAlign.remark"></el-input>
            </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="createTask">确 定</el-button>
        </span>
    </el-dialog>
</template>

<script>
import request from '../../utils/request'
import { Message } from 'element-ui'

function createTask(data) {
    return request({
        url: '/createTask',
        method: 'post',
        data: data,
    })
}


export default {
    data() {
        return {
            dialogVisible: false,
            formLabelAlign: {
                title: '',
                remark: '',
                path: ''
            },
            rules: {
                title: [
                    { required: true, message: '请输入服务器名称', trigger: 'blur' },
                ],
                path: [
                    { required: true, message: '请输入入口文件的绝对路径', trigger: 'blur' }
                ]
            }
        };
    },
    methods: {
        show() {
            this.dialogVisible = true
        },
        createTask() {
            createTask(this.formLabelAlign).then(res => {
                if (res.status == 'success') {
                    Message({ message: '添加成功', type: 'success' })
                    this.dialogVisible = false
                } else {
                    Message({ message: '添加失败', type: 'error' })
                }
                this.$parent.getlist()
            })
        }
    }
}
</script>

<style></style>