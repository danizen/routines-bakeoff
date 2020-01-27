import Vue from 'vue';
// import 'ant-design-vue';
// import 'ant-design-vue/dist/antd.css';

import Router from 'vue-router';

import App from './App.vue';
import HomePage from './components/HomePage.vue';
import AboutPage from './components/AboutPage.vue';
import RoutineList from './components/RoutineList.vue';
import RoutineDetail from './components/RoutineDetail.vue';

Vue.config.productionTip = false;
Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      name: 'about',
      path: '/about',
      component: AboutPage,
    },
    {
      name: 'routine-list',
      path: '/routines',
      component: RoutineList,
    },
    {
      name: 'routine-detail',
      path: '/routine/:id',
      component: RoutineDetail,
      props: true,
    },
    {
      name: 'home',
      path: '/',
      component: HomePage,
    },
  ],
});

new Vue({
  render: h => h(App),
  router,
}).$mount('#app');
