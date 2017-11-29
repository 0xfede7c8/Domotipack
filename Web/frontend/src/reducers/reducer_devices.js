import axios from 'axios';

const HOST_IP = document.getElementById("hostip").innerHTML;
//const HOST_IP = "192.168.0.16"
export const URL = "http://".concat(HOST_IP.concat(':5000'));
export const URL_API = URL + "/api/devices";
export const FETCH_DEVICES = 'devices/FETCH_DEVICES';
export const UPDATE_DEVICE = 'devices/UPDATE_DEVICE';
export const UPDATE_ALL = 'devices/UPDATE_ALL';

export default function(state=null, action) {
    switch(action.type){

        case FETCH_DEVICES:
            if(action.payload.data){
                const devices_obj = {};
                action.payload.data.forEach((device) => {
                    devices_obj[device.id] = device;
                });
                return devices_obj;
            }
            else return state;

        case UPDATE_DEVICE:
            if(action.payload.data){
                return action.payload.data;
            }
            else{
                return state;
            }
        
        case UPDATE_ALL:
            return action.payload

        default: return state;
    }
}
export function fetchDevices(){
    const get_request = axios.get(URL_API, {
            method:'GET',
            headers: {
                'Accept':'application/json',
                'Content-Type': 'application/json'
            }
        }
    );

    return {
        type: FETCH_DEVICES,
        payload: get_request
    }
}

export function updateDevice(device){
    const _URL = URL_API+"/"+device.id;
    const put_request = axios.put(_URL,device, {
            method:'PUT',
            headers: {
                'Accept':'application/json',
                'Content-Type': 'application/json'
            }
        }
    );
    return {
        type : UPDATE_DEVICE,
        payload : put_request
    }
}
export function updateAllDevices(devices){
    return {
        type : UPDATE_ALL,
        payload : devices
    }
}
