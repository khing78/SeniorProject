<template>
  <div class="show-all-area">
    <v-container>
      <v-row>
        <v-btn color="#1CE227" rounded>+ เพิ่มแปลงใหม่</v-btn>
        <v-col cols="12" md="2" sm="3">
          <v-combobox
            v-model="selectstate"
            :items="itemsstate"
            label="จังหวัด"
            outlined
            dense
          ></v-combobox>
        </v-col>
        <v-col cols="12" md="2" sm="3">
          <v-combobox
            v-model="selectdistrict"
            :items="itemsdistrict"
            label="อำเภอ"
            outlined
            dense
          ></v-combobox>
        </v-col>
        <v-col cols="12" md="2" sm="3">
          <v-combobox
            v-model="selectgrade"
            :items="itemsgrade"
            label="สถานะ"
            outlined
            dense
          ></v-combobox>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="8" sm="8">
          <GmapMap
            :center="{ lat: latitude, lng: longitude }"
            :zoom="12"
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
        <v-col cols="12" md="4" sm="4">
          <v-simple-table fixed-header id="table">
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center" id="areaname">
                    ชื่อแปลง
                  </th>
                  <th class="text-center" id="areaname">
                    รายละเอียด
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="elevation-1"
                  v-for="item in detailarea"
                  :key="item.name"
                  style="text: center"
                >
                  <td>{{ item.name }}</td>
                  <td>{{ item.desciption }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    selectstate: "",
    itemsstate: ["ขอนแก่น", "เลย", "เชียงใหม่", "อุบลราชธานี"],
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เวียงเก่า", "บ้านแฮด", "บ้านฝาง"],
    selectgrade: "",
    itemsgrade: ["A", "B", "C"],
    latitude: 16.4411261,
    longitude: 102.8644933,
    detailarea: [
      {
        name: "แปลงสมชาย",
        desciption: "อ.เมือง จ.ขอนแก่น",
      },
      {
        name: "แปลงสมศรี",
        desciption: "อ.เวียงเก่า จ.ขอนแก่น",
      },
      {
        name: "แปลงมารี",
        desciption: "อ.บ้านแฮด จ.ขอนแก่น",
      },
    ],
  }),
};
</script>
<style scoped>
#table {
  height: 400px;
  padding-bottom: 20px;
}
#areaname{
  background-color: #ffa9a9
}

</style>