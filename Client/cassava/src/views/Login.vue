<template>
  <div class="login">
    <v-container fill-height style="width:100%;height: 600px">
      <v-card width="400" class="mx-auto mt-5">
        <div id="formlogin">
          <div id="titlelogin">เข้าสู่ระบบ</div>
          <div id="inputlogin">
            อีเมล
            <v-text-field v-model="id"></v-text-field>
            รหัสผ่าน
            <v-text-field v-model="password"></v-text-field>
          </div>
          <div id="suandfobuttongroup">
            <v-btn id="forgotbutton" text> ลืมรหัสผ่าน </v-btn>
            <v-btn id="signupbutton" text> สร้างบัญชี </v-btn>
          </div>
          <v-btn id="loginbutton"> เข้าสู่ระบบ </v-btn>
        </div>
      </v-card>
      <v-row id="loginfield" justify="center" align="center">
        <!-- <v-col cols="12" md="6" sm="6">
          <div id="titlelogin">เข้าสู่ระบบ</div>
          <div id="inputlogin">
            อีเมล
            <v-text-field v-model="id"></v-text-field>
            รหัสผ่าน
            <v-text-field v-model="password"></v-text-field>
          </div>
          <div id="suandfobuttongroup">
            <v-btn id="forgotbutton" text> ลืมรหัสผ่าน </v-btn>
            <v-btn id="signupbutton" text> สร้างบัญชี </v-btn>
          </div>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="12" md="6" sm="6" class="text-right">
          <div id="loginbuttongroup">
            <v-btn id="loginbutton"> เข้าสู่ระบบ </v-btn>
          </div>
        </v-col>-->
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    id: "",
    password: "",
  }),
  methods: {},
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
</style>