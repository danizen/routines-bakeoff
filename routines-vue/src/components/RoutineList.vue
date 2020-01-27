<template>
  <div>
    <h1>Routines</h1>
    <ul>
      <li v-for="(routine, index) of routines" :key="index">
        <router-link :to="{name: 'routine-detail', params: {id: index}}">
          {{routine.name}}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import routines from '../data';

export default {
  computed: {
    routines() {
      return routines;
    },
  },
};
</script>
