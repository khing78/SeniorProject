<template>
  <v-main class="forgetpassword">
    <v-container id="mainbackground" fill-height fluid style="width: 100%">
      <v-card width="400" class="mx-auto mt-5">
        <div id="formregister">
          <div id="titleregister" style="font-size: 28px">ลืมรหัสผ่าน</div>
          <div id="inputregister">
            {{errorM}}
            อีเมล
            <v-text-field v-model="email" :rules="[rules.email]"></v-text-field>
          </div>
          <div id="suandfobuttongroup">
            <v-btn id="cancelbutton" @click="moveto('back')"> ยกเลิก </v-btn>
            <v-btn id="confirmbutton" :disabled="!email" @click="forgetpasswordfunction()"> ยืนยัน </v-btn>
          </div>
        </div>
      </v-card>
    </v-container>
  </v-main>
</template>

<script>
import firebase from "firebase/app";
export default {
  data: () => ({
    reg: /\S+@\S+\.\S+/,
    errorM: "",
    email: "",
    show1: false,
    show2: false,
    rules: {
      required: (value) => !!value || "Required.",
      email: (value) => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return pattern.test(value) || "Invalid e-mail.";
      },
    },
  }),
  methods: {
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/");
      }
    },
    forgetpasswordfunction() {
      var auth = firebase.auth()
      var emailAddress = this.email

      auth
        .sendPasswordResetEmail(emailAddress)
        .then(
          // Email sent.
          this.errorM = "ส่งอีเมลสำเร็จ โปรดตรวจสอบอีเมลเพื่อรีเซ็ทรหัสผ่าน"
        )
        .catch((error) => {
          var errorMessage = error.message;
          // ..
          this.errorM = errorMessage;
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
#mainbackground {
  background-color: #9ACD32	 ;
}
</style>