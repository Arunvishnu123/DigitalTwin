import mqtt from "mqtt"
import store from "../../../../store/index"

export function readMQTT() {
  console.log("test")
  let value
  const host = 'ws://193.49.165.77:3128'
  const options = {
    clean: true,
    connectTimeout: 4000,
  }
  const client = mqtt.connect(host, options)
  const client1 = mqtt.connect(host, options)
  console.log(client)
  client.subscribe("emse/fayol/device/P8/temperature", function () {
    client.on('message', function (topic, message, packet) {
      console.log("recrveed", message.toString())
      value = parseFloat(message.toString())
      store.state.readTemperature = value.toFixed(2)
    });
  });

  client1.subscribe("emse/fayol/4ET/418/window/state", function () {
    client1.on('message', function (windowTopic, windowStatus, windowPackets) {
      console.log("windowStatus", windowStatus)
      if (windowStatus.toString() === "true") {
        store.state.windowImage = "src/assets/windowOpen.PNG"
        store.state.windowOpen421FD = "Window Opened"
        store.state.windowStatus = true
        store.state.model.scene.objects["1jMGJTzbX0Gu65H0cXPmD5"].colorize = [0, 1, 0]
      }

      if (windowStatus.toString() === "false") {
        store.state.windowImage = "src/assets/windowClosed.PNG"
        store.state.windowOpen421FD = "Window Closed"
        store.state.windowStatus = false
        store.state.model.scene.objects["1jMGJTzbX0Gu65H0cXPmD5"].colorize = [1, 0, 0]
      }

      console.log("recrvefgfdgdfged", store.state.windowOpen421FD)
    });
  });
}