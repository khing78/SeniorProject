<template>
  <div class="nav-bar">
    <v-app-bar color="white" dense dark>
      <v-toolbar-title style="margin-top: 0px; color: #1ce227" class="navbar"
        >ระบบแสดงคุณภาพมันสำปะหลัง</v-toolbar-title
      >
      <v-spacer />
      <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn
        color="white"
          v-bind="attrs"
          v-on="on"
          text
          :disabled="!name"
        >
          <div id="username" style="color: #1ce227; padding-right: 5px">{{ name }}</div>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
        >
          <v-list-item-content @click="logoutbutton()">Logout</v-list-item-content>
        </v-list-item>
      </v-list>
    </v-menu>
      <v-avatar><v-img id="imagecharacter" :src="imagesrc"></v-img></v-avatar>
    </v-app-bar>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  data: () => ({
    usernameA: "",
    imagesrc: "../assets/iconusercc.png",
  }),
  methods: {
    logoutbutton(){

    }
  },
  computed: {
    ...mapGetters({
      name: "getName",
    }),
  },
};
</script>
<style>
.navbar {
  font-family: "Prompt", sans-serif;
}
</style>