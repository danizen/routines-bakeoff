<template>
  <div>
    <h2>{{ this.name }}</h2>
    <p>{{ this.description}}</p>
    <ul>
      <li v-for="(item, index) of items" :key="index">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
import routines from '../data';

export default {
  props: ['id'],
  computed: {
    name() {
      return routines[+this.id].name;
    },
    description() {
      return routines[+this.id].description;
    },
    items() {
      return routines[+this.id].items;
    },
  },
};
</script>
