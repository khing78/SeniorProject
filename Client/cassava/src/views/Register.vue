<template>
  <v-main class="register">
    <v-container fill-height style="width: 100%">
      <v-card width="400" class="mx-auto mt-5">
        <div id="formregister">
          <div id="titleregister">สมัครสมาชิก</div>
          <div id="inputregister">
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
            ยืนยันรหัสผ่าน
            <v-text-field
              v-model="confirmpassword"
              :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
              :type="show2 ? 'text' : 'password'"
              :rules="[rules.required, rules.min]"
              @click:append="show2 = !show2"
            ></v-text-field>
          </div>
          <div id="suandfobuttongroup">
            <v-btn id="cancelbutton"> ยกเลิก </v-btn>
            <v-btn id="confirmbutton" @click="registerfun(email,password)"> ยืนยัน </v-btn>
          </div>
        </div>
      </v-card>
    </v-container>
  </v-main>
</template>

<script>
import firebase from "firebase/app";
import "firebase/auth";
export default {
  data: () => ({
    reg: /\S+@\S+\.\S+/,
    email: "",
    password: "",
    confirmpassword: "",
    show1: false,
    show2: false,
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
  methods: {
    registerfun(email,password) {
      firebase
        .auth()
        .createUserWithEmailAndPassword(email, password)
        .then((user) => {
          console.log(user)
        })
        .catch((error) => {
          var errorCode = error.code;
          var errorMessage = error.message;
          // ..
          console.log(errorCode)
          console.log(errorMessage)
        });
    },
  },
};
</script>
<style scoped>
#titleregister {
  margin-bottom: 2vh;
}
#inputregister {
  margin-right: 2vw;
}
#formregister {
  padding: 30px;
}
#cancelbutton {
  margin-right: 1vw;
}
</style>