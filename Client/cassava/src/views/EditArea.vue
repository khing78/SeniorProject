<template>
  <div class="edit-area">
    <v-container>
      <v-btn>ลบแปลง</v-btn>
      <v-row>
        <v-col cols="12" md="9" sm="9">
          <GmapMap
            :center="{ lat: latitude, lng: longitude }"
            :zoom="7"
            map-type-id="terrain"
            style="width: 100%; height: 100%"
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
          <v-row>
            <v-col cols="12" md="6" class="text-center">
              <v-btn id="addpinbutton" rounded> เพิ่มหมุด </v-btn>
            </v-col>
            <v-col cols="12" md="6" class="text-center">
              <v-btn rounded> ลบหมุด </v-btn>
            </v-col>
            
          </v-row>
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
            v-model="latitude"
            hint="กรุณาใส่ละติจูด (หากมี)"
            label="ละติจูด (หากมี)"
          ></v-text-field>
          <v-text-field
            v-model="longitude"
            hint="กรุณาใส่ลองจิจูด (หากมี)"
            label="ลองจิจูด (หากมี)"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn id="backbutton" rounded href="../show-area">ย้อนกลับ</v-btn>
          <v-btn id="savebutton" rounded href="../show-area">บันทึก</v-btn>
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
    latitude: 16.4411261,
    longitude: 102.8644933,
    areaname: "",
    selectstate: "",
    itemsstate: ["ขอนแก่น", "เลย", "เชียงใหม่", "อุบลราชธานี"],
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เลย", "เชียงใหม่", "อุบลราชธานี"],
  }),
};
</script>
<style scoped>
#addpinbutton {
  color: #ffffff;
  background-color: #2643b6;
}
#backbutton{
  margin-right: 2vw;
}
#savebutton{
  background-color: #1CE227;
}
</style>