<template>
  <div class="nav-bar">
    <v-app-bar color="white" dense dark>
      <v-toolbar-title style="margin-top: 0px; color: #1ce227" class="navbar"
        >ระบบแสดงคุณภาพมันสำปะหลัง</v-toolbar-title
      >
      <v-spacer />
      <a id="username" style="color: #1ce227; padding-right: 5px">{{
        name
      }}</a>
      <v-avatar><v-img id="imagecharacter" :src="imagesrc"></v-img></v-avatar>
    </v-app-bar>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  data: () => ({
    usernameA: "",
    imagesrc: "../assets/iconusercc.png",
  }),
  methods: {
  },
  computed: {
    ...mapGetters({
      name: "getName"
    })
  },
};
</script>
<style>
.navbar {
  font-family: "Prompt", sans-serif;
}
</style>