<template>
  <v-app>
    <navbar></navbar>
    <router-view />
  </v-app>
</template>

<script>
import navbar from "../src/views/NavBar"
export default {
  name: 'App',

  components: {
    navbar
  },

  data: () => ({
    //
  }),
};
</script>
