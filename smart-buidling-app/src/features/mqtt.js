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
    console.log(client)
    client.subscribe("emse/fayol/device/P8/temperature", function() {
        client.on('message', function(topic, message, packet) {
          console.log("recrveed",message.toString())
          value = message.toString()
          store.state.readTemperature = message.toString()
        });
    });

    client.subscribe("emse/fayol/4ET/429/window/state", function() {e
        client.on('message', function(topic, message, packet) {
          console.log("recrvefgfdgdfged",message.toString())        
          store.state.windowOpen421FD  = message.toString()
        });
    });
}