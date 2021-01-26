<template>
  <v-main class="login">
    <v-container id="mainbackground" fill-height fluid style="width: 100%">
      <v-card width="400" class="mx-auto mt-5">
        <div id="formlogin">
          <div id="titlelogin">เข้าสู่ระบบ</div>
          <div id="errormessager">{{ errorM }}</div>
          <div id="inputlogin">
            อีเมล
            <v-text-field v-model="email" :rules="[rules.email]"></v-text-field>
            รหัสผ่าน
            <v-text-field
              v-model="password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show1 ? 'text' : 'password'"
              :rules="[rules.required, rules.min]"
              @click:append="show1 = !show1"
            ></v-text-field>
          </div>
          <div id="suandfobuttongroup">
            <v-btn id="forgotbutton" text @click="moveto('forgetpassword')">
              ลืมรหัสผ่าน
            </v-btn>
            <v-btn id="signupbutton" text @click="moveto('register')">
              สร้างบัญชี
            </v-btn>
          </div>
          <v-btn id="loginbutton" @click="loginfun(email, password)">
            เข้าสู่ระบบ
          </v-btn>
        </div>
      </v-card>
      <v-row id="loginfield" justify="center" align="center"> </v-row>
    </v-container>
  </v-main>
</template>

<script>
import axios from "axios";
import firebase from "firebase/app";
import "firebase/auth";
export default {
  data: () => ({
    reg: /\S+@\S+\.\S+/,
    email: "",
    password: "",
    errorM: "",
    show1: false,
    user: "",
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => v.length >= 8 || "Min 8 characters",
      emailMatch: () => `The email and password you entered don't match`,
      email: (value) => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return pattern.test(value) || "Invalid e-mail.";
      },
    },
  }),
  created(){
    this.checkloginstate()
  },
  methods: {
    moveto(i) {
      console.log(i);
      const vm = this;
      if (i == "register") {
        vm.$router.push("/register");
      } else if (i == "forgetpassword") {
        vm.$router.push("/forgetpassword");
      }
    },
    async checkloginstate() {
      const vm = this;
      firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
          vm.$router.push("/show-all-area");
        }
      });
    },
    loginfun(email, password) {
      const vm = this;
      firebase
        .auth()
        .signInWithEmailAndPassword(email, password)
        .then((user) => {
          axios
            .get("http://127.0.0.1:8000/uids/")
            .then((response) => {
              var i = 0;
              while (i < response.data.length) {
                if (response.data[i].uId == user.user.uid) {
                  this.$store.commit({
                    type: "setUserName",
                    username: response.data[i].username,
                  });
                  break;
                }
                i++;
              }
            })
            .catch((err) => {
              console.error(err);
            });
          this.$store.commit({
            type: "setUid",
            uid: user.user.uid,
          });
          vm.$router.push("/show-all-area");
        })
        .catch((error) => {
          //var errorCode = error.code;
          var errorMessage = error.message;
          // ..
          this.errorM = errorMessage;
        });
    },
  },
};
</script>
<style scoped>
#titlelogin {
  margin-bottom: 2vh;
}
#input {
  margin-right: 2vw;
}
#formlogin {
  padding: 30px;
}
#suandfobuttongroup {
  margin-bottom: 1vh;
}
#mainbackground {
  background: darkred;
}
</style>