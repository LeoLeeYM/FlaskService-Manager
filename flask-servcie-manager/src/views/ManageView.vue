<template>
    <div style="padding: 30px;">
        <div style="text-align: left;">
            <el-button type="primary" @click="$refs.addSerivce.show()">添加服务器</el-button>
        </div>

        <el-row :gutter="20" style="margin-top: 30px;">
            <el-col :span="6" v-for="(item, index) in takeList" :key="index">
                <el-card style="text-align: left; height: 230px;" shadow="hover" :class="item.isRun ? 'card-Run' : ''">
                    <div slot="header" class="clearfix">
                        <span style="font-weight: bold;">{{ item.title }}</span>
                        <el-button style="float: right; padding: 3px 0" type="text"
                            @click="changeService(item.isRun, item.id)">{{ item.isRun ? '关闭' : '启动' }}</el-button>
                        <el-button style="float: right; padding: 3px 0; margin-right: 10px; color: #ff9d00" type="text"
                            @click="$refs.infoService.show(item.id)">详情</el-button>
                        <el-button style="float: right; padding: 3px 0; color: #ff6161" type="text"
                            @click="delService(item.id)">删除</el-button>
                    </div>
                    <p v-if="item.isRun">状态：<strong style="color: #0ed28a;">已启动</strong></p>
                    <p v-if="!item.isRun">状态：<strong style="color: #ff6161;">未启动</strong></p>
                    <p>路径：{{ item.path }}</p>
                    <p>备注：{{ item.remark }}</p>
                </el-card>
            </el-col>
        </el-row>

        <AddService_DialogVue ref="addSerivce"></AddService_DialogVue>
        <InfoService_DialogVue ref="infoService"></InfoService_DialogVue>
    </div>
</template>

<script>
import request from '../utils/request'
import { Message } from 'element-ui'

import AddService_DialogVue from '@/components/Dialogs/AddService_Dialog.vue'
import InfoService_DialogVue from '@/components/Dialogs/InfoService_Dialog.vue'

function listTask() {
    return request({
        url: '/listTask',
        method: 'get'
    })
}

function runTask(id) {
    return request({
        url: `/runTask?taskId=${id}`,
        method: 'get'
    })
}

function closeTask(id) {
    return request({
        url: `/closeTask?taskId=${id}`,
        method: 'get'
    })
}

function delTask(id) {
    return request({
        url: `/delTask?taskId=${id}`,
        method: 'get'
    })
}

function getTask(id) {
    return request({
        url: `/getTask?taskId=${id}`,
        method: 'get'
    })
}

export default {
    components: {
        AddService_DialogVue,
        InfoService_DialogVue
    },
    data() {
        return {
            takeList: null
        }
    },
    mounted() {
        this.getlist()
    },

    methods: {
        getlist() {
            listTask().then(res => {
                if (res.error != 'Invalid token') {
                    this.takeList = res
                } else {
                    Message({ message: '获取数据失败，请重新登录', type: 'error' })
                }
            })
        },
        changeService(isRun, id) {
            if (!isRun) {
                runTask(id).then(res => {
                    if (res.status == 'success') {
                        Message({ message: '启动成功', type: 'success' })
                    } else {
                        Message({ message: '启动失败', type: 'error' })
                    }
                    this.getlist()
                })
            } else {
                closeTask(id).then(res => {
                    if (res.status == 'success') {
                        Message({ message: '关闭成功', type: 'success' })
                    } else {
                        Message({ message: '关闭失败', type: 'error' })
                    }
                    this.getlist()
                })
            }
        },
        delService(id) {
            delTask(id).then(res => {
                if (res.status == 'success') {
                    Message({ message: '删除成功', type: 'success' })
                } else {
                    Message({ message: '删除失败', type: 'error' })
                }
                this.getlist()
            })
        }
    }
}
</script>

<style>
.card-Run {
    background-color: #f8fcf6;
}
</style>