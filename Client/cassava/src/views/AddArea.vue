<template>
  <v-main class="add-area">
    <v-container>
      <v-row>
        <!-- For Map -->
        <v-col cols="12" md="9">
          <gmap-map
            id="map"
            :center="mapcenter"
            :zoom="16"
            style="width: 100%; height: 500px"
            map-type-id="satellite"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="true"
              @click="checkmap(m.position)"
            ></gmap-marker>
            <gmap-polyline
              v-if="path.length > 0"
              :path="path"
              :editable="disable"
              @path_changed="updateEdited($event)"
              @rightclick="handleClickForDelete"
              ref="polyline"
            >
            </gmap-polyline>
          </gmap-map>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="3">
          <v-text-field
            v-model="areaname"
            hint="กรุณาใส่ชื่อแปลง"
            label="ชื่อแปลง"
          ></v-text-field>
          <v-menu
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="computedDateFormatted"
                label="วัน/เดือน/ปี ที่ปลูก"
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
          <v-row>
            <v-container fluid>
              <v-row>
                <v-col>
                  <v-combobox
                    v-model="selectstate"
                    :items="itemsstate"
                    label="จังหวัด"
                    outlined
                    dense
                  ></v-combobox>
                  <v-combobox
                    v-model="selectdistrict"
                    :items="itemsdistrict"
                    label="อำเภอ"
                    outlined
                    dense
                  ></v-combobox>
                </v-col>
              </v-row>
            </v-container>
          </v-row>
          <v-text-field
            v-model="mapcenter.lat"
            hint="กรุณาใส่ละติจูด"
            label="ละติจูด"
          ></v-text-field>
          <v-text-field
            v-model="mapcenter.lng"
            hint="กรุณาใส่ลองจิจูด"
            label="ลองจิจูด"
          ></v-text-field>
          <v-text-field
            v-model="mapcenter.wide"
            hint="กรุณาใส่ความกว้าง"
            label="ความกว้าง"
          ></v-text-field>
          <v-text-field
            v-model="mapcenter.long"
            hint="กรุณาใส่ความยาว"
            label="ความยาว"
          ></v-text-field>
          <v-col cols="12">
            <v-btn @click="changepositionmap(mapcenter.lat, mapcenter.lng)"
              >ตั้งจุดใหม่</v-btn
            >
          </v-col>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn rounded style="margin-end: 10px" @click="moveto('back')"
            >ยกเลิก</v-btn
          >
          <v-btn color="#1CE227" rounded @click="moveto('save')">บันทึก</v-btn>
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
    mapcenter: { lat: 16.4411261, lng: 102.8644933, wide: 100, long: 100 },
    path: [
      { lat: 1.33, lng: 103.75 },
      { lat: 1.43, lng: 103.85 },
    ],
    positiona: {},
    markers: [
      { Id: 1, name: "1", position: { lat: 16.466022, lng: 102.898313 } },
    ],
    areaname: "",
    selectstate: "",
    itemsstate: [
      "กระบี่",
      "กรุงเทพมหานคร",
      "กาญจนบุรี",
      "กาฬสินธุ์",
      "กำแพงเพชร",
      "ขอนแก่น",
      "จันทบุรี",
      "ฉะเชิงเทรา",
      "ชลบุรี",
      "ชัยนาท",
      "ชัยภูมิ",
      "ชุมพร",
      "เชียงราย",
      "เชียงใหม่",
      "ตรัง",
      "ตราด",
      "ตาก",
      "นครนายก",
      "นครปฐม",
      "นครพนม",
      "นครราชสีมา",
      "นครศรีธรรมราช",
      "นครสวรรค์",
      "นนทบุรี",
      "นราธิวาส",
      "น่าน",
      "บึงกาฬ",
      "บุรีรัมย์",
      "ปทุมธานี",
      "ประจวบคีรีขันธ์",
      "ปราจีนบุรี",
      "ปัตตานี",
      "พระนครศรีอยุธยา",
      "พะเยา",
      "พังงา",
      "พัทลุง",
      "พิจิตร",
      "พิษณุโลก",
      "เพชรบุรี",
      "เพชรบูรณ์",
      "แพร่",
      "ภูเก็ต",
      "มหาสารคาม",
      "มุกดาหาร",
      "แม่ฮ่องสอน",
      "ยโสธร",
      "ยะลา",
      "ร้อยเอ็ด",
      "ระนอง",
      "ระยอง",
      "ราชบุรี",
      "ลพบุรี",
      "ลำปาง",
      "ลำพูน",
      "เลย",
      "ศรีสะเกษ",
      "สกลนคร",
      "สงขลา",
      "สตูล",
      "สมุทรปราการ",
      "สมุทรสงคราม",
      "สมุทรสาคร",
      "สระแก้ว",
      "สระบุรี",
      "สิงห์บุรี",
      "สุโขทัย",
      "สุพรรณบุรี",
      "สุราษฎร์ธานี",
      "สุรินทร์",
      "หนองคาย",
      "หนองบัวลำภู",
      "อ่างทอง",
      "อำนาจเจริญ",
      "อุดรธานี",
      "อุตรดิตถ์",
      "อุทัยธานี",
      "อุบลราชธานี",
    ],
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เวียงเก่า", "บ้านแฮด", "บ้านฝาง"],
  }),
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },
  methods: {
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/show-all-area");
      } else if (i == "save") {
        vm.$router.push("/show-all-area");
      }
    },
    changefrommetertolatlong(width,long) {
      //เปลี่ยน กว้างยาว เป็น lat long
      console.log(width)
      console.log(long)
      this.path = [
          {
            lat: this.path[0].lat - 0.01, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
            lng: this.path[0].lng,
          },
          {
            lat: this.path[0].lat,
            lng: this.path[0].lng,
          },
          {
            lat: this.path[0].lat,
            lng: this.path[0].lng + 0.01 //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
            ,
          },
        ]
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },
    changepositionmap(newlat, newlng) {
      this.mapcenter.lat = Number(newlat);
      this.mapcenter.lng = Number(newlng);
    },
    checkmap(k) {
      this.positiona = k;
      console.log(k);
    },
    addpinfun() {
      const lenghtmarker = this.markers.length;
      const po = this.mapcenter;
      if (this.markers.length == 0) {
        this.markers.push({
          Id: lenghtmarker + 1,
          name: (lenghtmarker + 1).toString(),
          position: po,
        });
      } else {
        this.markers.push({
          Id: lenghtmarker + 1,
          name: (lenghtmarker + 1).toString(),
          position: po,
        });
      }
    },
    deletedpinfun() {
      const lenghtmarker = this.markers.length;
      this.markers.pop({ Id: lenghtmarker });
    },
  },
  created() {
    navigator.geolocation.getCurrentPosition((position) => {
      (this.mapcenter = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
        wide: 100,
        long: 100,
      }),
        (this.markers = [
          {
            Id: 1,
            name: "1",
            position: {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            },
          },
        ]),
        (this.path = [
          {
            lat: position.coords.latitude - 0.01,
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude + 0.01,
          },
        ]),
        console.log(this.markers);
    });
    if (this.mapcenter.lat == null) {
      this.mapcenter.lat = 16.4411261;
      this.mapcenter.lng = 102.8644933;
    }
  },
};
</script>
<style scoped>
#addpinbutton {
  color: #ffffff;
  background-color: #2643b6;
  margin-bottom: 1vh;
}
</style>