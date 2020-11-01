<template>
  <div class="add-area">
    <v-container>
      <v-row>
        <v-col cols="9">
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
        <v-col cols="3">
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
          <v-row style="margin-bottom: 10px">
            <v-btn
              rounded
              style="
                margin-right: 20px;
                color: #ffffff;
                background-color: #2643b6;
                margin-bottom: 10px;
              "
            >
              เพิ่มหมุด
            </v-btn>
            <v-btn rounded> ลบหมุด </v-btn>
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
          <v-btn rounded style="margin-end:10px">ยกเลิก</v-btn>
          <v-btn color="#1CE227" rounded>บันทึก</v-btn>
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
    latitude: 15,
    longitude: 15,
    areaname: "",
    selectstate: "",
    itemsstate: ["ขอนแก่น", "เลย", "เชียงใหม่", "อุบลราชธานี"],
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เลย", "เชียงใหม่", "อุบลราชธานี"],
  }),
};
</script>
<style scoped>
</style>