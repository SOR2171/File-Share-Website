import { createRouter, createWebHistory } from "vue-router";
import MainPage from "../components/MainPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: MainPage,
    meta: { title: "SOR Music Share" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
