<template>
  <div class="nav-bar">
    <v-app-bar color="white" dense dark>
      <v-toolbar-title
        style="margin-top: 0px; color: #1ce227"
        class="navbar"
        ><v-btn @click="moveto('backtonormal')">ระบบแสดงคุณภาพมันสำปะหลัง</v-btn></v-toolbar-title
      >
      <v-spacer />
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="white" v-bind="attrs" v-on="on" text :disabled="!name">
            <div id="username" style="color: #1ce227; padding-right: 5px">
              {{ name }}
            </div>
          </v-btn>
        </template>
        <v-list>
          <v-list-item>
            <v-list-item-content @click="logoutbutton()"
              >Logout</v-list-item-content
            >
          </v-list-item>
        </v-list>
      </v-menu>
      <v-avatar><v-img id="imagecharacter" :src="imagesrc"></v-img></v-avatar>
    </v-app-bar>
  </div>
</template>
<script>
import firebase from "firebase/app";
import { mapGetters } from "vuex";
export default {
  data: () => ({
    imagesrc: "../assets/iconusercc.png",
  }),
  methods: {
    moveto() {
      const vm = this
      firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
          console.log(user)
          vm.$router.push("/show-all-area");
        } else {
          vm.$router.push("/");
        }
      });
    },
    logoutbutton() {
      const vm = this;
      firebase
        .auth()
        .signOut()
        .then(() => {
          this.$store.commit({
            type: "setUserName",
            name: "",
          });
          // Sign-out successful.
          vm.$router.push("/");
        })
        .catch((error) => {
          // An error happened.
          console.log(error);
        });
    },
  },
  computed: {
    ...mapGetters({
      name: "getUserName",
    }),
  },
};
</script>
<style>
.navbar {
  font-family: "Prompt", sans-serif;
}
</style>