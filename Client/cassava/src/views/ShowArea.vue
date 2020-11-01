<template>
  <div class="show-area">
    <v-container>
      <v-row>
        <v-col cols="2"
          ><v-btn color="#1CE227" rounded
            >+ เพิ่มข้อมูลมันสำปะหลัง</v-btn
          ></v-col
        >
        <v-col cols="3" class="text-right">
          <v-btn rounded>กราฟ</v-btn>
        </v-col>
        <v-col cols="4">
          <v-menu
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="date"
                label="วัน/เดือน/ปี ที่บันทึก"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date"
              @input="menu2 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="9">
          <!-- For Map -->
        </v-col>
        <v-col cols="3">
          <v-row align="center">
            <v-col cols="3"
              ><v-img
                src="../assets/Agradeicon.png"
                max-height="200px"
                max-width="20px"
              ></v-img></v-col
            >เกรด A</v-row
          >
          <v-row align="center">
            <v-col cols="3"
              ><v-img
                src="../assets/Bgradeicon.png"
                max-height="200px"
                max-width="20px"
              ></v-img></v-col
            >เกรด B</v-row
          >
          <v-row align="center">
            <v-col cols="3"
              ><v-img
                src="../assets/Cgradeicon.png"
                max-height="200px"
                max-width="20px"
              ></v-img></v-col
            >เกรด C</v-row
          >
          <div class="detailtext">
            คุณภาพโดยรวมทั้งแปลง
            <br />
            เกรด A: {{ gradeAtotal }} %
            <br />
            เกรด B: {{ gradeBtotal }} %
            <br />
            เกรด C: {{ gradeCtotal }} %
            <br />
            เปอร์เซ็นต์แปลงโดยเฉลี่ย
            <br />
            {{ totalstarch }} %
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn rounded style="margin-end: 10px">ย้อนกลับ</v-btn>
          <v-btn color="#FFB200" rounded>จัดการแปลง</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    gradeAtotal: 10,
    gradeBtotal: 50,
    gradeCtotal: 40,
    totalstarch: 50,
  }),
};
</script>
<style scoped>
.detailtext {
  text-align: center;
}
</style>