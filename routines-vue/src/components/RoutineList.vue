<template>
  <div>
    <h1>Routines</h1>
    <ul>
      <li v-for="routine of routines" :key="routine.name">
        {{routine.name}}
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
