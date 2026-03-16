<template>
  <div class="app-container">
    <div class="header">
      <h1>云端文件检索</h1>
      <p class="subtitle">扁平化设计 · 支持无限层级</p>
      <p class="subtitle">by Gemini 3.1 Pro</p>
    </div>

    <div class="tree-wrapper">
      <div v-if="loading" class="loading">正在加载文件列表...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else class="tree-content">
        <!-- 遍历根节点的数组 -->
        <FileNode v-for="(item, index) in treeData" :key="index" :node="item" />
      </div>
    </div>
  </div>
</template>

<script setup>
"]";
import { ref, onMounted } from "vue";
import FileNode from "./FileNode.vue";

const treeData = ref([]);
const loading = ref(true);
const error = ref(null);

const fetchData = async () => {
  try {
    const response = await fetch("/api/getitems");
    if (!response.ok) throw new Error("网络请求失败");

    const restBean = await response.json();
    if (restBean.code == 200) {
      treeData.value = restBean.data;
    } else {
      error.value = restBean.message;
    }
  } catch (err) {
    error.value = "无法获取数据，请检查网络设置。";
    console.error(err);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  fetchData();
});
</script>

<style>
/* 全局样式重置 */
body {
  margin: 0;
  padding: 0;
  background-color: #fdfbf7; /* 纸张淡黄色 */
  font-family:
    -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue",
    Arial, sans-serif;
}

.app-container {
  width: 80%;
  margin: 0 auto;
  padding: 40px 20px;
  min-height: 100vh;
}

.header {
  margin-bottom: 30px;
  text-align: center;
}

.header h1 {
  color: #3e3a37;
  margin: 0 0 8px 0;
  font-size: 28px;
}

.subtitle {
  color: #a0968a;
  margin: 0;
  font-size: 14px;
}

.tree-wrapper {
  background-color: rgba(255, 255, 255, 0.4);
  border-radius: 16px;
  padding: 20px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.02);
  border: 1px solid #f0e8da;
}

.loading,
.error {
  text-align: center;
  padding: 40px;
  color: #a0968a;
  font-size: 16px;
}

.error {
  color: #d62828;
}
</style>
