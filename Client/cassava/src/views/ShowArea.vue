<template>
  <div id="show-area">
    <v-container>
      <v-row>
        <v-col style="margin-right:1vh" cols="12" md="4" sm="4"
          ><v-btn id="addbutton" rounded
            >+ เพิ่มข้อมูลมันสำปะหลัง</v-btn
          ></v-col
        >
        <v-col cols="12" md="3" sm="3">
          <v-btn rounded>กราฟ</v-btn>
        </v-col>
        <v-col cols="12" md="3" sm="3">
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
      <v-row id="everythingisonfire">
        <v-col cols="9">
          <GmapMap id="showmap"
            :center="{ lat: latitude, lng: longitude }"
            :zoom="16"
            map-type-id="terrain"
          >
            <GmapMarker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="true"
              @click="center = m.position"
            />
          </GmapMap>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-row align="center">
            <v-col cols="3"
              ><v-img id="pin"
                src="../assets/Agradeicon.png"
              ></v-img></v-col
            >เกรด A</v-row
          >
          <v-row align="center">
            <v-col cols="12" md="3" sm="3"
              ><v-img id="pin"
                src="../assets/Bgradeicon.png"
              ></v-img></v-col
            >เกรด B</v-row
          >
          <v-row align="center">
            <v-col cols="12" md="3" sm="3"
              ><v-img id="pin"
                src="../assets/Cgradeicon.png"
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
          <v-btn id="backbutton" rounded style="margin-end: 10px">ย้อนกลับ</v-btn>
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
    latitude:16.4411261,
    longitude:102.8644933,
  }),
};
</script>
<style scoped>
.detailtext {
  text-align: center;
}
#showmap{
  width: 100%;
  height: 100%;
}
#pin{
  max-width: 1vw;
  min-width: 1vw;
}
#backbutton{
  margin-right: 10vw;
  border-radius: 10vh;
}
#addbutton{
  background-color: #1CE227;
}
#marginaddbutton{
  margin-right: 1vw;
}
</style>