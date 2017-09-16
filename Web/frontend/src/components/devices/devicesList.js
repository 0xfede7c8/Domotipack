import React, { Component } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import _ from 'lodash';
import { fetchDevices, updateDevice, updateAllDevices, URL} from '../../reducers/reducer_devices';
import  openSocket from 'socket.io-client';

import CircularProgress from 'material-ui/CircularProgress';
import Device from './device';

class DevicesList extends Component {

    componentDidMount(){
        this.props.fetchDevices();
        this.websocket = openSocket(URL);
        this.websocket.on('update_devices',(devices)=>{
            this.props.updateAllDevices(devices);
        });
    }

    renderDevices(){
        const handleStateChange = _.debounce((term) => {
            this.props.updateDevice(term)},500);
        const {devices} = this.props;
        const devices_list = Object.keys(devices);
        return devices_list.map((id)=>{
            const device = devices[id];
            return (
                <Device 
                    key={device.id} 
                    device={device}
                    onStateChange={handleStateChange.bind(this)}
                />
            );
       });
    }
    
    render(){
        if(!this.props.devices){
            return (
                <div style={{"margin":"0 auto", "display":"table", "marginTop":"25%"}}>
                    <CircularProgress size={100} />
                </div>
            );
        }
        return ( 
            <div >
               {  this.renderDevices() }
            </div>
        );
    }
}


function mapStateToProps(state){
    return {
        devices : state.devices
    }
}

function mapDispatchToProps(dispatch){
    return bindActionCreators({fetchDevices: fetchDevices,
                               updateDevice: updateDevice,
                               updateAllDevices : updateAllDevices},
                               dispatch);
}


export default connect(mapStateToProps, mapDispatchToProps)(DevicesList)
