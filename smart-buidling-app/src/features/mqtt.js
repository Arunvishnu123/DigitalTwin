import mqtt from "mqtt"
import store from "../store/index"

export function readMQTT(){
    console.log("test")
    let value 
    const host = 'ws://193.49.165.77:3128'
    const options = {
        clean: true,
        connectTimeout: 4000,     
    }
    const client  = mqtt.connect(host,options)
    const client1  = mqtt.connect(host,options)
    console.log(client)
    client.subscribe("emse/fayol/device/P8/temperature", function() {
        client.on('message', function(topic, message, packet) {
          console.log("recrveed",message.toString())
          value = message.toString()
          store.state.readTemperature = message.toString()
        });
    });

    client1.subscribe("emse/fayol/4ET/418/window/state", function() {
        client1.on('message', function(windowTopic, windowStatus, windowPackets) {
                 
          store.state.windowOpen421FD  = windowStatus.toString()
          if(store.state.windowOpen421FD){
              store.state.windowImage = "src/assets/windowOpen.PNG"
          }else{
            store.state.windowImage = "src/assets/windowClosed.PNG" 
          }

          console.log("recrvefgfdgdfged",store.state.windowOpen421FD) 
        });
    });
}