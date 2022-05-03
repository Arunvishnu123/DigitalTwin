<template>
<div>
    <div id="main"></div>
</div>
</template>

<script>
import * as echarts from "echarts/core";
import {
    GaugeChart
} from "echarts/charts";
import {
    CanvasRenderer
} from "echarts/renderers";
import store from "../store/index"
echarts.use([GaugeChart, CanvasRenderer]);

export default {
    name: "App",
    data: function () {
        return {};
    },
    mounted() {
        var dom = document.getElementById("main");
        var myChart = echarts.init(dom, null, {
            renderer: "canvas",
            useDirtyRect: false,
        });

        var option;

        option = {
            series: [{
                type: "gauge",
                min: 0,
                max: 50,
                axisLine: {
                    lineStyle: {
                        width: 30,
                        color: [
                            [0.31, "blue"],
                            [0.35, "yellow"],
                            [0.41, "green"],
                             [0.5, "orange"],
                             [0.58, "red"],
                             [0.66, "purple"],
                             [1,"black"]
                        ],
                    },
                },
                pointer: {
                    itemStyle: {
                        color: "red",
                    },
                },
                axisTick: {
                    distance: -30,
                    length: 10,
                    lineStyle: {
                        color: "#fff",
                        width: 2,
                    },
                },
                splitLine: {
                    distance: -30,
                    length: 30,
                    lineStyle: {
                        color: "#fff",
                        width: 4,
                    },
                },
                axisLabel: {
                    color: "auto",
                    distance: 40,
                    fontSize: 20,
                },
                detail: {
                    valueAnimation: true,
                    formatter: "{value}°C",
                    color: "auto",
                },
                data: [{
                    value: store.state.readTemperature,
                }, ],
            }, ],
        };

        if (option && typeof option === "object") {
            myChart.setOption(option);
        }

        //window.addEventListener('resize', myChart.resize);
    },
};
</script>

<style>
* {
    margin: 0;
    padding: 0;
}

#main {
    position: relative;
    height: 50vh;
    width: 50hv;
    overflow: hidden;
}
</style>
