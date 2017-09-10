import React, { Component } from 'react';
import Light from './devices/device_light';
import Alarm from './devices/device_alarm';

class DevicesList extends Component {
    render(){
        return (
            <div>
                <Light/>
                <Alarm/>
            </div>
        );
    }
}

export default DevicesList
