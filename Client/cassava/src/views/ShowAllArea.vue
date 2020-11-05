<template>
  <div class="show-all-area">
    <v-container>
      <v-row>
        <v-col>
          <v-btn color="#1CE227" rounded @click="moveto('addarea')">+ เพิ่มแปลงใหม่</v-btn>
        </v-col>
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
          <gmap-map
            :center="mapcenter"
            :zoom="5"
            style="width: 100%; height: 500px"
            map-type-id="satellite"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="false"
              :draggable="false"
              @click="center = m.position"
            ></gmap-marker>
          </gmap-map>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="4" sm="4">
          <v-simple-table fixed-header id="table">
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center" id="areaname">ชื่อแปลง</th>
                  <th class="text-center" id="areaname">รายละเอียด</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="elevation-1"
                  v-for="item in markers"
                  :key="item.name"
                  style="text: center"
                  @click="moveto(item.Id)"
                >
                  <td>{{ item.name }}</td>
                  <td>{{ item.desciption }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
          <v-col class="text-center">
            <v-btn href="../show-area">ตกลง</v-btn>
          </v-col>
          
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
    mapcenter: { lat: 16.4411261, lng: 102.8644933 },
    detailarea: [
      {
        id: 1,
        name: "แปลงสมชาย",
        desciption: "อ.เมือง จ.ขอนแก่น",
      },
      {
        id: 2,
        name: "แปลงสมศรี",
        desciption: "อ.เวียงเก่า จ.ขอนแก่น",
      },
      {
        id: 3,
        name: "แปลงมารี",
        desciption: "อ.บ้านแฮด จ.ขอนแก่น",
      },
    ],
    markers: [
        { Id: 0, name: "แปลงสมชาย",desciption: "อ.เมือง จ.ขอนแก่น", position: { lat: 18.466022, lng: 102.898313 } },
        { Id: 1, name: "แปลงสมศรี",desciption: "อ.เวียงเก่า จ.ขอนแก่น", position: { lat: 16.466037 , lng: 99.899724 } },
        { Id: 2,  name: "แปลงมารี",desciption: "อ.บ้านแฮด จ.ขอนแก่น", position: { lat: 15.465616 , lng: 102.899717 }},
      ],
  }),
  methods: {
    moveto(i){
      //this.mapcenter = this.markers[i].position
      const vm = this
      if (i == 'addarea'){
        vm.$router.push("/add-area");
      }
      else{
        vm.$router.push("/show-area");
      }
      
    }
  }
};
</script>
<style scoped>
#table {
  height: 400px;
  padding-bottom: 20px;
}
#areaname {
  background-color: #ffa9a9;
}
</style>