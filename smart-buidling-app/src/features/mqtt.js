import mqtt from "mqtt"
import store from "../store/index"

export function readMQTT(path){
    console.log("test")
    let value 
    const host = 'ws://193.49.165.77:3128'
    const options = {
        clean: true,
        connectTimeout: 4000,     
    }
    const client  = mqtt.connect(host,options)
    console.log(client)
    client.subscribe(path, function() {
        //When a message arrives, print it to the console
        client.on('message', function(topic, message, packet) {
         // console.log("Received '" + message + "' on '" + topic + "'");
          console.log("recrveed",message.toString())
          value = message.toString()
          store.state.readTemperature = message.toString()
        });
    });

    return value
}