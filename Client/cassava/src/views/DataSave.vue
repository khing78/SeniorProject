<template>
  <v-main class="data-save">
    <v-container>
      <v-row>
        <v-col cols="12" md="3" sm="3"> ข้อมูลผลตรวจคุณภาพ</v-col>
        <v-col class="text-right">
          <v-btn id="removebutton" rounded @click="moveto('deletearea')">ลบข้อมูล</v-btn>
        </v-col>
      </v-row>
      <v-row class="text-center" justify="start">
        <v-col cols="12" md="3" sm="3"
          ><v-menu
            v-model="menu2"
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="5vw"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="computedDateFormatted"
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
            ></v-date-picker> </v-menu
        ></v-col>
        <v-col cols="12" md="3" sm="3"
          ><v-text-field
            v-model="this.mapcenter.lat"
            hint="กรุณาใส่ละติจูด"
            label="ละติจูด"
          ></v-text-field
        ></v-col>
        <v-col cols="12" md="3" sm="3"
          ><v-text-field
            v-model="this.mapcenter.lng"
            hint="กรุณาใส่ลองจิจูด"
            label="ลองจิจูด"
          ></v-text-field
        ></v-col>
        <v-col cols="12" md="2" sm="3">
          <v-btn>Map</v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-btn id="savebutton" rounded>เพิ่มต้น +</v-btn>
        </v-col>
      </v-row>
      <v-simple-table
        fixed-header
        height="50vh"
        id="table"
      >
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center" style="background-color: #ffa9a9"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="text-left"
              v-for="(item, index) in xdata"
              :key="item.name"
            >
              <td>
                <v-row>
                  <v-col class="text-right"><v-btn rounded id="removebutton" @click="removecassvana(index)">ลบ</v-btn></v-col>
                </v-row>
                <v-row>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x1"
                  hint="X1"
                  label="X1"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x2"
                  hint="X2"
                  label="X2"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x3"
                  hint="X3"
                  label="X3"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.temputure"
                  hint="อุณหภูมิ"
                  label="อุณหภูมิ"
                ></v-text-field>
                </v-col>
                </v-row>
                <v-row>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x4"
                  hint="X4"
                  label="X4"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x5"
                  hint="X5"
                  label="X5"
                ></v-text-field>
                </v-col>
                <v-col cols="2">
                  <v-text-field
                  v-model="item.x6"
                  hint="X6"
                  label="X6"
                ></v-text-field>
                </v-col>
                </v-row>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-row>
        <v-col class="text-left">
          <v-btn id="backbutton" rounded @click="moveto('back')">ยกเลิก</v-btn>
        </v-col>
        <v-col class="text-right">
          <v-btn id="savebutton" rounded @click="moveto('save')">บันทึก</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
export default {
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    mapcenter: {lat: 16.466022,lng: 102.898313},
    xdata: [
      {
        id: 1,
        x1: 0.7568462,
        x2: 5.370551,
        x3: 10.28535,
        x4: 12.38871,
        x5: 24.18566,
        x6: 21.58091,
        temputure: 32.02,
      },
      {
        id: 2,
        x1: 1.892033,
        x2: 10.74111,
        x3: 20.5706,
        x4: 20.89075,
        x5: 36.91494,
        x6: 27.83622,
        temputure: 31.01,
      },
      {
        id: 3,
        x1: 1.922431,
        x2: 9.398447,
        x3: 17.14219,
        x4: 20.49366,
        x5: 38.69703,
        x6: 34.09154,
        temputure: 29.42,
      },
      {
        id: 4,
        x1: 2.270401,
        x2: 6.713198,
        x3: 15.1423,
        x4: 14.57496,
        x5: 31.8232,
        x6: 23.4575,
        temputure: 30.31,
      },
    ],
  }),
  computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },
  methods:{
    moveto(i){
      const vm = this
      if (i == "back"){
        vm.$router.push("/show-area")
      }
      if (i == "save"){
        vm.$router.push("/show-area")
      }
      if (i == 'deletearea'){
        vm.$router.push("/show-area")
      }
    },
    removecassvana(index){
      console.log(index+1)
      this.xdata.remove(index)
    },
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year)+543
      return `${day}/${month}/${newyear}`;
    },
  },
};
</script>
<style scoped>
#backbutton{
  background-color: #F2F2F2;
}
#savebutton{
  background-color: #1CE227;
}
#removebutton{
  background-color: #E21C1C;
}
#table{
  padding-bottom: 2vh; 
  padding-top: 2vh;
}
#indexhead{
  padding-right: 2vw;
}
</style>