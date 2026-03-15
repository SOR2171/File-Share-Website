<template>
  <div class="node-container">
    <!-- 当前节点 -->
    <div
      class="node-item"
      :class="{ 'is-file': isFile, 'is-folder': !isFile }"
      @click="toggle"
    >
      <!-- 图标 -->
      <div class="icon">
        <!-- 文件图标 (红色) -->
        <svg
          v-if="isFile"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"
          />
        </svg>
        <!-- 文件夹图标 (橘色) -->
        <svg
          v-else
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            v-if="isOpen"
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M5 19a2 2 0 01-2-2V7a2 2 0 012-2h4l2 2h4a2 2 0 012 2v1M5 19h14a2 2 0 002-2v-5a2 2 0 00-2-2H9a2 2 0 00-2 2v5a2 2 0 01-2 2z"
          />
          <path
            v-else
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"
          />
        </svg>
      </div>

      <!-- 文件名 -->
      <span class="node-name">{{ displayName }}</span>
    </div>

    <!-- 子节点递归 (如果是文件夹且已展开) -->
    <div class="node-children" v-if="!isFile && isOpen">
      <FileNode
        v-for="(child, index) in node.sub_list"
        :key="index"
        :node="child"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

// 为了在组件内部递归调用自身
defineOptions({ name: "FileNode" });

const props = defineProps({
  node: {
    type: Object,
    required: true,
  },
});

const isOpen = ref(false);

// 判断是否为文件 (sub_list为空)
const isFile = computed(() => {
  return !props.node.sub_list || props.node.sub_list.length === 0;
});

// 处理名称，去掉 "folder:" 或 "file:" 前缀
const displayName = computed(() => {
  return props.node.name.replace(/^(folder|file):/, "");
});

// 切换文件夹展开/收起状态
const toggle = () => {
  if (!isFile.value) {
    isOpen.value = !isOpen.value;
  }
};
</script>

<style scoped>
.node-container {
  margin: 4px 0;
}

.node-item {
  display: flex;
  align-items: center;
  padding: 10px 16px;
  background-color: #ffffff;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
  border-left: 4px solid transparent;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

/* 扁平化+悬浮强调动画 */
.node-item:hover {
  transform: translateX(6px) scale(1.01);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
}

.is-folder:hover {
  border-left-color: #f28c28; /* 橘色强调 */
  background-color: #fff9f2;
}

.is-file:hover {
  border-left-color: #d62828; /* 红色强调 */
  background-color: #fff5f5;
}

.icon {
  width: 24px;
  height: 24px;
  margin-right: 12px;
  flex-shrink: 0;
}

.is-folder .icon {
  color: #f28c28; /* 橘色 */
}

.is-file .icon {
  color: #d62828; /* 红色 */
}

.node-name {
  font-size: 15px;
  color: #3e3a37;
  font-weight: 500;
  user-select: none;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* 子节点层级缩进及左侧连接线 */
.node-children {
  margin-left: 22px;
  padding-left: 12px;
  border-left: 2px dashed #eaddcb; /* 淡淡的纸张折痕色 */
  margin-top: 4px;
}
</style>
