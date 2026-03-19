<template>
  <div class="app-container">
    <div class="header">
      <h1>云端音乐检索</h1>
      <p class="subtitle">扁平化设计 · 支持无限层级</p>
      <p class="subtitle">by Gemini 3.1 Pro</p>
    </div>

    <div class="tree-wrapper">
      <div v-if="loading || loadingPlaylists" class="loading">
        正在加载数据...
      </div>
      <div v-else-if="error || errorPlaylists" class="error">
        {{ error || errorPlaylists }}
      </div>
      <div v-else>
        <h2 class="section-title">播放列表</h2>
        <div class="tree-content">
          <FileNode
            v-for="(item, index) in playlistsData"
            :key="'pl-' + index"
            :node="item"
          />
        </div>

        <hr class="section-divider" />

        <h2 class="section-title">文件列表</h2>
        <div class="tree-content">
          <!-- 遍历根节点的数组 -->
          <FileNode
            v-for="(item, index) in treeData"
            :key="'file-' + index"
            :node="item"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import FileNode from "./FileNode.vue";

const treeData = ref([]);
const playlistsData = ref([]);
const loading = ref(true);
const loadingPlaylists = ref(true);
const error = ref(null);
const errorPlaylists = ref(null);

const fetchData = async () => {
  try {
    const response = await fetch("/api/get-items");
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

const fetchPlaylistsData = async () => {
  try {
    const response = await fetch("/api/get-playlists");
    if (!response.ok) throw new Error("网络请求失败");

    const restBean = await response.json();
    if (restBean.code == 200) {
      playlistsData.value = restBean.data;
    } else {
      errorPlaylists.value = restBean.message;
    }
  } catch (err) {
    errorPlaylists.value = "无法获取播放列表，请检查网络设置。";
    console.error(err);
  } finally {
    loadingPlaylists.value = false;
  }
};

onMounted(() => {
  fetchData();
  fetchPlaylistsData();
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

.section-title {
  color: #3e3a37;
  font-size: 20px;
  margin: 10px 0 20px 0;
  padding-left: 10px;
  border-left: 4px solid #a0968a;
}

.section-divider {
  border: none;
  border-top: 1px dashed #dcd5cc;
  margin: 30px 0;
}
</style>
