<template>
<div>
    <w-app>
        <w-drawer class="dialogbox" v-model="$store.state.openDrawer" :[position]="true">
            <w-flex column>
                <w-tag xl height="2em" class="label1" bg-color="primary">Floor Selection</w-tag>
                <w-button class="cross" @click="$store.state.openDrawer = false" bg-color="white" outline absolute round icon="wi-cross">
                </w-button>
                <w-radios class="checkboxes" v-model="$store.state.selection" :items="radioItems">
                </w-radios>

                <w-button @click="floorView()" :loading="button2loading" class="updateButton">Update Model</w-button>
            </w-flex>
        </w-drawer>
    </w-app>
</div>
</template>

<script>
import store from "../store/index";
export default {
    data: () => ({
        button2loading: false,
        election: 1,
        radioItems: [{
                label: 'SSOL',
                value: 1
            },
            {
                label: 'RDC',
                value: 2
            },
            {
                label: 'ENTRESOL',
                value: 3
            },
            {
                label: 'FIRST FLOOR',
                value: 4
            },
            {
                label: 'SECOND FLOOR',
                value: 5
            },
            {
                label: 'THIRD FLOOR',
                value: 6
            },
            {
                label: 'FOURTH FLOOR',
                value: 7
            },
            {
                label: 'FIFTH FLOOR',
                value: 8
            },
            {
                label: 'SIXTH FLOOR',
                value: 9
            }

        ]
    }),
    computed: {
        position() {
            return store.state.openDrawer || "right";
        },
    },
    methods: {
        floorView() {
            this.buttonDoLoading(2)
            store.dispatch("createFloorView")

        },
        buttonDoLoading(id) {
            this[`button${id}loading`] = true
            setTimeout(() => (this[`button${id}loading`] = false), 3000)
        }
    }
};
</script>

<style scoped>
.floorview {
    position: absolute;
    top: 40px;
    width: 100%;
}

.dialogbox {
    z-index: 200002;
}

.cross {
    position: absolute;
    z-index: auto;
    top: 5px;
}

.label1 {
    position: absolute;
    z-index: auto;
    width: 100%;
}

.checkboxes {
    position: absolute;
    top: 50px;
    width: 100%;
    left: 30px
}

.updateButton {
    position: absolute;
    top: 260px;
    width: 100%
}
</style>
