<template>
  <div class="nav-bar">
    <v-app-bar color="white" dense dark>
      <v-toolbar-title style="margin-top: 0px" class="navbar"
        ><v-btn
          text
          @click="moveto('backtonormal')"
          style="color: #0E8317; "
          >ระบบแสดงคุณภาพมันสำปะหลัง</v-btn
        ></v-toolbar-title
      >
      <v-spacer />
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="white" v-bind="attrs" v-on="on" text :disabled="!name">
            <div id="username" style="color: #1ce227; padding-right: 10vm; font-size: 18px">
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
      <!-- <v-avatar><v-img id="imagecharacter" :src="imagesrc"></v-img></v-avatar> -->
    </v-app-bar>
  </div>
</template>
<script>
import axios from "axios";
import firebase from "firebase/app";
import { mapGetters } from "vuex";
export default {
  data: () => ({
    imagesrc: "../assets/iconusercc.png",
  }),
  created(){
    //this.checkloginstate()
  },
  methods: {
    moveto() {
      const vm = this;
      firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
          vm.$router.push("/show-all-area");
        } else {
          vm.$router.push("/");
        }
      });
    },
    async checkloginstate() {
      const vm = this;
      firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
         axios
            .get("http://143.198.205.220:8000/uids/")
            .then((response) => {
              var i = 0;
              while (i < response.data.length) {
                if (response.data[i].uId == user.uid) {
                  vm.$store.commit({
                    type: "setUserName",
                    username: response.data[i].username,
                  });
                  break
                }
                i++
              }
            })
          console.log(user.uid);
          vm.$store.commit({
            type: "setUid",
            uid: user.uid,
          });
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
          vm.$store.commit({
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
.v-toolbar__content{
  width: auto;
}
@media screen and (min-width: 601px) {
  .v-btn__content {
    font-size: 22px;
  }
}

@media screen and (max-width: 600px) {
  .v-btn__content {
    font-size: 12px;
  }
}
</style>