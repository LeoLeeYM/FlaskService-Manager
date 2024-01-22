<template>
    <el-dialog title="服务器详情" :visible.sync="dialogVisible" width="50%" style="text-align: left;">
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

        <el-input id="logText_id" type="textarea" :rows="20" placeholder="服务器Log" v-model="service_log"
            resize="none"></el-input>

        <!-- <el-table ref="logTable" id="logTable_id" :data="logs" style="width: 100%" :row-class-name="tableRowClassName"
            max-height="500">
            <el-table-column prop="type" label="类型" width="100">
            </el-table-column>
            <el-table-column prop="info" label="信息">
            </el-table-column>
        </el-table> -->

        <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="editTask">更 新</el-button>
        </span>
    </el-dialog>
</template>

<script>
import request from '../../utils/request'
import { Message } from 'element-ui'

function editTask(data) {
    return request({
        url: '/editTask',
        method: 'post',
        data: data,
    })
}

function getTask(id) {
    return request({
        url: `/getTask?taskId=${id}`,
        method: 'get'
    })
}

export default {
    data() {
        return {
            logs: null,
            regetTask: null,
            dialogVisible: false,
            formLabelAlign: {
                taskId: '',
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
            },
            service_log: ''
        };
    },
    methods: {
        tableRowClassName() {

        },
        show(id) {
            clearInterval(this.regetTask);

            this.dialogVisible = true;
            getTask(id).then(res => {
                this.formLabelAlign = res.task;
                this.service_log = res.logData;
                this.formLabelAlign.taskId = res.task.id
                this.$nextTick(() => {
                    const textarea = document.getElementById('logText_id');
                    textarea.scrollTop = textarea.scrollHeight;
                });
            });

            this.regetTask = setInterval(() => {
                this.getLog(id);
                if (!this.dialogVisible) {
                    clearInterval(this.regetTask);
                }
            }, 500);
        },

        getLog(id) {
            getTask(id).then(res => {
                this.service_log = res.logData
            })
        },
        editTask() {
            editTask(this.formLabelAlign).then(res => {
                if (res.status == 'success') {
                    Message({ message: '修改成功', type: 'success' })
                    this.dialogVisible = false

                } else {
                    Message({ message: '修改失败', type: 'error' })
                }
                this.$parent.getlist()
            })
        }
    }
}
</script>

<style></style>