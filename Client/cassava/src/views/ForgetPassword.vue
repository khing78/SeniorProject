<template>
  <v-main class="forgetpassword">
    <v-container fill-height style="width: 100%">
      <v-card width="400" class="mx-auto mt-5">
        <div id="formregister">
          <div id="titleregister">ลืมรหัสผ่าน</div>
          <div id="inputregister">
            {{errormessage}}
            อีเมล
            <v-text-field
              v-model="email"
              :rules="[rules.email]"
            ></v-text-field>
          </div>
          <div id="suandfobuttongroup">
            <v-btn id="cancelbutton" > ยกเลิก </v-btn>
            <v-btn id="confirmbutton" :disabled = "!email"> ยืนยัน </v-btn>
          </div>
        </div>
      </v-card>
    </v-container>
  </v-main>
</template>

<script>
export default {
  data: () => ({
    reg: /\S+@\S+\.\S+/,
    errorM:"",
    email: "",
    show1: false,
    show2: false,
    rules: {
      required: (value) => !!value || "Required.",
      email: value => {
            const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return pattern.test(value) || 'Invalid e-mail.'
          },

    },
  }),
  methods: {},
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